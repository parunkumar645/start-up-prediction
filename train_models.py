"""
Quick model training script to generate models for the API
"""
import sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost as xgb
import joblib
from imblearn.over_sampling import SMOTE
import warnings

warnings.filterwarnings('ignore')

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.data_preprocessing import create_and_fit_preprocessor

print("=" * 60)
print("QUICK MODEL TRAINING")
print("=" * 60)

# Load raw data
print("\n1. Loading raw data...")
data_path = project_root / "data" / "raw" / "startups_data.csv"
df = pd.read_csv(data_path, encoding='latin-1')
print(f"   Loaded {len(df)} records with {len(df.columns)} features")

# Rename columns to match expected format
df['category_list'] = df['category_code'].astype(str)
print(f"   Columns: {list(df.columns)}")

# Preprocess data
print("\n2. Preprocessing data...")
processor = create_and_fit_preprocessor(str(data_path), encoding='latin-1')
X = processor.transform(df)
y = (df['status'] == 'acquired').astype(int)

print(f"   Feature matrix shape: {X.shape}")
print(f"   Class distribution: {y.value_counts().to_dict()}")

# Train test split
print("\n3. Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Apply SMOTE to handle class imbalance
print("\n4. Applying SMOTE for class imbalance...")
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
print(f"   After SMOTE - Train set: {X_train_smote.shape}")
print(f"   Class distribution: {pd.Series(y_train_smote).value_counts().to_dict()}")

# Create models directory
models_dir = project_root / "results" / "models"
models_dir.mkdir(parents=True, exist_ok=True)

# Train Logistic Regression
print("\n5. Training Logistic Regression...")
lr = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
lr.fit(X_train_smote, y_train_smote)
lr_score = lr.score(X_test, y_test)
print(f"   Accuracy: {lr_score:.4f}")
joblib.dump(lr, models_dir / "logistic_regression_best.pkl")
print(f"   Saved to: {models_dir / 'logistic_regression_best.pkl'}")

# Train SVM
print("\n6. Training SVM (RBF kernel)...")
svm = SVC(kernel='rbf', random_state=42, class_weight='balanced', probability=True)
svm.fit(X_train_smote, y_train_smote)
svm_score = svm.score(X_test, y_test)
print(f"   Accuracy: {svm_score:.4f}")
joblib.dump(svm, models_dir / "svm_rbf_best.pkl")
print(f"   Saved to: {models_dir / 'svm_rbf_best.pkl'}")

# Train XGBoost
print("\n7. Training XGBoost...")
# Calculate scale_pos_weight for class imbalance
scale_pos_weight = (y_train_smote == 0).sum() / (y_train_smote == 1).sum()
xgb_model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    scale_pos_weight=scale_pos_weight,
    tree_method='hist',
    device='cpu'
)
xgb_model.fit(X_train_smote, y_train_smote, verbose=False)
xgb_score = xgb_model.score(X_test, y_test)
print(f"   Accuracy: {xgb_score:.4f}")
joblib.dump(xgb_model, models_dir / "xgboost_best.pkl")
print(f"   Saved to: {models_dir / 'xgboost_best.pkl'}")

# Save feature columns
print("\n8. Saving metadata...")
feature_list = processor.feature_columns
joblib.dump(feature_list, models_dir / "feature_columns.pkl")
print(f"   Saved {len(feature_list)} feature columns")

# Save preprocessor
processor.save(str(models_dir / "preprocessor.pkl"))
print(f"   Saved preprocessor")

# Create simple SHAP explainers (using TreeExplainer for tree models)
print("\n9. Creating SHAP explainers...")
try:
    import shap
    
    # For XGBoost (TreeExplainer)
    xgb_explainer = shap.TreeExplainer(xgb_model)
    joblib.dump(xgb_explainer, models_dir / "xgboost_explainer.pkl")
    print("   Created XGBoost explainer")
    
    # For LR and SVM (KernelExplainer with sampling)
    background_data = shap.sample(X_train, min(100, len(X_train)))
    
    lr_explainer = shap.KernelExplainer(lr.predict_proba, background_data)
    joblib.dump(lr_explainer, models_dir / "logistic_explainer.pkl")
    print("   Created Logistic Regression explainer")
    
    svm_explainer = shap.KernelExplainer(svm.predict_proba, background_data)
    joblib.dump(svm_explainer, models_dir / "svm_explainer.pkl")
    print("   Created SVM explainer")
    
except Exception as e:
    print(f"   Warning: Could not create SHAP explainers: {e}")

print("\n" + "=" * 60)
print("✓ MODEL TRAINING COMPLETE!")
print("=" * 60)
print("\nModels are ready! The API can now use them.")
print(f"All files saved to: {models_dir}")

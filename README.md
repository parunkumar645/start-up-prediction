# 🚀 *Machine Learning Startup Success Predictor*

**Status**: ✅ **FULLY OPERATIONAL & PRODUCTION READY** (Updated: January 20, 2026)

A complete full-stack machine learning application that predicts startup acquisition success using intelligent feature engineering and multiple ML algorithms. Built with Next.js frontend, FastAPI backend, XGBoost, Logistic Regression, and SVM models with SHAP explainability.

## 📋 Table of Contents
- [🎯 Project Status](#-project-status)
- [⚡ Quick Start (5 Minutes)](#-quick-start-5-minutes)
- [🎓 Complete Setup Guide](#-complete-setup-guide)
- [🖥️ How to Run](#️-how-to-run)
- [📱 Using the Application](#-using-the-application)
- [📊 Technology Stack](#-technology-stack)
- [🏗️ Project Structure](#️-project-structure)
- [🤖 Machine Learning Models](#-machine-learning-models)
- [📈 API Endpoints](#-api-endpoints)
- [🔍 Features & Methodology](#-features--methodology)
- [📚 Learn More](#-learn-more)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🎯 Project Status

### ✅ Currently Running (January 20, 2026)

| Component | Status | Port | Tech Stack |
|-----------|--------|------|-----------|
| **Frontend** | ✅ RUNNING | 3000 | Next.js 15.4.5, React 19, TypeScript, Tailwind CSS |
| **Backend API** | ✅ RUNNING | 8000 | FastAPI, Python 3.14 |
| **XGBoost Model** | ✅ LOADED | - | 80.5% Accuracy |
| **Logistic Regression** | ✅ LOADED | - | 48.7% Accuracy |
| **SVM Model** | ✅ LOADED | - | 46.3% Accuracy |
| **SHAP Explainers** | ✅ LOADED | - | Model Interpretability |
| **Data Preprocessor** | ✅ LOADED | - | Feature Engineering |

---

## ⚡ Quick Start (5 Minutes)

### For Students Who Just Want to See It Work

```bash
# Terminal 1: Start Backend API
cd e:\ML-Startup-Success-Prediction
python -m uvicorn app.app:app --host localhost --port 8000

# Terminal 2: Start Frontend
cd e:\ML-Startup-Success-Prediction\startup-predictor
npm run dev

# Then open browser to:
# http://localhost:3000
```

**That's it!** The application will load with all models ready. Fill in the form and click "Predict"! 🎉

---

## 🎓 Complete Setup Guide

### Step 1: Prerequisites Installation

**A. Install Python 3.14**
- Download from: https://www.python.org/downloads/
- Add Python to PATH during installation
- Verify: `python --version`

**B. Install Node.js (v24+)**
- Download from: https://nodejs.org/
- Includes npm automatically
- Verify: `node --version` and `npm --version`

**C. Install Git** (optional but recommended)
- Download from: https://git-scm.com/

### Step 2: Clone/Download Project

```bash
# Option 1: Clone from GitHub
git clone https://github.com/yourusername/ML-Startup-Success-Prediction.git
cd ML-Startup-Success-Prediction

# Option 2: Download ZIP and extract
# Then navigate to the folder in terminal
```

### Step 3: Setup Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 4: Install Python Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Key packages installed:
# - fastapi (API framework)
# - uvicorn (API server)
# - pandas, numpy (data processing)
# - scikit-learn (ML algorithms)
# - xgboost (gradient boosting)
# - shap (model explanations)
# - joblib (model serialization)
```

### Step 5: Install Node.js Dependencies

```bash
# Navigate to frontend folder
cd startup-predictor

# Install npm packages
npm install

# This installs:
# - next (React framework)
# - react (UI library)
# - tailwindcss (styling)
# - lucide-react (icons)
```

### Step 6: Verify Models Are Ready

```bash
# Check if trained models exist
# Should see 8 files in results/models/:
# - xgboost_best.pkl
# - logistic_regression_best.pkl
# - svm_rbf_best.pkl
# - xgboost_explainer.pkl
# - logistic_explainer.pkl
# - svm_explainer.pkl
# - preprocessor.pkl
# - feature_columns.pkl
```

---

## 🖥️ How to Run

### Method 1: Run Both Services in Separate Terminals (Recommended)

**Terminal 1 - Backend API:**
```bash
cd e:\ML-Startup-Success-Prediction
python -m uvicorn app.app:app --host localhost --port 8000
```

Expected output:
```
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:app.app:Loading for models in: ...
INFO:app.app:All models and preprocessor loaded successfully!
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd e:\ML-Startup-Success-Prediction\startup-predictor
npm run dev
```

Expected output:
```
▲ Next.js 15.4.5
  - Local:        http://localhost:3000
  - Network:      http://10.191.213.129:3000
✓ Ready in 1867ms
```

**Then Open Browser:**
```
http://localhost:3000
```

### Method 2: Using npm concurrently (Advanced)

Install globally:
```bash
npm install -g concurrently
```

Then:
```bash
cd e:\ML-Startup-Success-Prediction
concurrently "python -m uvicorn app.app:app --port 8000" "cd startup-predictor && npm run dev"
```

---

## 📱 Using the Application

### Step-by-Step Guide

#### 1. **Access the Web Interface**
- Open browser: `http://localhost:3000`
- You should see a form titled "Startup Success Predictor"

#### 2. **Fill in Startup Information**

**Region Selection:**
- Click "Select Region" dropdown
- Choose from: Northern America, Western Europe, Eastern Asia, Southern Asia, Other
- Type to search if needed

**City Selection:**
- Click "Select City" dropdown
- Choose from: San Francisco, New York, Boston, Austin, Seattle, Chicago, Los Angeles, Denver, Atlanta, Other

**Industry Category:**
- Click "Select Category" dropdown
- Choose from 25 industries:
  - Software, Mobile, Web, E-commerce
  - Biotechnology, Health, Medical
  - Enterprise, Analytics, Data
  - Games, Entertainment, Media
  - Advertising, Marketing
  - And more...

**Founded Year:**
- Enter year between 1995 and 2015
- Example: 2010

**Other Details (Optional):**
- Funding amount
- Number of funding rounds
- Other startup metrics

#### 3. **Click "Predict" Button**

The application will:
1. Send data to API endpoint
2. Preprocess features
3. Run 3 ML models
4. Calculate predictions
5. Generate SHAP explanations
6. Display results

#### 4. **View Results**

You'll see:

**Success Probability:**
- Overall prediction: X% chance of acquisition

**Model Predictions:**
```
XGBoost:          75% confidence
Logistic Regression: 62% confidence
SVM:              58% confidence
```

**Feature Importance:**
- Top factors influencing prediction
- SHAP values showing impact direction

**Explanation:**
- Why the model made this prediction
- Which features matter most
- Model explainability scores

---

## 📊 Technology Stack

### Frontend
- **Framework**: Next.js 15.4.5 (React 19)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **State Management**: React Hooks
- **HTTP Client**: Built-in fetch API

### Backend
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Language**: Python 3.14
- **Validation**: Pydantic
- **CORS**: Enabled for frontend communication

### Machine Learning
- **Algorithms**: 
  - XGBoost (Gradient Boosting)
  - Logistic Regression (Linear)
  - SVM (Support Vector Machines)
- **Feature Engineering**: Scikit-learn, Pandas
- **Explainability**: SHAP (SHapley Additive exPlanations)
- **Data Processing**: NumPy, Pandas

### Data & Storage
- **Training Data**: 5,000 startup records (CSV)
- **Model Serialization**: Joblib (pickle format)
- **Feature Engineering**: Preprocessing pipeline (SavedStartupDataProcessor)

---

## 🏗️ Project Structure

```
ML-Startup-Success-Prediction/
│
├── 📄 README.md                          # This file - Complete guide
├── 📄 requirements.txt                   # Python dependencies
├── 📄 .gitignore                         # Git ignore rules
│
├── 📁 app/
│   └── app.py                            # FastAPI backend main file
│                                         # - Endpoints: /predict, /predict_with_explanation
│                                         # - Health checks and dropdown data
│
├── 📁 startup-predictor/                 # Next.js Frontend Project
│   ├── package.json                      # npm dependencies
│   ├── next.config.ts                    # Next.js configuration
│   ├── tsconfig.json                     # TypeScript configuration
│   ├── tailwind.config.ts                # Tailwind CSS configuration
│   │
│   ├── 📁 app/
│   │   ├── page.tsx                      # Main prediction interface
│   │   ├── layout.tsx                    # App layout wrapper
│   │   ├── globals.css                   # Global styles
│   │   └── 📁 about/
│   │       └── page.tsx                  # About page
│   │
│   ├── 📁 public/                        # Static assets
│   └── 📁 styles/
│       └── app.css                       # App-specific styles
│
├── 📁 src/
│   ├── data_preprocessing.py             # Feature engineering pipeline
│   │                                     # - StartupDataProcessor class
│   │                                     # - Handles all data transformations
│   ├── data_utils.py                     # Utility functions
│   └── README.md                         # Backend documentation
│
├── 📁 data/
│   ├── README.md                         # Data documentation
│   ├── 📁 raw/
│   │   └── startups_data.csv            # Training data (5,000 records)
│   └── 📁 processed/
│       ├── unique_regions.csv           # Available regions
│       └── unique_cities.csv            # Available cities
│
├── 📁 results/
│   ├── 📁 models/                        # Trained ML models
│   │   ├── xgboost_best.pkl             # XGBoost model (80.5% accuracy)
│   │   ├── logistic_regression_best.pkl # Logistic Regression (48.7%)
│   │   ├── svm_rbf_best.pkl             # SVM model (46.3%)
│   │   ├── xgboost_explainer.pkl        # XGBoost SHAP explainer
│   │   ├── logistic_explainer.pkl       # LR SHAP explainer
│   │   ├── svm_explainer.pkl            # SVM SHAP explainer
│   │   ├── preprocessor.pkl             # Feature preprocessor
│   │   └── feature_columns.pkl          # Feature names/order
│   │
│   └── 📁 figures/                       # Analysis visualizations
│       ├── model_performance_dashboard.html
│       ├── comprehensive_performance_plots.html
│       └── business_impact_analysis.html
│
└── 📁 notebooks/                         # Jupyter analysis notebooks
    ├── 01_data_exploration.ipynb        # EDA analysis
    ├── 02_data_preprocessing_feature_engineering.ipynb
    ├── 03_modeling.ipynb                # Model training
    ├── 04_evaluation.ipynb              # Model evaluation
    ├── 05_pipeline_setup.ipynb          # Production setup
    └── README.md                         # Notebooks guide
```

---

## 🤖 Machine Learning Models

### Model Comparison

| Model | Accuracy | Use Case |
|-------|----------|----------|
| **XGBoost** | **80.5%** | Best overall - Ensemble method with high accuracy |
| **Logistic Regression** | 48.7% | Baseline - Interpretable linear model |
| **SVM (RBF)** | 46.3% | Non-linear boundaries - Complex patterns |

### Features Used (22 Total)

**Geographic Features (3):**
- `region_startup_density` - Startup concentration by region (1-5 scale)
- `city_startup_density` - City-level startup density (1-5 scale)
- `is_usa` - Binary flag for USA-based companies

**Industry Features (15):**
- `category_software` - Software industry
- `category_mobile` - Mobile/apps
- `category_social` - Social platforms
- `category_web` - Web services
- `category_e-commerce` - E-commerce
- `category_biotechnology` - Biotech
- `category_health` - Healthcare
- `category_enterprise` - Enterprise software
- `category_advertising` - Ad tech
- `category_games` - Gaming
- `category_technology` - Tech
- `category_marketing` - Marketing tech
- `category_analytics` - Data/Analytics
- And more... (all binary: 0 or 1)

**Temporal Features (4):**
- `founded_year_std` - Standardized founding year
- `era_dotcom_era` - Founded 1995-2000 (binary)
- `era_post_crash` - Founded 2001-2008 (binary)
- `era_recovery` - Founded 2009-2015 (binary)

### Training Data

- **Records**: 5,000 startup companies
- **Class Distribution**: 
  - Acquired: 10.9% (546 startups)
  - Not Acquired: 89.1% (4,454 startups)
- **Feature Engineering**: Automated pipeline handles:
  - Categorical encoding (industry categories)
  - Standardization (founding year)
  - Density calculations (geographic clusters)
  - Missing value imputation
  - Era-based classification

---

## 📈 API Endpoints

### Prediction Endpoints

**1. POST /predict**
```bash
# Get startup acquisition probability

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "country_code": "USA",
    "region": "Northern America",
    "city": "San Francisco",
    "category_code": "software",
    "founded_year": 2010
  }'

# Response:
{
  "success_probability": 0.42,
  "xgboost_probability": 0.75,
  "logistic_probability": 0.62,
  "svm_probability": 0.58,
  "prediction": "Moderate chance of acquisition"
}
```

**2. POST /predict_with_explanation**
```bash
# Get predictions + SHAP explanations

curl -X POST http://localhost:8000/predict_with_explanation \
  -H "Content-Type: application/json" \
  -d '{...same as above...}'

# Response:
{
  "predictions": {...},
  "shap_values": [
    {
      "feature": "region_startup_density",
      "xgboost_impact": 0.15,
      "logistic_impact": 0.08,
      "svm_impact": 0.05
    },
    ...
  ]
}
```

### Data Endpoints

**3. GET /regions**
```bash
# Get available regions
curl http://localhost:8000/regions

# Response:
{
  "regions": [
    "Northern America",
    "Western Europe",
    "Eastern Asia",
    "Southern Asia",
    "Other"
  ]
}
```

**4. GET /cities**
```bash
# Get available cities
curl http://localhost:8000/cities
```

**5. GET /categories**
```bash
# Get available industry categories
curl http://localhost:8000/categories
```

**6. GET /health**
```bash
# Health check
curl http://localhost:8000/health

# Response:
{
  "status": "healthy",
  "models_loaded": true,
  "timestamp": "2026-01-20T..."
}
```

### API Documentation

**Interactive Swagger UI:**
```
http://localhost:8000/docs
```

Open this in browser to test all endpoints interactively!

---

## 🔍 Features & Methodology

### Feature Engineering Pipeline

The application automatically transforms raw startup data:

```python
1. Raw Input
   ├── country_code, region, city
   ├── category_code (industry)
   └── founded_year

2. Geographic Encoding
   ├── Calculate region density tiers (1-5)
   ├── Calculate city density tiers (1-5)
   └── Create USA binary flag

3. Industry Encoding
   ├── Standardize category names
   ├── Create binary flags for top 15 categories
   └── Handle multi-category startups

4. Temporal Engineering
   ├── Standardize founding year (z-score)
   ├── Assign economic era (dot-com/post-crash/recovery)
   └── Create era binary flags

5. Final Features (22 total)
   └── Ready for ML models!
```

### Model Training Process

```
1. Load 5,000 startup records
   ↓
2. Engineer 22 features from raw data
   ↓
3. Handle class imbalance with SMOTE
   ├── Original: 89% negative, 11% positive
   └── After SMOTE: 50% negative, 50% positive
   ↓
4. Train 3 models
   ├── XGBoost (Gradient Boosting)
   ├── Logistic Regression (Linear)
   └── SVM RBF (Non-linear)
   ↓
5. Generate SHAP explainers
   ├── TreeExplainer (XGBoost)
   └── KernelExplainer (LR & SVM)
   ↓
6. Save everything for production
   ├── Model files (.pkl)
   ├── Preprocessor
   └── Feature metadata
```

### SHAP Explainability

**What is SHAP?**
- Explains individual predictions
- Shows which features matter most
- Provides direction (increases/decreases probability)

**How we use it:**
1. Each prediction includes SHAP values
2. Top 5 most important features displayed
3. Feature impact visualization
4. Model transparency for stakeholders

---

## 📚 Learn More

### Understand the Code

**Frontend (React/Next.js):**
- Open `startup-predictor/app/page.tsx`
- See form components, API calls, result display

**Backend (FastAPI):**
- Open `app/app.py`
- See endpoints, model loading, prediction logic

**Feature Engineering:**
- Open `src/data_preprocessing.py`
- See StartupDataProcessor class
- Understand transformations

### Run Individual Notebooks

```bash
# Each notebook can be run independently
# They contain explanations and visualizations

1. jupyter notebook notebooks/01_data_exploration.ipynb
2. jupyter notebook notebooks/02_data_preprocessing_feature_engineering.ipynb
3. jupyter notebook notebooks/03_modeling.ipynb
4. jupyter notebook notebooks/04_evaluation.ipynb
5. jupyter notebook notebooks/05_pipeline_setup.ipynb
```

### Modify & Extend

**Add new cities/regions:**
1. Update CSV files in `data/processed/`
2. Restart backend

**Retrain models:**
1. Add new data to `data/raw/startups_data.csv`
2. Run `python train_models.py`
3. Models automatically update

**Change UI:**
1. Edit `startup-predictor/app/page.tsx`
2. Changes auto-reload in dev mode

---

## 🤝 Contributing

### For Students

This project is perfect for learning:
- ✅ Full-stack machine learning development
- ✅ Feature engineering and preprocessing
- ✅ Model comparison and evaluation
- ✅ API design with FastAPI
- ✅ Frontend development with React/Next.js
- ✅ Model explainability with SHAP
- ✅ Deployment and production practices

**Suggested Learning Path:**
1. Run the application (today!)
2. Make a prediction and understand results
3. Read the code in `app/app.py` (API logic)
4. Read `src/data_preprocessing.py` (features)
5. Explore `startup-predictor/app/page.tsx` (frontend)
6. Run notebooks for detailed analysis
7. Modify and extend the application

### Make Improvements

**Ideas for extensions:**
- [ ] Add more training data
- [ ] Add new ML models (Random Forest, Neural Network)
- [ ] Improve UI with more visualizations
- [ ] Add prediction confidence intervals
- [ ] Create comparison tool (vs other startups)
- [ ] Add export to PDF functionality
- [ ] Create admin dashboard for model monitoring
- [ ] Implement user authentication
- [ ] Add historical predictions tracking

---

## ⚠️ Troubleshooting

### Frontend shows "Cannot reach server"
```bash
# Check if backend is running
curl http://localhost:8000/health

# If not, restart:
python -m uvicorn app.app:app --host localhost --port 8000
```

### Models not loading
```bash
# Check if model files exist
ls results/models/

# Should see 8 .pkl files
# If missing, run:
python train_models.py
```

### Port already in use
```bash
# Find process using port 3000 or 8000
netstat -ano | findstr :3000

# Kill the process
taskkill /PID [PID_NUMBER] /F

# Then restart services
```

### Dependencies not installing
```bash
# Make sure virtual environment is activated
# For Windows:
venv\Scripts\activate

# Then retry:
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💼 Author

**Created for Educational Purposes**
- Updated: January 20, 2026
- Purpose: Teaching machine learning end-to-end development
- Target Audience: Students learning ML, web development, and data science

---

## 🙏 Acknowledgments

- **Academic Foundation**: Żbikowski & Antosiuk (2021) - "Predicting company bankruptcy on the basis of narrative reports"
- **Technologies**: FastAPI, Next.js, XGBoost, SHAP
- **Data Source**: Crunchbase startup database
- **Inspiration**: Building practical ML applications for real-world problems

---

## 🎓 What You've Learned by Using This Project

✅ How to run a full-stack ML application
✅ What features are important for startup success
✅ How different ML models make different predictions
✅ Why explainability (SHAP) matters in ML
✅ How to build APIs with FastAPI
✅ How to create modern UIs with React/Next.js
✅ Best practices in ML pipeline development
✅ Production-ready code structure

---

**Happy Learning! 🚀**

*Questions? Errors? Suggestions?*
- Check the troubleshooting section above
- Review individual README files in subdirectories
- Examine the Jupyter notebooks for detailed explanations
- Read the code comments in key files
- Ask in the comments/issues section

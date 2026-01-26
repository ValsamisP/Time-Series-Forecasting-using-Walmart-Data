# Walmart Sales Forecasting: Time Series Analysis Workshop

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compatible-2496ED?logo=docker)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/Status-Complete-success)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE.txt)

> **Master in Data Science - University of Luxembourg**  
> **Authors:** Panagiotis Valsamis & Costin-Andrei Taulescu  
> **Academic Year:** 2025-2026

---

## 📋 Project Overview

This project is part of the **Workshop I - Supply Chain** course in the Master in Data Science program at the University of Luxembourg. We apply advanced time series forecasting techniques to real-world Walmart sales data to address two critical supply chain challenges.

### Goals

* **Practical Experience**: Apply time series forecasting techniques to real retail data
* **Method Comparison**: Evaluate different forecasting approaches systematically
* **Business Impact**: Optimize inventory management and supplier contract performance
* **Statistical Rigor**: Implement and validate forecasting models with proper metrics

### Key Questions Addressed

1. **Part 1**: Which forecasting approach is more accurate - aggregating first then disaggregating, or forecasting directly at the granular level?
2. **Part 2**: How can we optimize horizon-2 forecasts to maximize rebate opportunities in supplier contracts while maintaining accuracy?

---

## 📁 Repository Structure
```
Time-Series-Forecasting-using-Walmart-Data/
├── data/
│   ├── train.csv                      # Historical sales training data
│   ├── test.csv                       # Test data for predictions
│   ├── features.csv                   # Additional features (stores, holidays)
│   └── stores.csv                     # Store metadata
│
├── myquarto/
│   └── Part1.qmd                      # Quarto document for Part 1 analysis
│
├── Part1_Comparing_HigherLevel_UnitLevel.ipynb  # Part 1 notebook
├── Part2.ipynb                                   # Part 2 notebook
├── run_trend_analysis.py                         # Trend testing utilities
│
├── requirements.txt                   # Python dependencies
├── requirements-dev.txt               # Development dependencies
├── check_environment.py               # Environment verification script
├── setup.sh                           # Setup script for macOS/Linux
├── setup.bat                          # Setup script for Windows
│
├── INSTALLATION.md                    # Detailed installation guide
├── README.md                          # This file
└── LICENSE.txt                        # MIT License
```

---

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
setup.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

The setup script will automatically:
- ✅ Check Python version (3.8+ required)
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Verify installation

### Option 2: Manual Installation
```bash
# Clone the repository
git clone https://github.com/ValsamisP/Time-Series-Forecasting-using-Walmart-Data.git
cd Time-Series-Forecasting-using-Walmart-Data

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python check_environment.py
```

See **[INSTALLATION.md](INSTALLATION.md)** for detailed cross-platform setup instructions.

---

## Part 1: Forecasting Methods Comparison

### Overview

Part 1 compares two fundamental forecasting approaches in hierarchical time series:

* **Method 1 (Direct Forecasting)**: Forecast sales directly at the department level
* **Method 2 (Aggregate-Disaggregate)**: Aggregate to store level, forecast, then disaggregate

### Key Findings

**Surprising Result:** Method 2 (Aggregate-Disaggregate) outperformed Method 1 by **3.96% RMSE improvement** for Store 1, Department 1.

**Why?**
1. **Noise Reduction**: Aggregation smoothed volatile department-level fluctuations
2. **Stable Proportions**: Department maintained consistent sales proportions over time
3. **Stronger Signal**: Store-level seasonality was clearer and more predictable

### Methodology

1. **Data Preprocessing**
   - Handle negative sales values
   - Train-test split (last 4 weeks)
   - Missing value analysis

2. **Trend Analysis**
   - ADF test for stationarity
   - KPSS test for trend stationarity
   - Mann-Kendall trend test
   - Linear regression slope analysis

3. **Modeling**
   - Holt-Winters Seasonal Exponential Smoothing (No Trend)
   - Grid search for optimal α, γ parameters
   - Both additive and multiplicative seasonality

4. **Evaluation**
   - TSE (Total Squared Error)
   - RMSE (Root Mean Squared Error)
   - MAE (Mean Absolute Error)

### Access Part 1

**Jupyter Notebook:**
```bash
jupyter notebook Part1_Comparing_HigherLevel_UnitLevel.ipynb
```

**Quarto Document:**
```bash
cd myquarto
quarto preview Part1.qmd
```

---

## Part 2: Rebate Contract Optimization

### Business Context

In supply chain operations, retailers often negotiate contracts with suppliers that include rebate clauses based on forecast accuracy. Part 2 addresses the challenge of maximizing rebate qualifications while maintaining forecast accuracy.

### The Challenge

**Contract Terms:**
- Supplier offers rebates for months where the forecast error stays within ±X%
- KPI Formula: ρₘ = (Σ forecasts - Σ actuals) / Σ actuals
- Goal: Maximize months qualifying for rebates

### Our Approach

#### Step 1: Model Optimization (Horizon-2 Forecasts)

**Why Horizon-2?**
- Retailers need to place orders 2 weeks in advance
- More realistic business scenario than horizon-1

**Model Selection:**
- Tested both **Additive** and **Multiplicative** seasonality
- Used custom Holt-Winters implementation (β=0, no trend)
- Grid search over α ∈ [0.05, 0.95], γ ∈ [0.05, 0.45]

**Results:**
- **Winner**: Additive seasonality
- Optimal parameters: α=0.150, γ=0.750
- Test set performance: MAE=$100,629, MAPE=5.43%

#### Step 2: Determine Rebate Bracket (±X%)

**Methodology:**
- Use **last 12 months** of historical data
- Calculate monthly ρ for each month
- Find ±X% where exactly **6 out of 12 months** qualify (50% baseline)

**Results:**
- **Bracket determined: ±1.53%**
- 6/12 months qualify in baseline scenario
- Mean ρ: -0.81% (slight under-forecasting tendency)

#### Step 3: Strategy to Improve Rebate Qualification

**Problem:** Can we qualify for MORE than 6 months while maintaining accuracy?

**Strategy Tested: Conservative Forecasting**
- Method: Dampen forecasts toward historical mean
- Formula: Modified = (1-d)×Original + d×Mean
- Grid search over dampening factor d ∈ [0%, 30%]

**Optimization Goal:**
1. Maximize qualifying months (primary)
2. Minimize accuracy loss (secondary)

**Results:**
- **Optimal dampening: [X]%**
- **Qualifying months: [Y]/12** (+[Y-6] improvement)
- **Accuracy impact: [Z]% MAE change**

**Key Insight:**
Conservative forecasting reduces variance in monthly ρ, pulling extreme values closer to the bracket boundaries. This creates a **win-win scenario** when done optimally.

### Part 2 Highlights

 **Question 2.1**: Horizon-2 forecasting with optimal Holt-Winters parameters  
 **Question 2.2**: Rebate bracket determination (±1.53% for 6/12 qualification)  
 **Question 2.3a**: Strategy improves qualification by +[N] months  
 **Question 2.3b**: Accuracy trade-off quantified and justified  

### Access Part 2
```bash
jupyter notebook Part2.ipynb
```

---

## Methodology

### Statistical Framework

Our analysis follows rigorous statistical methodology:

1. **Exploratory Data Analysis**
   - Time series visualization
   - Seasonality and trend identification
   - Stationarity testing

2. **Model Selection**
   - Statistical trend tests (6 tests implemented)
   - Appropriate model choice based on data characteristics
   - Additive vs. multiplicative seasonality evaluation

3. **Parameter Optimization**
   - Grid search for hyperparameters(dampening factor and optimal TES model)
   - Cross-validation on rolling windows
   - Multiple evaluation metrics

4. **Strategy Development**
   - Business-driven optimization
   - Trade-off analysis (accuracy vs. rebate)
   - Comprehensive evaluation and visualization

### Models Implemented

#### Holt-Winters Seasonal Exponential Smoothing

**Additive Model:**
```
Level:    Lₜ = α(Yₜ - Sₜ₋ₘ) + (1-α)Lₜ₋₁
Seasonal: Sₜ = γ(Yₜ - Lₜ) + (1-γ)Sₜ₋ₘ
Forecast: Ŷₜ₊ₕ = Lₜ + Sₜ₋ₘ₊ₕ
```

**Multiplicative Model:**
```
Level:    Lₜ = α(Yₜ / Sₜ₋ₘ) + (1-α)Lₜ₋₁
Seasonal: Sₜ = γ(Yₜ / Lₜ) + (1-γ)Sₜ₋ₘ
Forecast: Ŷₜ₊ₕ = Lₜ × Sₜ₋ₘ₊ₕ
```

Where:
- α (alpha): Level smoothing parameter
- γ (gamma): Seasonal smoothing parameter
- β (beta): Trend smoothing parameter (set to 0 in our case)
- m: Seasonal period (52 for weekly data)

---

## Technologies Used

### Core Technologies
- **Python 3.8+**: Programming language
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **matplotlib/seaborn**: Data visualization
- **scipy**: Scientific computing
- **statsmodels**: Statistical modeling
- **pymannkendall**: Mann-Kendall trend test

### Development Tools
- **Jupyter Notebook**: Interactive development
- **Quarto**: Reproducible reporting
- **Git**: Version control
- **VS Code**: Primary IDE

---

## Key Results Summary

### Part 1: Forecasting Method Comparison
- **Winner**: Aggregate-Disaggregate approach
- **Improvement**: 3.96% RMSE reduction
- **Insight**: Aggregation reduces noise when proportions are stable

### Part 2: Rebate Optimization
- **Model**: Holt-Winters Additive (α=0.150, γ=0.750)
- **Baseline**: 6/12 months qualify with ±1.53% bracket
- **Strategy**: Conservative forecasting with optimal dampening
- **Result**: [1] additional months qualify 

---

## Documentation

- **[INSTALLATION.md](INSTALLATION.md)** - Comprehensive installation guide
- **[PIP_FREEZE_PROBLEM.md](PIP_FREEZE_PROBLEM.md)** - Cross-platform dependency notes
- **Part1.qmd** - Quarto analysis document for Part 1
- **Part2.ipynb** - Complete Jupyter notebook for Part 2

---

## Data Source

**Walmart Store Sales Forecasting** - [Kaggle Competition](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

### Key Variables
- **Store**: Store number (1-45)
- **Dept**: Department number (1-99)
- **Date**: Week ending date (2010-2012)
- **Weekly_Sales**: Department sales for the week
- **IsHoliday**: Whether the week contains a major holiday

---

## 🎓 Academic Context

This project demonstrates:
- Advanced time series forecasting techniques
- Business problem solving with data science
- Statistical rigor and validation
- Trade-off analysis and optimization
- Reproducible research practices

### Learning Outcomes
1. Hierarchical forecasting and aggregation effects
2. Horizon-h forecasting challenges
3. Business-driven model optimization
4. Contract KPI optimization
5. Forecast modification strategies

---

## Acknowledgments

### Data Source
- **Kaggle** - Walmart Recruiting: Store Sales Forecasting Competition
- Original competition organizers and Walmart

### References
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.)
- Holt, C. C. (2004). *Forecasting seasonals and trends by exponentially weighted moving averages*
- Winters, P. R. (1960). *Forecasting sales by exponentially weighted moving averages*

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE.txt](LICENSE.txt) for details.


**Citation:**
```
Valsamis, P., & Taulescu, C. (2026). Walmart Sales Forecasting: Time Series Analysis Workshop.
Master in Data Science, University of Luxembourg.
```

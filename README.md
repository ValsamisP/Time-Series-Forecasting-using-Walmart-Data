# Walmart Sales Forecasting: Time Series Analysis Workshop

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compatible-2496ED?logo=docker)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE.txt)

> **Master in Data Science - University of Luxembourg**  
> **Authors:** Panagiotis Valsamis & Costin-Andrei Taulescu   
> **Academic Year:** 2025-2026

---

## 📋 Project Overview

This project is part of the **Workshop I - Supply Chain** course in the Master in Data Science program at the University of Luxembourg. The objective is to gain hands-on experience in dealing with, modeling, forecasting, and solving real-world complex time series problems using Walmart sales data from a historical Kaggle competition.

### Goals

-  **Practical Experience**: Apply time series forecasting techniques to real retail data
-  **Method Comparison**: Evaluate different forecasting approaches systematically
-  **Business Impact**: Understand implications for inventory management and supply chain optimization
-  **Statistical Rigor**: Implement and validate forecasting models with proper metrics

### Key Questions Addressed

1. **Part 1**: Which forecasting approach is more accurate - aggregating first then disaggregating, or forecasting directly at the granular level?
2. **Part 2**: How can we maximize forecast accuracy to optimize rebate opportunities in supplier contracts? *(Coming Soon)*

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
├── Part1_Comparing_HigherLevel_UnitLevel.ipynb
├── Part2.ipynb
│
├── requirements.txt                   # Python dependencies
├── requirements-dev.txt               # Development dependencies
├── check_environment.py               # Environment verification script
├── setup.sh                           # Setup script for macOS/Linux
├── setup.bat                          # Setup script for Windows
├── .gitattributes                     # Git line ending configuration
│
├── INSTALLATION.md                    # Detailed installation guide
├── README.md                          # This file
└── .gitignore                         # Git ignore rules
```

---

##  Quick Start

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

See **[INSTALLATION.md](INSTALLATION.md)** for detailed cross-platform setup instructions.

### Option 3: Docker (Coming Soon)

```bash
docker-compose up
```

Access Jupyter at `http://localhost:8888`

---

##  Installation & Setup

### Prerequisites

- **Python 3.8+** installed on your system
- **Git** for version control
- **Quarto CLI** (optional, for rendering Quarto documents) - [Install Quarto](https://quarto.org/docs/get-started/)

### Quick Install

```bash
# Clone the repository
git clone https://github.com/ValsamisP/Time-Series-Forecasting-using-Walmart-Data.git
cd Time-Series-Forecasting-using-Walmart-Data

# Run automated setup
# Windows: setup.bat
# macOS/Linux: ./setup.sh

# Verify installation
python check_environment.py
```

### Manual Setup

**Step 1: Create Virtual Environment**

Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 2: Install Dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Step 3: Verify Installation**

```bash
python check_environment.py
```

You should see:
```
✅ All checks passed!
🎉 Environment is fully set up and ready!
```

### Troubleshooting

If you encounter installation issues, see **[INSTALLATION.md](INSTALLATION.md)** for:
- Platform-specific troubleshooting
- Common error solutions
- Build tool requirements
- Detailed step-by-step instructions

---

##  Part 1: Forecasting Methods Comparison

### Overview

Part 1 compares two fundamental forecasting approaches in time series analysis:

- **Method 1 (Direct Forecasting)**: Forecast sales directly at the department level
- **Method 2 (Aggregate-Disaggregate)**: Aggregate sales to store level, forecast, then disaggregate back to departments

### Hypothesis

We hypothesize that **Method 1** would outperform **Method 2** because:
- It captures department-specific patterns
- Avoids loss of granular information through aggregation
- Can model unique seasonal behaviors per department

### Key Findings

**Surprising Result:** Method 2 (Aggregate-Disaggregate) outperformed Method 1 by **3.96% RMSE improvement** for Store 1, Department 1.

**Why?**
1. **Noise Reduction**: Aggregation smoothed out volatile department-level fluctuations
2. **Stable Proportions**: Department 1 maintained consistent sales proportions
3. **Stronger Signal**: Store-level seasonality was clearer and more predictable

### Methodology

1. **Data Preprocessing**
   - Handle negative sales values
   - Train-test split (last 4 weeks as test set)
   - Check for missing values

2. **Trend Analysis**
   - Augmented Dickey-Fuller (ADF) test
   - KPSS test for trend stationarity
   - Mann-Kendall trend test
   - Linear regression slope analysis

3. **Modeling**
   - Holt-Winters Seasonal Exponential Smoothing (No Trend)
   - Grid search for optimal parameters (α, γ)
   - Both additive and multiplicative seasonality tested

4. **Evaluation Metrics**
   - **TSE (Total Squared Error)**: Overall model fit
   - **RMSE (Root Mean Squared Error)**: Standard forecasting metric
   - **MAE (Mean Absolute Error)**: Robust error measure

### Access Part 1

**Quarto Document:**
```bash
cd myquarto
quarto preview Part1.qmd
```

**Jupyter Notebook:**
```bash
jupyter notebook Part1_Comparing_HigherLevel_UnitLevel.ipynb
```

---

##  Part 2: Coming Soon

Part 2 will focus on **maximizing forecast accuracy** to optimize rebate opportunities in supplier contracts. Stay tuned!

**Expected Topics:**
- Advanced forecasting models (ARIMA, Prophet, LSTM)
- Incorporating external variables (holidays, promotions, economic indicators)
- Multi-step ahead forecasting
- Probabilistic forecasting and uncertainty quantification
- Business optimization and decision-making framework

---

## Data 

### Source

Walmart Store Sales Forecasting - [Kaggle Competition](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

**Note:** Only `train.csv` is used for Part 1 analysis.

### Key Variables Used

- **Store**: Store number (1-45)
- **Dept**: Department number (1-99)
- **Date**: Week ending date (2010-2012)
- **Weekly_Sales**: Sales for the department in the given week

---

## Methodology

### Statistical Framework

Our analysis follows a rigorous statistical approach:

1. **Exploratory Data Analysis (EDA)**
   - Visualize time series patterns
   - Identify seasonality, trend, and outliers
   - Check for stationarity

2. **Model Selection**
   - Test for trend presence (multiple statistical tests)
   - Choose appropriate model (Holt-Winters, ARIMA, etc.)
   - Consider additive vs. multiplicative seasonality

3. **Parameter Optimization**
   - Grid search for hyperparameters
   - Minimize in-sample error (TSE)
   - Validate on hold-out test set

4. **Evaluation & Comparison**
   - Multiple metrics (TSE, RMSE, MAE)
   - Visualize forecasts vs. actuals
   - Statistical significance testing

### Models Implemented

#### Holt-Winters Seasonal Exponential Smoothing

**Additive Model:**
```
Level: L_t = α(Y_t - S_{t-m}) + (1-α)L_{t-1}
Seasonal: S_t = γ(Y_t - L_t) + (1-γ)S_{t-m}
Forecast: Ŷ_{t+h} = L_t + S_{t-m+h}
```

**Multiplicative Model:**
```
Level: L_t = α(Y_t / S_{t-m}) + (1-α)L_{t-1}
Seasonal: S_t = γ(Y_t / L_t) + (1-γ)S_{t-m}
Forecast: Ŷ_{t+h} = L_t × S_{t-m+h}
```

Where:
- α (alpha): Level smoothing parameter
- γ (gamma): Seasonal smoothing parameter
- m: Seasonal period (52 for weekly data)

---

##  Part 1 Summary

**Winner:** Method 2 (Aggregate-Disaggregate)

### Key Insights

1. **Aggregation Benefits**: When department proportions are stable, aggregation reduces noise
2. **Granularity Trade-off**: Not all problems benefit from maximum granularity
3. **Context Matters**: Department characteristics determine optimal approach

---

## Technologies Used

### Core Technologies
- **Python 3.8+**: Programming language
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **statsmodels**: Statistical modeling and time series analysis
- **matplotlib/seaborn**: Data visualization
- **scipy**: Scientific computing
- **pymannkendall**: Mann-Kendall trend test

### Additional Tools
- **Jupyter Notebook**: Interactive development
- **Quarto**: Reproducible reporting
- **Git**: Version control
- **VS Code**: Primary IDE

---

## How to Run

### Option 1: Jupyter Notebook

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Launch Jupyter
jupyter notebook

# Navigate to:
# Part1_Comparing_HigherLevel_UnitLevel.ipynb
```

### Option 2: Quarto Document

```bash
# Navigate to myquarto directory
cd myquarto

# Preview (live reload)
quarto preview Part1.qmd

# Or render to HTML
quarto render Part1.qmd

# Or render to PDF
quarto render Part1.qmd --to pdf
```

---

## 📚 Documentation

- **[INSTALLATION.md](INSTALLATION.md)** - Comprehensive installation guide for all platforms
- **[PIP_FREEZE_PROBLEM.md](PIP_FREEZE_PROBLEM.md)** - Understanding cross-platform dependency issues

---

## Acknowledgments

### Data Source

- **Kaggle** - Walmart Recruiting: Store Sales Forecasting Competition
- Original competition organizers and Walmart for providing the dataset

### References

- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.)
- Holt, C. C. (2004). *Forecasting seasonals and trends by exponentially weighted moving averages*
- Winters, P. R. (1960). *Forecasting sales by exponentially weighted moving averages*

---

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

### Academic Use

This project is submitted as part of academic coursework. Please respect academic integrity guidelines if referencing this work.

**Citation:**
```
Valsamis, P., & Taulescu, C. (2026). Walmart Sales Forecasting: Time Series Analysis Workshop.
Master in Data Science, University of Luxembourg.
```

---

## Authors

**Panagiotis Valsamis**  
Master in Data Science, University of Luxembourg

**Costin-Andrei Taulescu**  
Master in Data Science, University of Luxembourg

---

## Issues & Contributing

If you encounter any issues or have suggestions:

1. Check **[INSTALLATION.md](INSTALLATION.md)** for troubleshooting
2. Run `python check_environment.py` to diagnose problems
3. Create an issue on GitHub with:
   - Your OS and Python version
   - Full error message
   - Output of the environment check

---

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 500MB for dependencies + data files
- **OS**: Windows 10+, macOS 10.14+, or modern Linux distribution

---

## Cross-Platform Compatibility

This project is fully compatible with:
- ✅ Windows 10/11
- ✅ macOS 10.14+
- ✅ Ubuntu 20.04+
- ✅ Debian 10+
- ✅ Fedora 34+

All dependencies are tested across platforms. See **[INSTALLATION.md](INSTALLATION.md)** for platform-specific notes.
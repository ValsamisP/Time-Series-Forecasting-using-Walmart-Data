# Walmart Sales Forecasting: Time Series Analysis Workshop

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE.txt)

> **Master in Data Science - University of Luxembourg**  
> **Authors:** Panagiotis Valsamis & Costin-Andrei Taulescu   
> **Academic Year:** 2025-2026

---


##  Project Overview

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

##  Repository Structure

```


 Project/
├── data/
│   ├── train.csv                      # Historical sales training data
│   ├── test.csv                       # Test data for predictions
│   ├── features.csv                   # Additional features (stores, holidays)
│   └── stores.csv                     # Store metadata
│
├── quarto/
│   └── Part1.qmd                      # Quarto document for Part 1 analysis
│
│
├── Part1_Comparing_HigherLevel_UnitLevel.ipynb  # Jupyter notebook version
│
│
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── .gitignore                         # Git ignore rules

```

---

##  Installation & Setup

### Prerequisites

- **Python 3.8+** installed on your system
- **Quarto CLI** (optional, for rendering Quarto documents) - [Install Quarto](https://quarto.org/docs/get-started/)
- **Git** for version control

### Step 1: Clone the Repository

```bash
git clone https://github.com/ValsamisP/Time-Series-Forecasting-using-Walmart-Data.git
cd walmart-forecasting/Project
```

### Step 2: Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Installation

```python
python -c "import pandas; import numpy; import matplotlib; print('✓ All packages installed successfully!')"
```

### Step 5: Install Quarto (Optional)

If you want to render the Quarto documents:

**Windows:**
- Download from [quarto.org](https://quarto.org/docs/get-started/)
- Run the installer

**macOS:**
```bash
brew install quarto
```

**Linux:**
```bash
# Download from https://quarto.org/docs/download/
sudo dpkg -i quarto-*.deb
```

Verify installation:
```bash
quarto --version
```

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
jupyter notebook notebooks/Part1_Comparing_HigherLevel_UnitLevel.ipynb
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

##  Data Description

### Source

Walmart Store Sales Forecasting - [Kaggle Competition](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

### Files

| File | Description | Size |
|------|-------------|------|
| `train.csv` | Historical weekly sales data | 421,570 rows |
| `test.csv` | Test set for predictions | 115,064 rows |
| `features.csv` | Store, department, regional info | Multiple tables |
| `stores.csv` | Store type and size metadata | 45 stores |

**Note:** Only `train.csv` is used for Part 1 analysis.

### Key Variables Used

- **Store**: Store number (1-45)
- **Dept**: Department number (1-99)
- **Date**: Week ending date (2010-2012)
- **Weekly_Sales**: Sales for the department in the given week


##  Methodology

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


### Part 1 Summary

**Winner:** Method 2 (Aggregate-Disaggregate)

### Key Insights

1. **Aggregation Benefits**: When department proportions are stable, aggregation reduces noise
2. **Granularity Trade-off**: Not all problems benefit from maximum granularity
3. **Context Matters**: Department characteristics determine optimal approach


---

##  Technologies Used


### Additional Tools

- **Jupyter Notebook**: Interactive development
- **Quarto**: Reproducible reporting
- **Git**: Version control
- **VS Code**: Primary IDE

---

##  How to Run

### Option 1: Jupyter Notebook

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Launch Jupyter
jupyter notebook

# Navigate to:
# notebooks/Part1_Comparing_HigherLevel_UnitLevel.ipynb
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

### Data Source

- **Kaggle** - Walmart Recruiting: Store Sales Forecasting Competition
- Original competition organizers and Walmart for providing the dataset

### References

- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.)
- Holt, C. C. (2004). *Forecasting seasonals and trends by exponentially weighted moving averages*
- Winters, P. R. (1960). *Forecasting sales by exponentially weighted moving averages*


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

### Academic Use

This project is submitted as part of academic coursework. Please respect academic integrity guidelines if referencing this work.

**Citation:**
```
Valsamis, P., & Taulescu, C. (2026). Walmart Sales Forecasting: Time Series Analysis Workshop.
Master in Data Science, University of Luxembourg.
```

---


### Authors

**Panagiotis Valsamis**

**Costin-Andrei Taulescu**




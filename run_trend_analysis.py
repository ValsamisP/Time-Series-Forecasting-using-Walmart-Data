
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller, kpss
import warnings
warnings.filterwarnings('ignore')
import pymannkendall as mk

def mann_kendall_test(data):
    """Mann-Kendall test for monotonic trend"""
    print("\n" + "="*70)
    print("1. MANN-KENDALL TEST (Non-parametric)")
    print("="*70)
    
    
    result = mk.original_test(data)
    
    print(f"Trend: {result.trend}")
    print(f"Test Statistic (S): {result.s}")
    print(f"p-value: {result.p:.6f}")
    print(f"Tau (correlation): {result.Tau:.6f}")
    print(f"z-score: {result.z:.6f}")
    
    if result.p < 0.05:
        print(f"\n RESULT: Significant trend detected (p < 0.05)")
        print(f"  Direction: {result.trend}")
    else:
        print(f"\n RESULT: No significant trend (p >= 0.05)")
    
    return result

def adf_test(data):
    """Augmented Dickey-Fuller test for stationarity"""
    print("\n" + "="*70)
    print("2. AUGMENTED DICKEY-FULLER (ADF) TEST")
    print("="*70)
    
    result = adfuller(data, autolag='AIC')
    
    print(f"ADF Statistic: {result[0]:.6f}")
    print(f"p-value: {result[1]:.6f}")
    print(f"Lags used: {result[2]}")
    print(f"Number of observations: {result[3]}")
    print("\nCritical Values:")
    for key, value in result[4].items():
        print(f"  {key}: {value:.3f}")
    
    if result[1] < 0.05:
        print(f"\n RESULT: Series is stationary (p < 0.05)")
        print(f"   No unit root → Suggests NO trend")
    else:
        print(f"\n RESULT: Series is non-stationary (p >= 0.05)")
        print(f"   Unit root present → May have trend")
    
    return result

def kpss_test(data):
    """KPSS test for stationarity"""
    print("\n" + "="*70)
    print("3. KPSS TEST (Kwiatkowski-Phillips-Schmidt-Shin)")
    print("="*70)
    
    result_trend = kpss(data, regression='ct', nlags='auto')
    
    print("KPSS Test (with trend):")
    print(f"KPSS Statistic: {result_trend[0]:.6f}")
    print(f"p-value: {result_trend[1]:.6f}")
    print(f"Lags used: {result_trend[2]}")
    print("\nCritical Values:")
    for key, value in result_trend[3].items():
        print(f"  {key}: {value:.3f}")
    
    if result_trend[1] >= 0.05:
        print(f"\n RESULT: Series is trend stationary (p >= 0.05)")
        print(f"   Null hypothesis not rejected → NO significant trend")
    else:
        print(f"\n RESULT: Series is not trend stationary (p < 0.05)")
        print(f"   Trend component present")
    
    return result_trend

def linear_regression_test(data):
    """Linear regression test for trend"""
    print("\n" + "="*70)
    print("4. LINEAR REGRESSION TEST")
    print("="*70)
    
    time = np.arange(len(data))
    slope, intercept, r_value, p_value, std_err = stats.linregress(time, data)
    
    print(f"Slope: {slope:.6f}")
    print(f"Intercept: {intercept:.2f}")
    print(f"R-squared: {r_value**2:.6f}")
    print(f"p-value: {p_value:.6f}")
    print(f"Standard Error: {std_err:.6f}")
    
    confidence = 0.95
    dof = len(data) - 2
    t_val = stats.t.ppf((1 + confidence) / 2, dof)
    ci_lower = slope - t_val * std_err
    ci_upper = slope + t_val * std_err
    
    print(f"\n95% Confidence Interval for slope: [{ci_lower:.6f}, {ci_upper:.6f}]")
    
    if p_value < 0.05:
        if slope > 0:
            print(f"\n RESULT: Significant positive linear trend (p < 0.05)")
        else:
            print(f"\n RESULT: Significant negative linear trend (p < 0.05)")
    else:
        print(f"\n RESULT: No significant linear trend (p >= 0.05)")
    
    return {'slope': slope, 'intercept': intercept, 'p_value': p_value, 
            'r_squared': r_value**2, 'std_err': std_err}

def cox_stuart_test(data):
    """Cox-Stuart test for trend"""
    print("\n" + "="*70)
    print("5. COX-STUART TEST (Non-parametric)")
    print("="*70)
    
    n = len(data)
    c = n // 2
    
    if n % 2 == 1:
        first_half = data[:c]
        second_half = data[c+1:]
    else:
        first_half = data[:c]
        second_half = data[c:]
    
    plus_signs = sum(second_half > first_half)
    minus_signs = sum(second_half < first_half)
    ties = sum(second_half == first_half)
    
    n_comparisons = plus_signs + minus_signs
    p_value = 2 * min(stats.binom.cdf(min(plus_signs, minus_signs), n_comparisons, 0.5),
                      1 - stats.binom.cdf(min(plus_signs, minus_signs) - 1, n_comparisons, 0.5))
    
    print(f"Number of pairs: {c}")
    print(f"Plus signs (+): {plus_signs} (second half > first half)")
    print(f"Minus signs (-): {minus_signs} (second half < first half)")
    print(f"Ties: {ties}")
    print(f"p-value: {p_value:.6f}")
    
    if p_value < 0.05:
        if plus_signs > minus_signs:
            print(f"\n RESULT: Significant upward trend (p < 0.05)")
        else:
            print(f"\n RESULT: Significant downward trend (p < 0.05)")
    else:
        print(f"\n RESULT: No significant trend (p >= 0.05)")
    
    return {'plus': plus_signs, 'minus': minus_signs, 'p_value': p_value}

def spearman_correlation_test(data):
    """Spearman's rank correlation test for monotonic trend"""
    print("\n" + "="*70)
    print("6. SPEARMAN'S RANK CORRELATION TEST (Bonus)")
    print("="*70)
    
    time = np.arange(len(data))
    rho, p_value = stats.spearmanr(time, data)
    
    print(f"Spearman's rho: {rho:.6f}")
    print(f"p-value: {p_value:.6f}")
    
    if p_value < 0.05:
        if rho > 0:
            print(f"\n RESULT: Significant positive monotonic trend (p < 0.05)")
        else:
            print(f"\n RESULT: Significant negative monotonic trend (p < 0.05)")
    else:
        print(f"\n RESULT: No significant monotonic trend (p >= 0.05)")
    
    return {'rho': rho, 'p_value': p_value}

def analyze_series(data, series_name="store_1_aggregated_train"):
    """
    Run comprehensive trend analysis on time series data
    
    Parameters:
    -----------
    data : array-like
        Time series data (pandas Series, numpy array, or list)
    series_name : str
        Name of the series for display purposes
    
    Returns:
    --------
    dict : Dictionary containing all test results
    """
    
    # Convert to numpy array if needed
    if isinstance(data, pd.Series):
        data_array = data.values
    else:
        data_array = np.array(data)
    
    print("\n" + "#"*70)
    print(f"COMPREHENSIVE TREND ANALYSIS FOR: {series_name}")
    print("#"*70)
    print(f"\nData points: {len(data_array)}")
    print(f"Mean: {np.mean(data_array):.2f}")
    print(f"Std Dev: {np.std(data_array):.2f}")
    print(f"Min: {np.min(data_array):.2f}")
    print(f"Max: {np.max(data_array):.2f}")
    
    results = {}
    
    # Run all tests
    results['mann_kendall'] = mann_kendall_test(data_array)
    results['adf'] = adf_test(data_array)
    results['kpss'] = kpss_test(data_array)
    results['linear_regression'] = linear_regression_test(data_array)
    results['cox_stuart'] = cox_stuart_test(data_array)
    results['spearman'] = spearman_correlation_test(data_array)
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY OF RESULTS")
    print("="*70)
    
    print("\nTrend Detection Tests:")
    if results['mann_kendall'] is not None:
        print(f"  Mann-Kendall: {results['mann_kendall'].trend} (p={results['mann_kendall'].p:.4f})")
    print(f"  Linear Regression: {'Trend' if results['linear_regression']['p_value'] < 0.05 else 'No Trend'} (p={results['linear_regression']['p_value']:.4f})")
    print(f"  Cox-Stuart: {'Trend' if results['cox_stuart']['p_value'] < 0.05 else 'No Trend'} (p={results['cox_stuart']['p_value']:.4f})")
    print(f"  Spearman: {'Trend' if results['spearman']['p_value'] < 0.05 else 'No Trend'} (p={results['spearman']['p_value']:.4f})")
    
    print("\nStationarity Tests:")
    print(f"  ADF: {'Stationary' if results['adf'][1] < 0.05 else 'Non-Stationary'} (p={results['adf'][1]:.4f})")
    print(f"  KPSS: {'Trend Stationary' if results['kpss'][1] >= 0.05 else 'Not Trend Stationary'} (p={results['kpss'][1]:.4f})")
    
    
    # Count how many tests reject null hypothesis of no trend
    trend_tests = [
        results['linear_regression']['p_value'] < 0.05,
        results['cox_stuart']['p_value'] < 0.05,
        results['spearman']['p_value'] < 0.05
    ]
    
    if results['mann_kendall'] is not None:
        trend_tests.append(results['mann_kendall'].p < 0.05)
    
    
    return results

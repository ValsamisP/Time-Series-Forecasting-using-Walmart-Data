#!/usr/bin/env python3
"""
Environment Check Script for Walmart Forecasting Project
Verifies that all dependencies are correctly installed across platforms.
"""

import sys
import platform
import subprocess
from pathlib import Path


def print_header(title):
    """Print a formatted section header."""
    width = 60
    print("\n" + "=" * width)
    print(f" {title}")
    print("=" * width)


def check_python_version():
    """Check if Python version meets requirements."""
    print_header("Python Version Check")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    print(f"Python Version: {version_str}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    
    if version < (3, 8):
        print("❌ ERROR: Python 3.8 or higher is required")
        return False
    else:
        print("✅ Python version is compatible")
        return True


def check_pip():
    """Check pip version."""
    print_header("Pip Check")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout.strip())
        print("✅ Pip is available")
        return True
    except subprocess.CalledProcessError:
        print("❌ ERROR: Pip is not available")
        return False


def check_packages():
    """Check if all required packages can be imported."""
    print_header("Package Import Check")
    
    required_packages = {
        'pandas': 'pandas',
        'numpy': 'numpy',
        'matplotlib': 'matplotlib.pyplot',
        'seaborn': 'seaborn',
        'statsmodels': 'statsmodels.api',
        'scipy': 'scipy',
        'jupyter': 'jupyter',
        'notebook': 'notebook',
        'IPython': 'IPython',
    }
    
    all_ok = True
    for display_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            # Get version if available
            module = sys.modules[import_name.split('.')[0]]
            version = getattr(module, '__version__', 'unknown')
            print(f"✅ {display_name:15s} {version}")
        except ImportError as e:
            print(f"❌ {display_name:15s} NOT INSTALLED")
            all_ok = False
    
    return all_ok


def check_data_files():
    """Check if data files exist."""
    print_header("Data Files Check")
    
    # Assuming script is run from project root
    data_dir = Path("data")
    required_files = ["train.csv", "test.csv", "features.csv", "stores.csv"]
    
    if not data_dir.exists():
        print(f"⚠️  WARNING: 'data' directory not found at {data_dir.absolute()}")
        print("   Make sure you're running this from the project root")
        return False
    
    all_files_present = True
    for filename in required_files:
        filepath = data_dir / filename
        if filepath.exists():
            size_mb = filepath.stat().st_size / (1024 * 1024)
            print(f"✅ {filename:20s} ({size_mb:.2f} MB)")
        else:
            print(f"❌ {filename:20s} NOT FOUND")
            all_files_present = False
    
    return all_files_present


def check_notebooks():
    """Check if notebooks can be found."""
    print_header("Notebook Files Check")
    
    notebooks = [
        "Part1_Comparing_HigherLevel_UnitLevel.ipynb",
        "Part2.ipynb"
    ]
    
    all_present = True
    for notebook in notebooks:
        if Path(notebook).exists():
            print(f"✅ {notebook}")
        else:
            print(f"⚠️  {notebook} not found")
            all_present = False
    
    return all_present


def test_basic_functionality():
    """Test basic data science operations."""
    print_header("Basic Functionality Test")
    
    try:
        import pandas as pd
        import numpy as np
        
        # Create simple test data
        df = pd.DataFrame({
            'A': np.random.randn(100),
            'B': np.random.randn(100)
        })
        
        # Test basic operations
        mean_a = df['A'].mean()
        std_b = df['B'].std()
        
        print("✅ Pandas DataFrame operations work")
        print("✅ NumPy random number generation works")
        print("✅ Statistical calculations work")
        return True
        
    except Exception as e:
        print(f"❌ Error during functionality test: {e}")
        return False


def main():
    """Run all checks."""
    print("\n" + "=" * 60)
    print(" WALMART FORECASTING PROJECT - ENVIRONMENT CHECK")
    print("=" * 60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Pip", check_pip),
        ("Required Packages", check_packages),
        ("Basic Functionality", test_basic_functionality),
        ("Data Files", check_data_files),
        ("Notebooks", check_notebooks),
    ]
    
    results = {}
    for name, check_func in checks:
        try:
            results[name] = check_func()
        except Exception as e:
            print(f"\n❌ Error during {name} check: {e}")
            results[name] = False
    
    # Summary
    print_header("Summary")
    
    total_checks = len(results)
    passed_checks = sum(results.values())
    
    for name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status:10s} {name}")
    
    print("\n" + "=" * 60)
    print(f" Result: {passed_checks}/{total_checks} checks passed")
    
    if passed_checks == total_checks:
        print(" 🎉 Environment is fully set up and ready!")
    elif passed_checks >= total_checks - 2:
        print(" ⚠️  Environment mostly ready, minor issues present")
    else:
        print(" ❌ Environment setup incomplete, please fix errors above")
    
    print("=" * 60 + "\n")
    
    return passed_checks == total_checks


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
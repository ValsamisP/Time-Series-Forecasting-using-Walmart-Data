# Installation & Setup - Cross-Platform Guide

This guide works for **Windows**, **macOS**, and **Linux**.

## Quick Start (Recommended)

### Option 1: Automated Setup

**Windows:**
```bash
setup.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- ✅ Check Python version (3.8+ required)
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Verify installation

---

### Option 2: Manual Setup

#### Step 1: Verify Python Installation

Check if Python 3.8+ is installed:

```bash
# Try python3 first (macOS/Linux)
python3 --version

# Or try python (Windows/some Linux)
python --version
```

If not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3` or download from [python.org](https://www.python.org/downloads/)
- **Ubuntu/Debian**: `sudo apt-get install python3 python3-pip python3-venv`
- **Fedora**: `sudo dnf install python3 python3-pip`

#### Step 2: Clone Repository

```bash
git clone https://github.com/ValsamisP/Time-Series-Forecasting-using-Walmart-Data.git
cd Time-Series-Forecasting-using-Walmart-Data
```

#### Step 3: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify activation:**
Your command prompt should now show `(venv)` at the beginning.

#### Step 4: Upgrade Pip

```bash
pip install --upgrade pip
```

#### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

**If installation fails on Windows**, try:
```bash
pip install --prefer-binary -r requirements.txt
```

**If installation fails on Linux**, you may need build tools:
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev build-essential

# Fedora
sudo dnf install python3-devel gcc gcc-c++

# Then retry
pip install -r requirements.txt
```

#### Step 6: Verify Installation

```bash
python check_environment.py
```

You should see:
```
🎉 Environment is fully set up and ready!
```

---

## Running the Project

### Jupyter Notebooks

**Activate virtual environment first** (if not already activated):

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Launch Jupyter:**
```bash
jupyter notebook
```

Navigate to:
- `Part1_Comparing_HigherLevel_UnitLevel.ipynb`
- `Part2.ipynb`

### Quarto Documents

```bash
cd myquarto
quarto preview Part1.qmd
```

Or render to HTML/PDF:
```bash
quarto render Part1.qmd --to html
quarto render Part1.qmd --to pdf  # Requires LaTeX
```

---

## Troubleshooting

### "Command not found: python3" (macOS/Linux)

Try `python` instead of `python3`:
```bash
python --version
python -m venv venv
```

### "No module named 'venv'" (Linux)

Install Python venv package:
```bash
# Ubuntu/Debian
sudo apt-get install python3-venv

# Fedora
sudo dnf install python3-venv
```

### Permission denied on setup.sh (macOS/Linux)

Make the script executable:
```bash
chmod +x setup.sh
./setup.sh
```

### Package installation errors

**Windows - Missing Visual C++ compiler:**
- Download "Microsoft C++ Build Tools" from [visualstudio.microsoft.com](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

**macOS - Missing Xcode tools:**
```bash
xcode-select --install
```

**Linux - Missing build tools:**
```bash
# Ubuntu/Debian
sudo apt-get install build-essential python3-dev

# Fedora
sudo dnf groupinstall "Development Tools"
sudo dnf install python3-devel
```

### Jupyter kernel not found

Install the kernel:
```bash
python -m ipykernel install --user --name=venv
```

### Import errors in notebooks

Make sure your virtual environment is activated and install notebook kernel:
```bash
# Activate venv first!
pip install ipykernel
python -m ipykernel install --user --name walmart-forecasting --display-name "Walmart Forecasting"
```

Then select this kernel in Jupyter: `Kernel > Change Kernel > Walmart Forecasting`

---

## Deactivating Virtual Environment

When done working:
```bash
deactivate
```

---

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 500MB for dependencies + data files
- **OS**: Windows 10+, macOS 10.14+, or modern Linux distribution

---

## What Gets Installed

Core packages installed:
- **pandas** (>=2.0.0) - Data manipulation
- **numpy** (>=1.24.0) - Numerical computing
- **matplotlib** (>=3.7.0) - Plotting
- **seaborn** (>=0.12.0) - Statistical visualization
- **statsmodels** (>=0.14.0) - Statistical models
- **scipy** (>=1.11.0) - Scientific computing
- **jupyter** (>=1.0.0) - Interactive notebooks

See `requirements.txt` for complete list.

---

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `pip` not found | Use `python -m pip` instead of `pip` |
| Virtual env won't activate | Check you're in project directory |
| Kernel not appearing in Jupyter | Run `python -m ipykernel install --user` |
| Package conflicts | Delete `venv` folder and recreate |
| Slow pip install | Add `--prefer-binary` flag |

---

## Development Setup

For contributors and developers:

```bash
pip install -r requirements-dev.txt
```

This includes:
- Testing tools (pytest)
- Code formatters (black, isort)
- Linters (flake8)

---

## Getting Help

1. Check this guide first
2. Run `python check_environment.py` to diagnose issues
3. Check existing GitHub Issues
4. Create a new issue with:
   - Your OS and Python version
   - Full error message
   - Output of `python check_environment.py`
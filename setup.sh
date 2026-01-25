#!/bin/bash
# Setup script for macOS and Linux
# Usage: ./setup.sh

set -e  # Exit on error

echo "=================================================="
echo " Walmart Forecasting Project Setup"
echo " Platform: macOS/Linux"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
echo ""
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    echo -e "${GREEN}✓ Found: $(python3 --version)${NC}"
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    echo -e "${GREEN}✓ Found: $(python --version)${NC}"
else
    echo -e "${RED}✗ Python 3 is not installed${NC}"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}✗ Python $PYTHON_VERSION found, but $REQUIRED_VERSION or higher is required${NC}"
    exit 1
fi

# Remove old virtual environment if exists
if [ -d "venv" ]; then
    echo ""
    echo -e "${YELLOW}Found existing virtual environment${NC}"
    read -p "Do you want to remove it and create a fresh one? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing old virtual environment..."
        rm -rf venv
    else
        echo "Keeping existing virtual environment"
    fi
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo -e "${GREEN}✓ Pip upgraded${NC}"

# Install dependencies
echo ""
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Run environment check
echo ""
echo "Running environment check..."
python check_environment.py

echo ""
echo "=================================================="
echo -e "${GREEN} Setup Complete!${NC}"
echo "=================================================="
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run Jupyter notebooks:"
echo "  jupyter notebook"
echo ""
echo "To run Quarto documents:"
echo "  cd myquarto"
echo "  quarto preview Part1.qmd"
echo ""
echo "=================================================="
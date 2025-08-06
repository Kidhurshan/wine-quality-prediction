# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a wine quality prediction machine learning project structured as a modular Python package. The project follows MLOps best practices with configuration-driven development.

## Architecture

The codebase follows a standard ML project structure:

- **src/Wine Quality Prediction/**: Main package directory containing all core modules
  - **components/**: ML pipeline components (data ingestion, validation, transformation, training, evaluation)
  - **config/**: Configuration management (configuration.py handles YAML configs)  
  - **entity/**: Data classes and entities (config_entity.py defines configuration structures)
  - **pipeline/**: Training and prediction pipelines
  - **utils/**: Common utilities (common.py contains shared functions)
  - **constants/**: Project constants and parameters
- **config/config.yaml**: Main configuration file for the project
- **params.yaml**: Model parameters and hyperparameters
- **schema.yaml**: Data schema definitions
- **main.py**: Main entry point for training pipeline
- **app.py**: Flask web application for model serving
- **research/**: Jupyter notebooks for experimentation
- **templates/**: HTML templates for the web interface

## Development Commands

### Environment Setup
```bash
# Install the package in development mode
pip install -e .

# Install dependencies
pip install -r requirements.txt
```

### Project Initialization
```bash
# Run template.py to create the initial file structure
python template.py
```

### Running the Application
```bash
# Run training pipeline
python main.py

# Start Flask web application  
python app.py
```

## Configuration System

The project uses YAML-based configuration:
- **config/config.yaml**: Contains paths, directories, and general settings
- **params.yaml**: Model hyperparameters and training parameters  
- **schema.yaml**: Data validation schemas

Configuration is managed through the `src/Wine Quality Prediction/config/configuration.py` module which handles loading and parsing of YAML files.

## Logging

The project uses Python's built-in logging configured in `src/Wine Quality Prediction/__init__.py`:
- Logs are written to `logs/running_logs.log`
- Console output is also enabled
- Log format includes timestamp, level, module, and message

## Package Structure

The project is set up as an installable Python package via setup.py:
- Package name: `wine_quality_prediction` 
- Source code in `src/` directory
- Version: 0.0.1
- Author: kidhu (d.kidhu@gmail.com)

## Key Dependencies

- pandas, numpy: Data manipulation
- scikit-learn: Machine learning
- matplotlib, seaborn: Visualization  
- flask, flask-cors: Web application
- PyYAML, python-box: Configuration management
- joblib: Model serialization
- tqdm: Progress bars
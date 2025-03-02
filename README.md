# Book Recommender System

Here is the project structure. To have the same structure, you can use:
```python
python template.py
```
You will have as a result the following structure:

```
book-recommendation-system/
│
├── data/
│   ├── raw/                   # Original immutable data (e.g., CSV from providers)
│   ├── processed/             # Cleaned, transformed data ready for modeling
│   ├── interim/               # Intermediate data during processing
│   └── external/              # Third-party data sources (e.g., genre mappings)
│
├── notebooks/
│   ├── 0_EDA.ipynb            # Initial exploration
│   ├── 1_Data_Cleaning.ipynb  # Data preprocessing prototype
│   ├── 2_Baseline_Models.ipynb # Initial modeling attempts
│   └── 3_Model_Evaluation.ipynb # Final evaluation
│
├── src/
│   ├── data/                  # Data processing modules
│   │   ├── make_dataset.py    # Data loading/writing
│   │   ├── preprocessing.py   # Feature engineering
│   │   └── data_validation.py # Data quality checks
│   │
│   ├── features/              # Feature engineering pipelines
│   ├── models/                # Model-related code
│   │   ├── train_model.py     # Training pipeline
│   │   ├── predict_model.py   # Inference pipeline
│   │   └── evaluate.py        # Model evaluation metrics
│   │
│   ├── visualization/         # Visualization utilities
│   ├── config/                # Configuration files
│   │   └── config.yaml        # Paths, hyperparameters, constants
│   │
│   └── utils/                 # Helper functions
│       ├── logger.py          # Logging configuration
│       └── helpers.py         # Generic utilities
│
├── models/                    # Serialized models and binaries
│   ├── trained_models/        # Saved model weights/pipelines
│   └── model_metrics/         # Performance reports
│
├── tests/                     # Unit and integration tests
│   ├── test_data.py           # Data validation tests
│   └── test_models.py         # Model logic tests
│
├── docs/                      # Documentation
│   ├── architecture.md        # System design
│   └── api_docs.md            # API specifications
│
├── reports/                   # Generated analysis/output
│   ├── figures/               # Visualizations for presentations
│   └── final_report.pdf       # Final project summary
│
├── app/                       # Deployment components
│   ├── api/                   # FastAPI/Flask endpoints
│   ├── static/                # Web assets
│   └── templates/             # HTML templates
│
├── .gitignore                 # Version control exclusion
├── requirements.txt           # Python dependencies
├── environment.yml            # Conda environment
├── setup.py                   # Package installation
└── README.md                  # Project overview & setup guide
```

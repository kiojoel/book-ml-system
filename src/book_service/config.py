from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Package root directory
PACKAGE_ROOT = Path(__file__).resolve().parent

# Data directory
DATA_DIR = PROJECT_ROOT / "data"

# Data files
TRAINING_DATA_FILE = "books.csv"

TARGET = "is_highly_rated"

#  ML Model Configuration
# Features to use in the classification model
FEATURES = [
    'num_pages',
    'ratings_count',
    'text_reviews_count',
    'publication_year',
    'language_code'
]

# Split features into types for the preprocessor
NUMERICAL_FEATURES = ['num_pages', 'ratings_count', 'text_reviews_count', 'publication_year']
CATEGORICAL_FEATURES = ['language_code']

# Paths for saving trained artifacts
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
PIPELINE_NAME = "classification_pipeline.pkl"
PIPELINE_SAVE_PATH = TRAINED_MODEL_DIR / PIPELINE_NAME
# Recommendation Model Configuration
RECOMMENDER_PIPELINE_NAME = "recommender_pipeline.pkl"
RECOMMENDER_PIPELINE_SAVE_PATH = TRAINED_MODEL_DIR / RECOMMENDER_PIPELINE_NAME
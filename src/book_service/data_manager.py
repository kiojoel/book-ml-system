import pandas as pd
from pathlib import Path
from book_service.config import DATA_DIR, TARGET

def load_dataset(*, file_name: str) -> pd.DataFrame:
    """
    Loads a CSV file and performs all initial data cleaning and
    feature engineering.
    """
    filepath = Path(DATA_DIR) / file_name
    df = pd.read_csv(filepath, on_bad_lines="skip")

    if 'bookID' in df.columns:
        df = df.drop('bookID', axis=1)
    df.columns = df.columns.str.strip()

    # Handle and feature engineer the publication_date
    df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
    df['publication_year'] = df['publication_date'].dt.year

    # We use the median as the threshold for a balanced classification
    median_rating = df['average_rating'].median()
    df[TARGET] = (df['average_rating'] >= median_rating).astype(int)

    # Group various English codes into a single 'eng' category
    eng_codes = ['eng', 'en-US', 'en-GB', 'en-CA', 'enm']
    df['language_code'] = df['language_code'].apply(lambda x: 'eng' if x in eng_codes else x)

    # Drop rows with missing values that were created
    df.dropna(inplace=True)

    return df
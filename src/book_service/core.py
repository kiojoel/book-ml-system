import joblib
import pandas as pd
from book_service.config import PIPELINE_SAVE_PATH,RECOMMENDER_PIPELINE_SAVE_PATH,TRAINING_DATA_FILE
from book_service.data_manager import load_dataset

classification_pipeline = joblib.load(PIPELINE_SAVE_PATH)
recommender_artifacts = joblib.load(RECOMMENDER_PIPELINE_SAVE_PATH)

def make_prediction(*, input_data)-> dict:
  data = pd.DataFrame([input_data])
  prediction = classification_pipeline.predict(data)
  return {"prediction": int(prediction[0])}

def get_recommendations(*, title: str) -> dict:
    # Load the full dataset to map indices to titles
    data = load_dataset(file_name=TRAINING_DATA_FILE).reset_index()
    # Extract recommender components
    vectorizer = recommender_artifacts['vectorizer']
    similarity_matrix = recommender_artifacts['similarity_matrix']

    # Find the index of the book that matches the title
    try:
        idx = data[data['title'] == title].index[0]
    except IndexError:
        return {"error": f"Book with title '{title}' not found."}

    # Get similarity scores and sort them
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar books (excluding itself)
    sim_scores = sim_scores[1:6]
    book_indices = [i[0] for i in sim_scores]

    recommendations = data['title'].iloc[book_indices].tolist()
    return {"recommendations": recommendations}
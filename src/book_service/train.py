from sklearn.model_selection import train_test_split
from book_service.data_manager import load_dataset
from book_service.pipeline import book_classification_pipeline
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from book_service.config import(
   TRAINING_DATA_FILE,TARGET,
   FEATURES,PIPELINE_SAVE_PATH,
   TRAINED_MODEL_DIR,
   RECOMMENDER_PIPELINE_SAVE_PATH
   )



def run_training():
  """Train the model."""

  data = load_dataset(file_name=TRAINING_DATA_FILE)

  tfidf_vectorizer = TfidfVectorizer(stop_words='english')
  tfidf_matrix = tfidf_vectorizer.fit_transform(data['title'])
  cosine_sim = cosine_similarity(tfidf_matrix)

  recommender_artifacts = {
    'vectorizer': tfidf_vectorizer,
    'similarity_matrix': cosine_sim
}
  joblib.dump(recommender_artifacts, RECOMMENDER_PIPELINE_SAVE_PATH)

  X = data[FEATURES]
  y = data[TARGET]

  X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size = 0.2, random_state = 42
     )

  book_classification_pipeline.fit(X_train,y_train)

  TRAINED_MODEL_DIR.mkdir(parents=True, exist_ok=True)
  joblib.dump(book_classification_pipeline,PIPELINE_SAVE_PATH)

  print(f"Training complete. Pipeline saved to: {PIPELINE_SAVE_PATH}")



if __name__ == "__main__":
    run_training()


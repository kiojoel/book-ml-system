from sklearn.model_selection import train_test_split
from book_service.data_manager import load_dataset
from book_service.pipeline import book_classification_pipeline
from book_service.config import TRAINING_DATA_FILE,TARGET,FEATURES
from book_service.config import PIPELINE_SAVE_PATH, TRAINED_MODEL_DIR
import joblib



def run_training():
  """Train the model."""

  data = load_dataset(file_name=TRAINING_DATA_FILE)

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


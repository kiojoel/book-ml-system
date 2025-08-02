from sklearn.model_selection import train_test_split
from book_service.data_manager import load_dataset
from book_service.pipeline import book_classification_pipeline
from book_service.config import TRAINING_DATA_FILE,TARGET,FEATURES


def run_training():
  """Train the model."""

  data = load_dataset(file_name=TRAINING_DATA_FILE)

  X = data[FEATURES]
  y = data[TARGET]

  X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size = 0.2, random_state = 42
     )

  book_classification_pipeline.fit(X_train,y_train)

  print("Training complete.")



if __name__ == "__main__":
    run_training()


from sklearn.pipeline import Pipeline
from book_service.processing.features import feature_preprocessor
from book_service.models.classification import classification_model

book_classification_pipeline = Pipeline([
  ('preprocessing', feature_preprocessor),
  ('model', classification_model)
])
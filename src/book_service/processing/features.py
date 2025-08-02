from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from book_service.config import NUMERICAL_FEATURES, CATEGORICAL_FEATURES


feature_preprocessor  = ColumnTransformer(
  transformers=[
    ('num', StandardScaler(), NUMERICAL_FEATURES ),
    ('cat', OneHotEncoder(handle_unknown='ignore'), CATEGORICAL_FEATURES)
  ]
)
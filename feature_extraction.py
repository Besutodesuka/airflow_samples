import pandas as pd
# source
# https://www.kaggle.com/competitions/playground-series-s5e1/data?select=train.csv

# path is at '/tmp/airflowtmp2tvlf56y/
# argparse
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pickle
import sys
sys.path.append("/home/65070503434_DAG/")

# Sample dataset
data = pd.read_csv("./train.csv")

# Define features and target
X = data.drop(columns=['num_sold', 'date'])
y = data['num_sold']

categorical_features = X.columns

# columns transform 
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
])

# ColumnTransformer
X_transformed = preprocessor.fit_transform(X)
    
# Save preprocessor
pickle.dump(preprocessor, "preprocessor.pkl")
pickle.dump(X_transformed, "X_transformed.pkl")
pickle.dump(y, "y.pkl")

print("Preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()
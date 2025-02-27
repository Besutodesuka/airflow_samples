import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import os

# Sample dataset
data = pd.read_csv("./train.csv")

# Define features and target
X = data.drop(columns=['num_sold', 'date'])
y = data['num_sold']




# Create pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', DecisionTreeRegressor())
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Output predictions
print(predictions)

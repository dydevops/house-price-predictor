# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import joblib

# # Sample training data
# data = {
#     'area': [1000, 1500, 2000, 2500, 3000],
#     'bedrooms': [2, 3, 3, 4, 4],
#     'age': [5, 10, 15, 20, 25],
#     'price': [300000, 400000, 500000, 600000, 650000]
# }

# df = pd.DataFrame(data)
# X = df[['area', 'bedrooms', 'age']]
# y = df['price']

# model = LinearRegression()
# model.fit(X, y)

# # Save the model
# joblib.dump(model, 'ml/house_price_model.pkl')
# print("Model trained and saved successfully.")

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    # Read updated training data from CSV
    df = pd.read_csv('ml/data.csv')

    # Define features and target
    X = df[['area', 'bedrooms', 'age']]
    y = df['price']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save trained model
    os.makedirs('ml', exist_ok=True)
    joblib.dump(model, 'ml/house_price_model.pkl')
    print("Model auto-trained and saved.")

# Call this function wherever needed
train_model()

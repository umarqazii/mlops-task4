import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
df = pd.read_csv('dataset.csv')

# Prepare the data
X = df[['Id']]
y = df['Coin_Flip_Binary']

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Save the model to disk
joblib.dump(model, 'model.pkl')

print("Model trained and saved as model.pkl")

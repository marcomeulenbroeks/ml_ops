import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

df = pd.read_csv('data/ice_cream_sales_dataset.csv')

X = df[['temperature_celsius', 'num_tourists']]
y = df['ice_creams_sold']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

os.makedirs('models', exist_ok=True)
model_filename = "models/linear_model.pkl"
joblib.dump(model, model_filename)

print(f"Model saved as: {model_filename}")
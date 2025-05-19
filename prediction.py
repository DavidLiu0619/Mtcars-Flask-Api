import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("mtcars.csv")

# Drop 'model' column if it exists
data = data.drop(columns=['model'], errors='ignore')

# Define target and selected features
labels = data['mpg']
col_imp = ["wt", "am", "qsec", "gear", "drat", "cyl"]
features = data[col_imp]

# Train the model
model = LinearRegression()
model.fit(features, labels)

# Prediction function
def predict(dict_values, col_imp=col_imp, model=model):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1, -1)
    y_pred = model.predict(x)[0]
    return y_pred

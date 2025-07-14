import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 4, 5, 4, 5])

# Create and fit model
model = LinearRegression()
model.fit(X, Y)

# Prediction
y_pred = model.predict(X)

# Plotting
plt.scatter(X, Y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Regression line')
plt.title('Simple Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Coefficients
print(f"Slope (coefficient): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
print(f"Equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")

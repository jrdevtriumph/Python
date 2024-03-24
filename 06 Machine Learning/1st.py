# Generate some sample data
X = [0.5, 1.2, 2.0, 2.5, 3.0]  # Sample input data
y = [2.0, 2.8, 4.0, 5.0, 6.0]   # Sample output data

# Calculate the mean of X and y
mean_X = sum(X) / len(X)
mean_y = sum(y) / len(y)



# Calculate the slope (m) and y-intercept (c) of the line
m = sum((xi - mean_X) * (yi - mean_y) for xi, yi in zip(X, y)) / sum((xi - mean_X)**2 for xi in X)
c = mean_y - m * mean_X

# Make predictions for new input values
def predict(x):
    return m * x + c

# Test the model with a new input
new_x = 4.5
predicted_y = predict(new_x)
print("Predicted y for x =", new_x, "is", predicted_y)
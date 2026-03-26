import numpy as np
import matplotlib.pyplot as plt

# Study Hours vs Marks Data
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
marks = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Scatter Plot
plt.figure()
plt.scatter(study_hours, marks, color='blue', label="Data Points")

# Best Fit Line
m, b = np.polyfit(study_hours, marks, 1)
plt.plot(study_hours, m*study_hours + b, color='red', label="Best Fit Line")

# Labels and Title
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Time vs Marks Analysis")
plt.legend()

# Prediction
hours = float(input("Enter study hours: "))
predicted_marks = m * hours + b
print("Predicted Marks:", round(predicted_marks, 2))

# Show Graph
plt.show()

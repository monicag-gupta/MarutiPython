from sklearn.neighbors import KNeighborsClassifier
import numpy as np
# Sample data (features: [height, weight], labels: 0 = Class A, 1 = Class B)
X = np.array([
    [160, 55],
    [165, 60],
    [170, 65],
    [175, 70],
    [180, 75],
    [155, 50],
    [150, 45],
    [185, 80],
    [190, 85],
    [195, 90]
])
y = np.array([0, 0, 0, 1, 1, 0, 0, 1, 1, 1])  # Labels

# Create the KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn.fit(X, y)

# Predict a new sample
new_data = np.array([[172, 66]])  # A new person (height, weight)
prediction = knn.predict(new_data)

# Output : Predicted class: 0
print("Predicted class:", prediction[0]) 






#######

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = load_iris()
# Features (X) and labels (y)
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Labels (species)
# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a KNN classifier with 3 neighbors
knn = KNeighborsClassifier(n_neighbors=3)
# Train the KNN classifier
knn.fit(X_train, y_train)
# Make predictions on the test set
y_pred = knn.predict(X_test)
# Evaluate the model using accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of KNN classifier: {accuracy * 100:.2f}%")




#####


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Training data: Height, Weight
X = np.array([
    [160, 55],
    [165, 60],
    [170, 65],
    [175, 70],
    [180, 75],
    [155, 50],
    [150, 45],
    [185, 80],
    [190, 85],
    [195, 90]
])

# Labels (0 = Class A, 1 = Class B)
y = np.array([0, 0, 0, 1, 1, 0, 0, 1, 1, 1])

# New test data (height=172, weight=66)
new_data = np.array([[172, 66]])

# KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Prediction
prediction = knn.predict(new_data)
print("Predicted class for", new_data[0], "is:", prediction[0])

# --- Visualization ---
# Split by class
X_class0 = X[y == 0]
X_class1 = X[y == 1]

plt.scatter(X_class0[:, 0], X_class0[:, 1], color='blue', label='Class 0')
plt.scatter(X_class1[:, 0], X_class1[:, 1], color='green', label='Class 1')
plt.scatter(new_data[0, 0], new_data[0, 1], color='red', marker='X', s=100, label='Test Point')

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("KNN Classification Example")
plt.legend()
plt.grid(True)
plt.show()



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


import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump

# TODO: you should fetch the data from the MongoDB database
df = pd.read_csv("wine.csv")

# set the features and labels
y = df["target"]
X = df.drop(["id", "target"], axis=1)

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train the model
model = KNeighborsClassifier(n_neighbors=20)
model.fit(X_train, y_train)

# see how the model performs on the training and test data
y_pred_test = model.predict(X_test)
y_pred_train = model.predict(X_train)
print(f"Training accuracy: {accuracy_score(y_train, y_pred_train)}")
print(f"Test accuracy: {accuracy_score(y_test, y_pred_test)}")

# save the model to file
# this model should be used when making predictions through the API
dump(model, "model.joblib")

# can be loaded with the following code:
# from joblib import load
# model = load("model.joblib")
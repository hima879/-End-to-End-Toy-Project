# train.py
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv("placement.csv")
df = df.iloc[:, 1:]          # drop the unnamed index column

X = df.iloc[:, 0:2]          # cgpa, iq
y = df.iloc[:, -1]           # placement

# Train
clf = LogisticRegression()
clf.fit(X, y)

# Save
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Saved new model.pkl")
print("Model expects features in order:", list(X.columns))
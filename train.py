import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

# load the dataset
df = pd.read_csv("student_data.csv")

print("Dataset loaded:", df.shape[0], "rows")
print()

# separate features and target
X = df[["study_hours", "attendance", "past_score", "sleep_hours", "extra_classes"]]
y = df["final_score"]

# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print()

# train the model
model = LinearRegression()
model.fit(X_train, y_train)

# test the model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("Model trained successfully!")
print("R2 Score:", round(r2, 2))
print("Mean Absolute Error:", round(mae, 2))
print()

# show which features matter most
features = ["study_hours", "attendance", "past_score", "sleep_hours", "extra_classes"]
print("Feature importance:")
for f, c in zip(features, model.coef_):
    print(" ", f, "->", round(c, 2))

# save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print()
print("Model saved as model.pkl")
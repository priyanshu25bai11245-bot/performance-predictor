import pickle

# load the saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Student Performance Predictor")
print("------------------------------")

# take input from user
study = float(input("Enter study hours per day (1-10): "))
attendance = float(input("Enter attendance percentage (40-100): "))
past = float(input("Enter previous exam score (0-100): "))
sleep = float(input("Enter sleep hours per day (4-10): "))
extra = int(input("Do you attend extra classes? (1=Yes, 0=No): "))

# predict the score
features = [[study, attendance, past, sleep, extra]]
predicted = model.predict(features)[0]
predicted = round(min(max(predicted, 0), 100), 1)

print()
print("Predicted Final Score:", predicted, "/ 100")

# show result category
if predicted >= 85:
    print("Performance: Excellent")
elif predicted >= 70:
    print("Performance: Good")
elif predicted >= 50:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")

# simple suggestions
print()
print("Suggestions:")
if study < 4:
    print("- Try to study at least 4-5 hours daily")
if attendance < 75:
    print("- Improve your attendance to at least 75%")
if sleep < 6:
    print("- Try to get at least 6-7 hours of sleep")
if predicted >= 85:
    print("- Great work, keep it up!")
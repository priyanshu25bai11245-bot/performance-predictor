# Student Performance Predictor

A simple machine learning project that predicts a student's final exam score based on their study habits and attendance.

---

## What this project does

This project takes some basic information about a student like study hours, attendance, and past scores and predicts what their final exam score might be. It also tells the student whether their performance is Excellent, Good, Average, or Needs Improvement.

---

## Files in this project

| File | What it does |
|------|-------------|
| generate_dataset.py | Creates a dataset of 200 student records |
| train.py | Trains a machine learning model on the dataset |
| predict.py | Takes user input and predicts the final score |
| student_data.csv | The dataset (created after running generate_dataset.py) |
| model.pkl | The trained model (created after running train.py) |

---

## How to run this project

**Step 1 - Install the required libraries**
```
pip install pandas scikit-learn
```

**Step 2 - Generate the dataset**
```
python generate_dataset.py
```

**Step 3 - Train the model**
```
python train.py
```

**Step 4 - Run the predictor**
```
python predict.py
```

---

## What inputs does it need

When you run predict.py it will ask you to enter:
- Study hours per day (between 1 and 10)
- Attendance percentage (between 40 and 100)
- Previous exam score (between 0 and 100)
- Sleep hours per day (between 4 and 10)
- Whether you attend extra classes (1 for Yes, 0 for No)

---

## Example output

```
Student Performance Predictor
------------------------------
Enter study hours per day (1-10): 6
Enter attendance percentage (40-100): 80
Enter previous exam score (0-100): 72
Enter sleep hours per day (4-10): 7
Do you attend extra classes? (1=Yes, 0=No): 1

Predicted Final Score: 81.4 / 100
Performance: Good

Suggestions:
- Great work, keep it up!
```

---

## Libraries used

- pandas
- scikit-learn

---

## Author
Priyanshu
VITyarthi BYOP Project

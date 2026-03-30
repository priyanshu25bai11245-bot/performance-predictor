import pandas as pd
import random

random.seed(42)

data = []

for i in range(200):
    study = round(random.uniform(1, 10), 1)
    attendance = round(random.uniform(40, 100), 1)
    past = round(random.uniform(30, 100), 1)
    sleep = round(random.uniform(4, 10), 1)
    extra = random.randint(0, 1)

    # simple formula to calculate final score
    score = (study * 3.5) + (attendance * 0.3) + (past * 0.4) + (sleep * 1.2) + (extra * 5)
    score = score + random.uniform(-5, 5)  # add some noise
    score = round(min(max(score, 0), 100), 1)  # keep between 0 and 100

    data.append([study, attendance, past, sleep, extra, score])

df = pd.DataFrame(data, columns=["study_hours", "attendance", "past_score", "sleep_hours", "extra_classes", "final_score"])
df.to_csv("student_data.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print(df.head())
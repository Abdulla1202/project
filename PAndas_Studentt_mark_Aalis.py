import pandas as pd

# ---------- Step 1: Create some sample data ----------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 67, 90, 76, 92],
    "Science": [78, 80, 95, 66, 88],
    "English": [90, 72, 85, 60, 91]
}

df = pd.DataFrame(data) # give values to student in a charte

print("📊 Student Marks Data")
print(df)

# ---------- Step 2: Basic Statistics ----------
print("\n🔎 Summary Statistics:")
print(df.describe()) # Provides count, mean, std, min, 25%, 50%, 75%, max for each subject  

# ---------- Step 3: Find Topper in Each Subject ----------
print("\n🏆 Toppers in Each Subject:")
for subject in ["Maths", "Science", "English"]:
    topper = df.loc[df[subject].idxmax()] # Get the row of the topper
    print(f"{subject}: {topper['Name']} with {topper[subject]} marks") 

# ---------- Step 4: Add a Total and Average column ----------
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1) # total marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1) # avereg marks

print("\n📊 Data with Total and Average:")
print(df)

# ---------- Step 5: Filter students with Average > 80 ----------
print("\n🎯 Students with Average > 80:")
print(df[df["Average"] > 80])

# ---------- Step 6: Save to CSV ----------
df.to_csv("student_results.csv", index=False)
print("\n✅ Results saved to student_results.csv")

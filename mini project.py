import numpy as np

marks = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [90, 76, 85],
    [65, 70, 60]
])

# Student names and subject names
students = ['Alice', 'Bob', 'Charlie', 'David']
subjects = ['python', 'os', 'java']

# Average marks per student
avg_per_student = np.mean(marks, axis=1)
print("Average Marks per Student:")
for name, avg in zip(students, avg_per_student):
    print(f"{name}: {avg:.2f}")

# Average marks per subject
avg_per_subject = np.mean(marks, axis=0)
print("\nAverage Marks per Subject:")
for subj, avg in zip(subjects, avg_per_subject):
    print(f"{subj}: {avg:.2f}")

# Highest and lowest marks in each subject
print("\nHighest and Lowest Marks per Subject:")
for i, subj in enumerate(subjects):
    print(f"{subj} - Highest: {np.max(marks[:, i])}, Lowest: {np.min(marks[:, i])}")

# Overall class average
overall_avg = np.mean(marks)
print(f"\nOverall Class Average: {overall_avg:.2f}")


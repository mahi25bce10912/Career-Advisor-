"""
Career Advisor Application
"""
import numpy as np
import matplotlib.pyplot as plt
import random

# Initialize data
subjects = ["Math", "Science", "English", "History", "Programming"]
marks = []

# Get marks from user
print("CAREER ADVISOR SYSTEM")
print("Please enter your marks (0-100):")
for subject in subjects:
    while True:
        try:
            mark = int(input(f"{subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter a number between 0 and 100")
        except:
            print("Please enter a valid number")

# Convert to numpy array
marks_array = np.array(marks)

# Find strongest subject
strongest_index = np.argmax(marks_array)
strongest_subject = subjects[strongest_index]
strongest_mark = marks_array[strongest_index]

print(f"\n Your strongest subject is {strongest_subject} with {strongest_mark}%")

# Career recommendations
career_map = {
    "Math": ["Data Analyst", "Statistician", "Actuary"],
    "Science": ["Research Scientist", "Biomedical Engineer", "Doctor"],
    "English": ["Writer", "Editor", "Content Manager"],
    "History": ["Historian", "Researcher", "Teacher"],
    "Programming": ["Software Developer", "Web Developer", "App Developer"]
}

print("\n RECOMMENDED CAREERS:")
for career in career_map[strongest_subject]:
    salary = random.randint(50000, 120000)
    print(f"• {career}: ${salary:,}/year")

# Performance classification
print("\n PERFORMANCE ANALYSIS:")
for i, subject in enumerate(subjects):
    mark = marks[i]
    if mark >= 90:
        level = "Excellent "
    elif mark >= 75:
        level = "Good "
    elif mark >= 60:
        level = "Average "
    else:
        level = "Needs Improvement "
    print(f"{subject}: {mark}% - {level}")

# Simple prediction
if len(marks) > 1:
    avg_marks = np.mean(marks_array)
    if avg_marks >= 80:
        prediction = "Excellent! Keep up the great work! "
    elif avg_marks >= 70:
        prediction = "Good performance! You're doing well! "
    elif avg_marks >= 60:
        prediction = "Average - there's room for improvement! "
    else:
        prediction = "Focus on improving your studies! "
    
    print(f"\n PREDICTION: {prediction}")

# Create visualization
plt.figure(figsize=(12, 5))

# Bar chart
plt.subplot(1, 2, 1)
colors = ['lightblue', 'lightgreen', 'lightcoral', 'plum', 'orange']
bars = plt.bar(subjects, marks, color=colors)
bars[strongest_index].set_color('gold')  # Highlight strongest subject

plt.title('Subject Marks')
plt.xlabel('Subjects')
plt.ylabel('Marks (%)')
plt.ylim(0, 100)
plt.grid(True, alpha=0.3)

# Performance distribution
plt.subplot(1, 2, 2)
categories = ['Excellent (90+)', 'Good (75-89)', 'Average (60-74)', 'Needs Improvement (<60)']
counts = [
    len([m for m in marks if m >= 90]),
    len([m for m in marks if 75 <= m < 90]),
    len([m for m in marks if 60 <= m < 75]),
    len([m for m in marks if m < 60])
]

# Only show categories that have data
labels = [categories[i] for i in range(4) if counts[i] > 0]
sizes = [counts[i] for i in range(4) if counts[i] > 0]

if sizes:
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'blue', 'orange', 'red'])
    plt.title('Performance Distribution')
else:
    plt.text(0.5, 0.5, 'No Data', ha='center', va='center', fontsize=16)
    plt.title('No Data Available')

plt.tight_layout()
plt.show()

print(f"\n TIP: {random.choice(['Practice regularly!', 'Set study goals!', 'Ask for help when needed!', 'Stay consistent!'])}")

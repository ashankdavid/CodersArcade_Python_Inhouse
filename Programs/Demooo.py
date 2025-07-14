# Input marks for 5 subjects
marks = []
total_subjects = 5

print("Enter marks for 5 subjects:")
for i in range(1, total_subjects + 1):
    while True:
        try:
            mark = int(input(f"Enter marks for subject {i}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

# Calculate total marks and percentage
total_marks = sum(marks)
max_marks = total_subjects * 100
percentage = (total_marks / max_marks) * 100

# Determine grade
if percentage >= 75:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 30:
    grade = "C"
else:
    grade = "Fail"

# Display the results
print("\n----- Result -----")
print(f"Total Marks: {total_marks}/{max_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

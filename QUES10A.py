
# Mini Challenge (Choose ONE):  Attendance Percentage Calculator (eligible if attendance ≥75%)



total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance_percentage = (attended_classes / total_classes) * 100

# Display result
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("✅ Eligible for exam (attendance ≥ 75%)")
else:
    print("❌ Not eligible for exam (attendance < 75%)")


# Input the length and width (in metres) of a rectangular plot and calculate its area. 
# Modify Problem 3 to accept dimensions in feet and display the area in square metres.




length_feet = float(input("Enter the length of the plot (in feet): "))
width_feet = float(input("Enter the width of the plot (in feet): "))

# Convert feet to metres
length_metres = length_feet * 0.3048
width_metres = width_feet * 0.3048

# Calculate area in square metres
area = length_metres * width_metres

# Display result
print("The area of the rectangular plot is", area, "square metres.")


# Input the number of seconds (1–86400) and display the equivalent time in HH:MM: SS format. 



seconds = int(input("Enter seconds (1–86400): "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{hours:02}:{minutes:02}:{secs:02}")

#ASSIGNMENT 1: FITNESS BAND HEART RATE ANALYSIS

# Step 1: Import NumPy
import numpy as np

# Step 2: Create a 1-D NumPy array containing
# 10 random heart-rate values between 80 and 150
# 151 is used because the upper limit is excluded
heart_rate = np.random.randint(80, 151, 10)

# Step 3: Display all heart-rate readings
print("Heart rates for 10 minutes:")
print(heart_rate)

# Step 4: Slice the array to get the first 5 minutes
first_5_minutes = heart_rate[:5]

# Display the first 5 minutes
print("\nHeart rates during first 5 minutes:")
print(first_5_minutes)

# Step 5: Calculate the maximum heart rate
maximum = np.max(heart_rate)

# Step 6: Calculate the minimum heart rate
minimum = np.min(heart_rate)

# Step 7: Calculate the average heart rate
average = np.mean(heart_rate)

# Display the results
print("\nMaximum heart rate:", maximum, "BPM")
print("Minimum heart rate:", minimum, "BPM")
print("Average heart rate:", round(average, 2), "BPM")

# Step 8: Identify heart rates greater than 120 BPM
high_rate = heart_rate > 120

# Display the actual heart rates above 120
print("\nHeart rates exceeding 120 BPM:")
print(heart_rate[high_rate])

# Step 9: Identify the minutes where heart rate exceeded 120 BPM
# NumPy index starts from 0, so +1 converts it to minute number
minutes = np.where(heart_rate > 120)[0] + 1

# Display the minute numbers
print("\nMinutes where heart rate exceeded 120 BPM:")
print(minutes)

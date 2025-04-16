'''In this assignment, you will create a Python program to track your daily heart rate at different times and calculate the average.

Objective:
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.'''
time_slots = "Morning", "Midday", "Afternoon", "Evening" #Times
heart_rates=[]#List
for time in time_slots:#Loop
    beats= int(input(f"What is your heart rate (in BPM) at {time}? "))#Gets user input
    heart_rates.append([time, beats])#Multilevel list
bpm_values= [rate[1] for rate in heart_rates]
average= sum(bpm_values)/4#Equation for BPM
print("Your average heart rate is", average, "Beats Per Minute.")#End result

#Gulzat Kaipova
#7.11.2023
#This Python code converts a speed value from kilometers per hour (km/h) to miles per hour (mph)
#!/usr/bin/env python
kmh = int(input("Enter km/h: "))
#This line prompts the user to enter a speed value in kilometers per hour and stores the input as an integer in the variable kmh.
mph =  0.6214 * kmh
#This line calculates the equivalent speed in miles per hour by multiplying the value of kmh by the conversion factor 0.6214. The result is stored in the variable mph.
print("Speed:", kmh, "KM/H = ", mph, "MPH")
#This line prints the original speed in kilometers per hour (kmh), followed by the string "KM/H =", the calculated speed in miles per hour (mph), and finally the string "MPH". The output displays the converted speed in miles per hour.

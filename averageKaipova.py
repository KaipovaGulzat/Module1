#Gulzat Kaipova
#7.11.2023
#This Python code prompts the user to enter scores for three rounds, calculates the average of those scores, and then prints the average score.
#!/usr/bin/env python
round1 = int(input("Enter score for round 1: ")) 
#This line prompts the user to enter the score for round 1 and stores the input as an integer in the variable 'round 1'.
round2 = int(input("Enter score for round 2: ")) 
#This line prompts the user to enter the score for round 2 and stores the input as an integer in the variable 'round 2'.
round3 = int(input("Enter score for round 3: ")) 
#This line prompts the user to enter the score for round 3 and stores the input as an integer in the variable 'round 3'.
average = (round1 + round2 + round3) / 3 
#This line calculates the average score by adding up round 1, round 2, and round 3, and then dividing the sum by 3. The result is stored in the variable average.
print ("the average score is: ", average)
#This line prints the string "the average score is: " followed by the value of the variable average. The average score is displayed as output to the user.

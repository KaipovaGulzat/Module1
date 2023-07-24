#Gulzat Kaipova
#7.11.2023 
#this code prompts the user to enter a username, checks if the entered username matches any of the valid usernames, and then provides access or denies access based on the comparison result.
#!/usr/bin/env python
username = input("Login: >> ")
#This line prompts the user to enter a username
user1 = "Jack"
user2 = "Jill"
#These two lines define two variables, user1 and user2, with the values "Jack" and "Jill", respectively. 
#These variables represent the valid usernames that can be used for login.
if username == user1:
    print("Access granted")
elif username == user2:
    print("Welcome to the system")
else:
    print("Access denied")
#This block of code uses an if-elif-else statement to check the entered username against the valid usernames.
#If the username matches the value of user1, it prints "Access granted".
#If the username matches the value of user2, it prints "Welcome to the system".
#If the username does not match either user1 or user2, it prints "Access denied".

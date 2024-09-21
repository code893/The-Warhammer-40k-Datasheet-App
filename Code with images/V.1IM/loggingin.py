from getpass import getpass
from os import system

import time


def loginPage():
	# opens a file to read
	file = open("usernames.txt", "r")
	file_data = file.readlines()
	users = []
	passwords = []
	# adds the lines from a file into 2 lists
	# 1 for users and 1 for passwords
	for line in file_data:
		temp = line.strip("\n")
		usern,passw = temp.split(",")
		users.append(usern)
		passwords.append(passw)
	file.close()
	
	login_page = True
		
	while login_page == True:
		print("""
		MAIN MENU
Enter a choice:
1 - Login
2 - Exit
""")
		choice = int(input("Enter a choice: "))
		if choice == 1:
			system('clear')
			print("""
LOGIN PAGE""")
			username = input("Username: ").lower()
			print("You will be unable to see what you type as it is hidden; securing your password")
			password = getpass()
			time.sleep(1)
			print("Keep Writing your password is being inputted")
			if username.lower() in users:
				position = users.index(username)
				if password == passwords[position]:
					print("Welcome, " + username)
					login_page = False
				else:
					print("""

        Incorrect password        """)
			else:
				print("""

        Username not found        """)

		elif choice == 2:
			system('clear')
			print("""
USER REGISTRATION PAGE""")
			new_username = input("New username: ")
			while new_username.lower() in users:
				print("Username already exists")
				new_username = input("New username: ")
			new_password = input("Password (8 characters or more): ")
			attempts = 3
			while len(new_password) < 8 and attempts !=0:
				print("Password must be 8 characters or more")
				attempts -= 1
				new_password = input("Password (8 characters or more): ")
			if attempts == 0:
				print("You have been locked out")
				quit()
			print("You have sucessfully created a new user account")
			file = open("usernames.txt", "a")
			file.write("\n" + new_username.lower() + "," + new_password)
			file.close()
			login_page = False
		elif choice == 2:
			quit()
		else:
			print("Invalid choice")

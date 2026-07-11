# # conditional statements are certain keywords we to use write a program (if, elif and else)
# # if statement 
# x = 30
# if x > 20:
#     print("X is greater than 20")

# print()

# # Elif statement
# if x > 40:
#     print("X is greater")
# elif x < 40:
#     print("X is less")

# print()

# # else statement
# if x > 40:
#     print("X is greater")
# elif x == 40:
#     print("x is equal to 40")
# else:
#     print("It's none of the above")


# print()

# pin = 2345
# # pinn = int(input("Enter Your transaction pin: "))

# if pinn == pin:
#     print("Access Granted")
# else:
#     print("Incorrect pin")

print()
#===============================================================================
# Modules
#Math module
# from math import pi
# print(pi)

import math
print(dir(math))

print(f"Pi --> {math.pi}")
print(math.sqrt(100))
print(math.floor(4.9))
print(math.ceil(4.9))
print(math.pow(2, 10))

radius = 7
area = math.pi * math.pow(radius, 2)
print(f"Area: {area}")


print()

#hashlib
import hashlib
# print(dir(hashlib))
hash1 = hashlib.sha512("car".encode()).hexdigest()
hash2 = hashlib.sha256("car".encode()).hexdigest()
hash3 = hashlib.md5("car".encode()).hexdigest()
print(hash1)
print(hash2)
print(hash3)

print()

# stored_hash = hashlib.sha256("password123".encode()).hexdigest()
# user_input = input("Enter your Password: ")
# user_hash = hashlib.sha256(user_input.encode()).hexdigest()

# if user_hash == stored_hash:
#     print("Access Granted: ")
# else:
#     print("Access denied")

# print()

import socket
ip = socket.gethostbyname("earlycode.net")
print(ip)
# print(dir(socket))

print()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)

result = s.connect_ex(("scanme.nmap.org", 80))

if result == 0:
    print("Port 80 is OPEN")
else:
    print("Port 80 is CLOSED")

s.close()


print()

import random 
selection = ['rock', 'paper', 'scissors' ]
computer = random.choice(selection)
user = input("Enter your selection: ")
if user not in selection:
    print("Invalid selection.")
elif user == 'rock' and computer == 'scissors':
    print("You won, computer chose", computer)
elif user == 'paper' and computer == 'rock':
    print("You won, computer chose", computer)
elif user == 'scissors' and computer == 'paper':
    print("You won, computer chose", computer)
else:
    print("You lost, computer chose", computer)
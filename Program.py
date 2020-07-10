import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('How many passwords would you like to generate?\n')
number = int(number)

length = input('Password Length:\n ')
length = int(length)

print('\nGenerated Password: ')

for pw in range(number):
  password = ''
  for i in range(length):
    password += random.choice(chars)
  print(password)
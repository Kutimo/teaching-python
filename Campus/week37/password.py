""" Skriv et program som ber brukeren om passord "Gokstad123".

Enter password: hello
Wrong, try again!
Enter password: Gokstad123
Access granted!

Make sure the user input is a string
 """

while True:
  attempt = input("Enter password: ")
  if attempt != password:
    print("Wrong, try again!")
  elif attempt == password: 
    print("Access granted!")
    break
  else:
    print("Something went wrong")


password = 1234

while True:
  attempt = input("Password: ")
  if attempt.isdigit():
    attempt = int(attempt)
    if attempt == password:
      print("Access granted")
      break
    elif attempt != password:
      print("wrong password")
    else:
      print("Something went wrong")
  else:
    print("password contains only numbers, please try again")


""" def main():
  print("hello world")
  normal_while_Loop()


def normal_while_Loop():
  while count <= 3:
    print("Count is:", count)
    count += 1 """

""" Continuous loop """
""" count = 1
while True:
    count += 1
    print("Count is:", count) """
""" 
while True:
    text = input("Type 'stop' to quit: ")
    if text == "stop":
        print("Loop ended.")
        break
    print("You typed:", text)


for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num) """


from helpers.say_hello import greet
name = input("Enter your name: ")
print(greet(name))

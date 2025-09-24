""" 

fruit_list = ["apple", "banana", "melon", "kiwi"]

fruit_list.append("kiwi")
fruit_list.insert(3, "orange")

print(fruit_list)

print(fruit_list.count("kiwi"))
""" 
""" while True:
  print(fruit_list)
  user_input = input("Please add a fruit: ")
  fruit_list.append(user_input)
 """

fruit_list = ["apple", "banana", "melon", "kiwi"]

def print_name(i):
  print(fruit_list[i])

print_name(1)
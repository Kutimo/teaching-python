""" 
count = 1
while True:
  count + 1
  print(count)
 """""" 
count = 3
while count <= 3:
  print(f"The count is: {count}")
  count += 1 """


""" while True:
  text = input("Skriv stopp for avslutte while løkken: ")
  if text == "stop":
    print("stopper programmet")
    break
 """

while True:
    text = input("Type 'stop' to quit: ")
    if text != "stop":
        print("tekst er ikke lik")
        continue
    break
print("Loop ended.")
    

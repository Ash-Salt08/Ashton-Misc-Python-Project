character_name = "Johnny"
character_age = "70"
name_his = []
name_his.append(character_name)

print("Your name is " + character_name + ",")
print("and you are " + character_age + " years old.")
print("Your name is " + str(len(character_name)) +" characters long.")

character_name = input("What is your actual name?\n")
character_age = input("How old are you really?\n")
name_his.append(character_name)

print("Your name is now " + character_name + ",")
print("and you are now " + character_age + " years old.")
print("Your name is now " + str(len(character_name)) +" characters long.")

how_many_years = input("We will calculate your future age. How many years from now should it be?\n")
result = int(how_many_years) + int(character_age)

print("You will be " + str(result) + " years old in " + str(how_many_years) + " years.")

print("Your previous names have included " + str(name_his[0:-1]) + " and " str(name_his[-1]))

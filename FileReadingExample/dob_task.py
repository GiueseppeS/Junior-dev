with open('DOB.txt', 'r+', encoding='utf-8') as file:  ##Struggle a little bit because I forgot to add the file on the project folder
    lines = file.read().splitlines() #reading from file and splitting the lines to create a list 

#declaring variables of type list in order to create a list of names and birthdates
names = [] 
dates = []
#looping the lines, splitting the single words in order to join them thanks to the same index for every line
for line in lines:
    words = line.split()
    names.append(' '.join(words[:2]))
    dates.append(' '.join(words[2:]))


#looping and printing the names and dates
print("Name")
for name in names:
    print(name)

print("Birthdate")
for date in dates:
    print(date)
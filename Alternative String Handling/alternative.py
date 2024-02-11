"""Alternative string assignment"""

def user_input():
    """Reading user input and returning the value"""
    return str(input("Insert the string to modify: "))

def alternative_letters(phrase):
    """Function alternating the char inside a phrase lowercase to uppercase and viceversa"""
    #looping through the phrase in order swap the lower and upper case
    for index, char in enumerate(phrase):
        if char == " ":
            string_list.append(" ")
        if index % 2 == 0:
            string_list.append(char.upper())
        else:
            string_list.append(char.lower())

    #Small note, I missunderstood the task, I thought that I had to alternate upper with lower cases

    #Creating a new list to return
    new_list_joined = "".join(string_list)
    return new_list_joined


def alternative_words(phrase):
    """Converting each words in pattern lowercase/uppercase"""

    #Splitting the phrase in a list of single phrase
    words_list = phrase.split()
    new_word_list = []

    #Looping through the list in order to append the new word based on the index
    index = 0
    while index < len(words_list):
        #Checking the result of the module operation in order to get the even or uneven position
        if index % 2 == 0:
            new_word_list.append(words_list[index].lower() + " ")
        else: new_word_list.append(words_list[index].upper() + " ")
        index += 1
    list_joined = "".join(new_word_list)
    return list_joined


#Handling input
STRING = user_input()
string_list = []
LIST_JOINED = ""


#Calling the first function
LIST_JOINED = alternative_letters(STRING)
print(" \n \n Firt Task")
print(LIST_JOINED)


#Calling the second function
LIST_JOINED = alternative_words(STRING)
print(" \n \n Second Task")
print(LIST_JOINED)

import pandas

#Loop through rows of a data frame
#
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

file = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code = {}

for (index, row) in file.iterrows():
    letter_code[row.letter] = row.code

print(letter_code)




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonatic():
    name = input("Enter a word:\n").upper()
    try:
        name_codes = {letter:letter_code[letter] for letter in name}
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonatic()
    else:
        KeyError == False
        print(name_codes)

generate_phonatic()
# for items in list_of_user_letters:
#     print(letter_code[items])
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index,row)  in data.iterrows()}

# print(phonetic_dict)


ask = True
while ask:
    word = input("enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError: 
        print("Sorry, only letters in the alphabet please.")
    else: 
        print(output_list)
        ask = False
        
# or 

# def generate_phonetic():
#     word = input("enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError: 
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else: 
#         print(output_list)

# generate_phonetic()
        
    







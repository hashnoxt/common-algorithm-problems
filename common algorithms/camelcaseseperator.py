string_to_decode = input('Enter camel case string to seperate: ')

have_more_items : int = 1

all_words : list = []

while have_more_items:

    index_list : list = [0]

    for letter_index in range(len(string_to_decode)):
        if string_to_decode[letter_index].isupper():
            index_list.append(letter_index)
    
    for item_index in range(len(index_list) -1):
        print(string_to_decode[index_list[item_index] : index_list[item_index + 1]])

    have_more_items = 0


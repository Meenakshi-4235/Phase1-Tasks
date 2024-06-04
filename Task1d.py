def remove_common_chars(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)

    for char in name1:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)

    return ''.join(name1_list), ''.join(name2_list)

def count_remaining_chars(name1, name2):
    name1, name2 = remove_common_chars(name1, name2)
    return len(name1 + name2)

def flames_game(name1, name2):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    name1 = name1.lower().replace(' ', '')
    name2 = name2.lower().replace(' ', '')
    
    count = count_remaining_chars(name1, name2)

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]

def flames_meaning(letter):
    meanings = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    return meanings[letter]

# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate FLAMES result
result = flames_game(name1, name2)

# Get the meaning of the result
result_meaning = flames_meaning(result)

print(f"The relationship between {name1} and {name2} is: {result_meaning}")

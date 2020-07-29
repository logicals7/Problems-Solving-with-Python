in_str = input()
for char in in_str:
    if char in 'aeiou':
        print('vowel')
    elif char not in 'abcdefghiojklmnopqrstuvwxyz':
        break
    else:
        print('consonant')
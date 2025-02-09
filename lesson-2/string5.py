vowels="aeiouAEIOU"
given = input("Enter a string: ")

num_vowels = given.count("e")+given.count("u")+given.count("i")+given.count('o')+given.count('a')+given.count('A')+given.count('U')+given.count('E')+given.count('I')+given.count('O')
print(num_vowels)

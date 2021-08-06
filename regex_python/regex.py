import re

# result = re.search(r"aza", "plaza")
# print(result)

print(re.search(r"p.ng", "penguin"))


# Look for the string 'way' preceded by any character

print(re.search(r"[a-z]way", "The end of the highway"))

# Combine as many ranges and symbols as you want

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloudy[a-zA-Z0-9]", "cloud1ZA"))

# Look for a character that's not a letter

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

# Match either one expression or another
# Search will return the first result

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like both dogs and cats."))

# To find all possible matches, Findall Function

print(re.findall(r"cat|dog", "I like both cats and dogs"))

# Repetition Qualifiers

# Match Py followed by any number of chars followed by n
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))

# + and ?

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# The repeating_letter_a function checks if the text passed includes the 
# letter "a" (lowercase or uppercase) at least twice. For example, 
# repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") 
# is False. Fill in the code to make this work. 

import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# ? Means either zero or one occurance of the character before it
# ? Makes P optional
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))


# Escaping Characters "\"
# When we see a pattern that includes a backslash,
# it could be escaping a special regex character or 
# a special string character

print(re.search(r"\.com", "welcome.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))


# Fill in the code to check if the text passed has at least 2 groups
# of alphanumeric characters (including letters, numbers, and underscores)
# separated by one or more whitespace characters

# import re

def check_character_groups(text):
    result = re.search(r"[0-9]\w", text)
    return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


# Fill in the code to check if the text passed looks like a standard sentence,
# meaning that it starts with an uppercase letter, followed by at least some 
# lowercase letters or a space, and ends with a period, question mark, or 
# exclamation point. 

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][ |a-z]*[.?\!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
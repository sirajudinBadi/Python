import re

s = "abc123"

# print(re.search("123", s)) # If found then it will be truthy value else None which is falsey


# -=-==-=-=-=-======================================= META CHARACTERS========================================

# 1. [] -> This makes a CHARACTER CLASS --------------------------------------------------------------------------
# To search for 3 continuous digit in the string
# print(re.search("[0-9][0-9][0-9]", s))

# 2. DOT (.) -> Matches any character except new line. (like WILDCARD)
# print(re.search("a.k", s))

# 3. ^ CARET 
# ^ At the begining of the pattern
# print(re.search("^foo", s)) # To check if string begins with that character or not.

# Inside character class will negate the character class
# print(re.findall("[^0-9]", s)) # Negates the character class digits and give rest characters
# print(re.findall("[^aeiou]", "oiasgl;kan;o2h3klnasl;dgnka;hsg"))
# print(re.search("[^aeiou]", "oiasgl;kan;o2h3klnasl;dgnka;hsg")) # search for the first character that is not a lower vovel

# 4. $ => If ends with 
print(re.search("\.pdf$", "index.pdf"))
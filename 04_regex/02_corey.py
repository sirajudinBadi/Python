import re

text_to_serach = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Metacharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*431*2344

Mr. Sirajudin
Mr Smith
Ms Dacey
Mrs. Robinson
Mr. Praful
Mr T

userAdmin@gmail.com
example.User.Dev@university.edu
Dummy-User-IM@my-work.net
"""

# pattern = re.compile(r"Mr\.?\s[A-Z]\w*")
# pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")

# pattern = re.compile(r"[a-zA-Z.-]+@[a-zA-Z-]+\.(com|edu|net)")
# matches = pattern.finditer(text_to_serach)

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))
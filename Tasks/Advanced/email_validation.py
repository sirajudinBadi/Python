import re

def fun(s):
    pattern = re.compile(r"^[A-Za-z0-9_\-]+@[A-Za-z0-9]+\.[a-zA-Z]{0,3}$")
    match = pattern.search(s)
    if match:
        return True
    return False

def filter_emails(emails):
    email_list = emails.strip().splitlines()
    filtered = list(filter(lambda x : fun(x), email_list))
    return filtered

raw_emails = """
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
user-admin@gmail.commerce
userase2343.234-@email_me.comme2365
"""
print(filter_emails(raw_emails))

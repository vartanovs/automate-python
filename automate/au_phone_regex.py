# This program finds phone and e-mail patterns in a string
import re, pyperclip

# Create a regex object for phone numbers
phone_regex = re.compile(r'''
# 111-111-1111, 111-1111, (111) 111-1111, ext 1234, ext. 1234, x1234
(
((\d\d\d)|(\(\d\d\d\)))?  # area code (optional)
(\s|-)                    # first separator (- or space)
(\d\d\d)                  # first 3 digits
-                         # second separator
(\d\d\d\d)                # last 4 digits
(((ext(\.)?\s?)|x)        # extension word (optional)
(\d{2,5}))?               # extension num (optional)
)
''', re.VERBOSE)

# Create a regex object for email addresses
email_regex = re.compile(r'''
# abc._def@ghi.jkl
[a-zA-Z0-9_.+]+   # name part
@                 # @ symbol
[a-zA-Z0-9_.+]+   # domain name

''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste()

# Extract the email and phone number
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

# Append first tuple value (group 0, full phoen number) to a list
all_numbers = []
for phone_number in extracted_phone:
  all_numbers.append(phone_number[0])

# Generate a string that has all phone numbers and emails on their own line
results = '\n'.join(all_numbers) + '\n' + '\n'.join(extracted_email)

# TODO: Copy extracted data to the clipboard
pyperclip.copy(results)

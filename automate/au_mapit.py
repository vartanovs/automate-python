# Module that opens Google Maps, searching for the address passed in the command line

import webbrowser, sys, pyperclip

# Check if command line arguments were passed
if len(sys.argv) > 1:
  # Combine all arguments into a single address string
  address = ' '.join(sys.argv[1:])
else:
  # If no command line argument, assume address is on the clipboard
  address = pyperclip.paste()

# Open Google Maps with the address passed in
url = 'https://www.google.com/maps/place/' + address
webbrowser.open(url)

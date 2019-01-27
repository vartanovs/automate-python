from selenium import webdriver

# Generate a Selenium Chrome Driver and visit automatetheboringstuff.com
browser = webdriver.Chrome('/Users/sergeyvartanov/Code/udemy/automate-python/chromedriver')
browser.get('https://www.automatetheboringstuff.com')

# Identify and print the page's title
title = browser.title
print(f'We\'re on the "{title}" page.')

# Count the number of 'li' tags on the page
elems = browser.find_elements_by_css_selector('li')
print(f'There are {len(elems)} "li" tags on this page')

# Find the image that links to Amazon and click it
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(4) > center > a > img')
alt_tag = elem.get_attribute('alt')
print(f'We\'re about to click the "{alt_tag}" image.')
elem.click()

# Identify and print the Amazon page title
title = browser.title
print(f'Now we\'re on the "{title}" page.')

# Count the number of 'li' tags on the page
elems = browser.find_elements_by_css_selector('li')
print(f'There are {len(elems)} "li" tags on this page')
print('We\'re about to go back one page')

# Go back one page, identify and print the page's title
browser.back()
title = browser.title
print(f'Now we\'re back on the "{title}" page.')

# Count the number of 'li' tags on the page
elems = browser.find_elements_by_css_selector('li')
print(f'Again, there are {len(elems)} "li" tags on this page')

# Close the browser
browser.quit()

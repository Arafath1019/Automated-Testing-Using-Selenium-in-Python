# importing webdriver from selenium
from selenium import webdriver

example_url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

# Loading chromedriver.exe as chrome_browser
chrome_browser = webdriver.Chrome('./chromedriver.exe')

# Opening the session as maximize_window
chrome_browser.maximize_window()

# get the demo url for our playground
chrome_browser.get(example_url)

# checking whether our demo site title contains "Selenium Easy Demo" part, if not then raise an error will show us in our log and pause our next work

assert "Selenium Easy Demo" in chrome_browser.title


# In this section, we will try to fill up a from by automated testing using selenium

# selecting the message showing button

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

# selecting the input field which is used for user to write their message

user_message = chrome_browser.find_element_by_id('user-message')

# clear the input field

user_message.clear()

# setting up the message

user_message.send_keys('HELLOOOOO! LONG TIME NO SEE MY BOYS')

# Clicking the button for the output

show_message_button.click()
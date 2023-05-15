from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()
email = "hicker.coder.2023@gmail.com"
password = "VARisBS2018*"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/amine-lahouani-5220881a0/", driver=driver)



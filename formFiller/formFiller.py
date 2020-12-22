# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Access website via Chrome driver
web = webdriver.Chrome()
web.get('https://careers.twitter.com/en/work-for-twitter/202008/86f2d6ff-3da3-4543-995e-b4570f0b3076/30d62be6-f857-4d06-b244-a8b00706cdc4.html/software-engineer-systems-health-machine-learning-infrastructure.html')


#  Upoad resume
element = web.find_element_by_xpath('//*[@id="twtr-main"]/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[1]/div[1]/label/div/div/div/div[2]/div/input').send_keys("/Users/johnduva/Desktop/Resume_Duva_1220.pdf")


# Deny pop-up request
# obj = web.switch_to.alert
# msg = obj.text
# print(msg)

# button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div/button[1]')
# button.click()




# web.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div/button[1]/span').click("Yes")

# web.switch_to_alert().dismiss()

#  Fill in personal info
firstName = "John"
first = web.find_element_by_xpath('//*[@id="twtr-main"]/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[1]/div[3]/label/input')
first.send_keys(firstName)

lastName = "D'Uva"
last = web.find_element_by_xpath('//*[@id="twtr-main"]/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[1]/div[4]/label/input')
last.send_keys(lastName)

email = "jduva4@jhu.edu"
email2 = web.find_element_by_xpath('//*[@id="twtr-main"]/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[1]/div[5]/label/input')
email2.send_keys(email)

phone = "3055099415"
phone2 = web.find_element_by_xpath('//*[@id="twtr-main"]/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[1]/div[6]/label/input')
phone2.send_keys(phone)

element = web.find_element_by_xpath('/html/body/div/main/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[1]/div[7]/label/fieldset/select')
country = Select(element)
country.select_by_value("US")

prevTwit = Select(web.find_element_by_xpath('//*[@id="twtr-main"]/div/div/div[6]/div/div/div/div/div/div/div[1]/form/div[2]/div[1]/label/fieldset/select'))
prevTwit.select_by_visible_text("No")
#!/usr/bin/env python
# coding: utf-8

'''This is a simple python script to upload any number of images to twitter with a single Tweet Text
To use this script you can put all the images in a single folder and provide its path to the variable
image_path. The script will get the name of all images provided in the folder and creates a list of
them. You need to provide your username and password of your twitter account for login. Everything is
secure as nothing never goes out of your system. Once logged in one by one images will be uploaded

@Author: Varun Tyagi
@github: https://github.com/tyagivarun01'''

# Importing necessary libraries
from os import listdir
from os.path import isfile, join
import autoit
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

# Defining a variable to store the path of images directory
image_path = ""
only_files = [f for f in listdir(image_path) if isfile(join(image_path, f))]
only_files

print("Number of images to be uploaded",len(only_files))

#Defining a variable to store the path of chromedriver executable file. You can download driver as per Chrome version
chrome_driver = "chromedriver.exe"

#Initializing a webdriver object using Chrome driver and opening a new browser window.
#On my machine driver path wasn't required.
driver = webdriver.Chrome()

#Defining a constant to store URL of Twitter website
url_twitter = "https://www.twitter.com/"

'''Defining variables to store selectors for login button, username input field, password input field, 
upload button, tweet post button, caption text box, and hashtags string respectively'''

login_button = "//a[@href='/login']"
login_username = "//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']"
enter_username_button = "(//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-usiww2 r-13qz1uu r-2yi16 r-1qi8awa r-ymttw5 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l'])[1]"
enter_password_button = "//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1dye5f7 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']"
upload_button = "(//div[@aria-label='Add photos or video'])[1]"
input_field = "//input[@type='password']"
post_tweet = "//a[@href='/compose/tweet']"
write_caption = "//div[@aria-label='Post text']"
post_finally = "//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19u6a5r r-2yi16 r-1qi8awa r-ymttw5 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']"

# You can put the tweet text but dont remove the ending \n for the post button to be visible to webdriver
hastags = "Tweet Text"+"  \n"

# Defining variables to store login credentials
username = ""
password = ""

def sleep_in_seconds(time_in_seconds):
    """Pauses the execution of a script or program for a specified amount of time."""
    print("Sleeping for %2d seconds" % (time_in_seconds))
    time.sleep(time_in_seconds)

driver.maximize_window()
driver.get(url_twitter)
sleep_in_seconds(5)

driver.find_element(By.XPATH, login_button).click()
sleep_in_seconds(5)

driver.find_element(By.XPATH, login_username).send_keys(username)
sleep_in_seconds(3)

driver.find_element(By.XPATH, enter_username_button).click()
sleep_in_seconds(5)

driver.find_element(By.XPATH, input_field).send_keys(password)
sleep_in_seconds(3)

driver.find_element(By.XPATH, enter_password_button).click()
sleep_in_seconds(10)

for image in only_files:
    print("Uploading the image: ", image)

    driver.find_element(By.XPATH, post_tweet).click()
    sleep_in_seconds(5)

    driver.find_element(By.XPATH, upload_button).click()
    sleep_in_seconds(3)

    autoit.win_active("Open")
    sleep_in_seconds(3)

    autoit.control_send("Open","Edit1",image_path+'\\'+ image)
    sleep_in_seconds(3)

    autoit.control_send("Open","Edit1","{ENTER}")
    sleep_in_seconds(5)

    driver.find_element(By.XPATH, write_caption).send_keys(hastags)
    sleep_in_seconds(3)

    driver.find_element(By.XPATH, post_finally).click()
    sleep_in_seconds(6)
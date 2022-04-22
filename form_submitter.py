#Indebted thanks for guidance from: 
#https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e

#Form Submitter
#Reads a csv, populates data into a web form, and submits data

#Currently configured for humboldtgov but could be modified for other
#sites with minimal change


#Load python libraries (this has not been optimized for the current code, 
#Hence, some libraries are likely unnecessary)
from selenium import webdriver
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import numpy as np
import pandas as pd


#Send the keys to the webform
#Variables configured for current humboldtgov site
def answerForm(driver, df, element_class, user_id):

    
    #Modify here for a different site or if form changes
    data_field= df["data_field"][user_id]
    department= df["department"][user_id]
    email= df["email"][user_id]
    name = df["your_name"][user_id] #"name" on humboldtgov, "your_name" on test form
    phone=df["phone"][user_id]
    address=df["address"][user_id]
    city= df["city"][user_id]
    state= df["state"][user_id]
    zip= df["zip"][user_id]
    company= df["company"][user_id]

    text_answers = [data_field, department, email, name, phone, address, city, state, zip, company]

    text_questions = driver.find_elements_by_class_name(element_class)
    for a,q in zip(text_answers,text_questions):
        q.send_keys(a)
    
    return driver

#Click the submit button 
def click_submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver



#Load variables for humboldtgov and get website
url = "https://humboldtgov.nextrequest.com/requests/new"  # Change this to fill out a different form
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)


df = pd.read_csv("./submission_form_database.csv")
text_question_element_class = ""
checkbox_question_element_class = ""
submit_element_class = ''

for user_id in range(len(df)):
    driver.get(url)
    
    driver.maximize_window()
    driver = answerNameAge(driver, df, text_question_element_class, user_id)
    driver = answerCheckBox(driver, df, checkbox_question_element_class, user_id)
    driver = submit(driver, submit_element_class)
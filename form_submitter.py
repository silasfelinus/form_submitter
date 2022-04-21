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


#declare form variables and populate with filler data
data_field="description"
data_field.element = "ql-editor ql-blank"
department="null"
department.element="NrSelect-2"
email="test@test.com"
email.element="nr_form_input-3"
name="Fake Name"
name.element = "nr_form_input-4"
phone= "111-111-1111"
phone.element="nr_form_input-5"
address="111 Home st."
address.element="nr_form_input-6"
city= "Eureka"
city.element="nr_form_input-7"
state= "CA"
state.element="nr_form_select-8"
zip="11111"
zip.element="nr_form_input-9"
company= "THC"
company.element="nr_form_input-10"
button_element="nr-button_label"
button_xpath="/html/body/div[2]/main/section/div/div[1]/form/div[3]/button/span"


#save info as csv file
database = pd.DataFrame(dict(data_field=data_field, department=department, email = email, name=name, phone=phone, address=address, city=city, state=state, zip=zip, company=company))
database.to_csv("submission_form_database.csv", index=False)
database.head()

url = "https://humboldtgov.nextrequest.com/requests/new"
driver = webdriver.Chrome(executable_path="./chromedriver")


def answerForm(driver, df, element_class, user_id):
    data_field= df["data_field"][user_id]
    department= df["department"][user_id]
    email= df["email"][user_id]
    name = df["name"][user_id]
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
#Form Submitter
#THC Humboldt
#Reads a csv, populates data into a web form, and submits data

#Load python libraries
from selenium import webdriver
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import numpy as np
import csv
sys.path.append("./plugins")

intro = "This request is being made by the Transparent Humboldt Coalition, a co-operative organization of citizens dedicated to anti-corruption activism through radical transparency.\nWe are passing along the following request:"
polite_sendoff="Thank you for your assistance in expediting this request. You efficient cooperation is heavily supported by law and helps make a cleaner, less corrupt world."
request = ""
department= ""
email = "requester@transparencyhumboldtcoalition.org"
phone= "111-111-1111"
address= "111 Fake Address"
city= "Eureka"
zip= "95501"
company= "Transparent Humboldt Coalition"



#Read CSV
with open('formData.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in reader:
    request = row[0]
    department = row[1]

#Stitch together request
final_request = "Attn: " + department + "\n" + intro + "\n" + request + "\n" + polite_sendoff





#populate webform
url = "https://fakeform.acrocatranch.com"
ChromeOptions options = new ChromeOptions();
options.addExtensions(new File("/chromedriver/chromedriver.exe"));
ChromeDriver driver = new ChromeDriver(options);



#Click the Submit Button 
def click_submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


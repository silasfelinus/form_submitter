#Form Submitter
#THC Humboldt
#Reads a csv, populates data into a web form, and submits data

#Load python libraries
import csv
import time
from selenium import webdriver

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

#For Testing
print("Attn: " + department)
print(intro + "\n")
print(request + "\n")
print(polite_sendoff + "\n")
print(company)
print(email)
print(phone)
print(address)
print(city)
print(zip)


#populate webform
url = "https://fakeform.acrocatranch.com"
driver = webdriver.Chrome(executable_path="./chromedriver")


#Click the Submit Button 
def click_submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


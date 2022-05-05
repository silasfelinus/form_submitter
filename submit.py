#Form Submitter
#THC Humboldt
#Reads a csv, populates data into a web form, and submits the data

#troubleshooting: insert the following (uncommented) to pause code
#import pdb; pdb.set_trace()

#Load python libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pathlib
import csv
import sys
sys.path.append(".")
sys.path.append("./plugins")
sys.path.append("./chromedriver")

def launchChrome():
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-gpu")
  chrome_options.add_argument("--disable-dev-shm-usage")
  driver = webdriver.Chrome(options=chrome_options)
  return driver

driver = launchChrome()


def loadURL(driver, url):
  print('Loading webpage from ' + url)
  driver.get(url)
  print("Webpage " + url + " loaded!")
  return driver

def readRealForm(driver):
  url="https://humboldtgov.nextrequest.com/requests/new"
  driver = loadURL(driver, url)
  print(driver.find_element(by=By.CLASS_NAME, value='ql-editor'))       #request
  print(driver.find_element(by=By.ID, value='NrSelect-2'))              #department
  print(driver.find_element(by=By.ID, value='nr_form_input-3'))         #email
  print(driver.find_element(by=By.ID, value='nr_form_input-4'))         #name
  print(driver.find_element(by=By.ID, value='nr_form_input-5'))         #phone
  print(driver.find_element(by=By.ID, value='nr_form_input-6'))         #address
  print(driver.find_element(by=By.ID, value='nr_form_input-7'))         #city
  print(driver.find_element(by=By.ID, value='nr_form_select-8'))        #state
  print(driver.find_element(by=By.ID, value='nr_form_input-9'))         #zip
  print(driver.find_element(by=By.ID, value='nr_form_input-10'))        #company
  print("all elements found! " + url + " should populate!")
  return driver


def readFakeForm(driver):
  url="https://www.acrocatranch.com/"
  driver = loadURL(driver, url)
  print(driver.find_element(by=By.NAME, value='description'))    #request
  print(driver.find_element(by=By.NAME, value='NrSelect-2'))    #department
  print(driver.find_element(by=By.NAME, value='nr_form_input-3'))         #email
  print(driver.find_element(by=By.NAME, value='nr_form_input-4'))          #name
  print(driver.find_element(by=By.NAME, value='nr_form_input-5'))         #phone
  print(driver.find_element(by=By.NAME, value='nr_form_input-6'))       #address
  print(driver.find_element(by=By.NAME, value='nr_form_input-7'))          #city
  print(driver.find_element(by=By.NAME, value='nr_form_select-8'))         #state
  print(driver.find_element(by=By.NAME, value='nr_form_input-9'))           #zip
  print(driver.find_element(by=By.NAME, value='nr_form_input-10'))       #company
  print("all elements found! " + url + " should populate!")
  return driver



#run tests
#readFakeForm(driver)
#readRealForm(driver)

intro = "This request is being made by the Transparent Humboldt Coalition, a co-operative organization of citizens dedicated to anti-corruption activism through radical transparency.\nWe are passing along the following request:"
polite_sendoff="Thank you for your assistance in expediting this request. You efficient cooperation is heavily supported by law and helps make a cleaner, less corrupt world."
request = ""
department= ""
email = "requester@transparencyhumboldtcoalition.org"
name= "Transparent Humboldt Coalition"
phone= "111-111-1111"
address= "111 Fake Address"
city= "Eureka"
state = "CA"
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

url="https://www.acrocatranch.com/"
driver = loadURL(driver, url)

def updateElement(element_value, element_name, driver):
  driver.find_element(by=By.NAME, value=element_value).send_keys(element_name)
  return driver
  
def checkElement(element_value, element_name, driver):
  if driver.find_element(by=By.NAME, value=element_value).key == element_name:
    return print("It matches! " + driver.find_element(by=By.NAME, value=element_value).key + " equals " + element_name)
  else:
    return print("Failure! " + driver.find_element(by=By.NAME, value=element_value).key + " doesn't equal " + element_name)

  
def updateElements(driver):
  driver = updateElement('description', final_request, driver)
  driver = updateElement('NrSelect-2', department, driver)
  driver = updateElement('nr_form_input-3', email, driver)
  driver = updateElement('nr_form_input-4', name, driver)
  driver = updateElement('nr_form_input-5', phone, driver)
  driver = updateElement('nr_form_input-6', address, driver)
  driver = updateElement('nr_form_input-7', city, driver)
  driver = updateElement('nr_form_select-8', state, driver)
  driver = updateElement('nr_form_input-9', zip, driver)
  driver = updateElement('nr_form_input-10', company, driver)
  return driver

def checkElements(driver):
  driver = checkElement('description', final_request, driver)
  driver = checkElement('NrSelect-2', department, driver)
  driver = checkElement('nr_form_input-3', email, driver)
  driver = checkElement('nr_form_input-4', name, driver)
  driver = checkElement('nr_form_input-5', phone, driver)
  driver = checkElement('nr_form_input-6', address, driver)
  driver = checkElement('nr_form_input-7', city, driver)
  driver = checkElement('nr_form_select-8', state, driver)
  driver = checkElement('nr_form_input-9', zip, driver)
  driver = checkElement('nr_form_input-10', company, driver)
  return driver


driver = updateElements(driver)
#driver = checkElements(driver)
driver.find_element(by=By.NAME, value='nr_form_input-10').submit()
readFakeForm(driver)
print("Did this work?")


def click_submit(driver, element_class):
  driver.find_element_by_xpath(element_class).click()
  return driver


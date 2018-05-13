import argparse
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Setting up cli
parser = argparse.ArgumentParser()
parser.add_argument("url", help="page url")
parser.add_argument("file", help="name of source file")
parser.add_argument("-s", "--sheet", type=int, default = 0, help="sheet index, default 0" )
args = parser.parse_args()

driver = webdriver.Chrome() # Open browser
driver.get(args.url) # Open given page

# read excel file to dataframe
df = pd.read_excel(args.file, sheet_name = args.sheet)

# loop over dataframe rows and fill values to text boxes
for index, row in df.iterrows():
    id = "id_" + str(row[0]) + str(row[2])
    try:
        element = driver.find_element_by_id(id)
        element.clear()
        element.send_keys(row[1])
    except NoSuchElementException:
        print("WARN: element with id: " + id + " not found")

# find save button and click it
try:
    save = driver.find_element_by_id("Tallenna") # true id?
    element.click()
except:
    print("WARN: save button not found")

# close opened Chrome window
driver.quit()
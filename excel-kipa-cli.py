import argparse
from selenium import webdriver
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

labels = df.columns.tolist()
# loop over dataframe rows and fill values to text boxes
for index, row in df.iterrows():
    # loop over dataframe value columns (2nd->)
    for i in range(1,len(labels)):
        # parse id from team and label numbers
        id = "id_" + str(row[0]) + "_" + str(labels[i]) + "-arvo"
        try:
            element = driver.find_element_by_id(id)
            element.clear()
            element.send_keys(str(row[i]))
        except NoSuchElementException:
            print("WARN: element with id: " + id + " not found")

# find save button and click it
try:
    save = driver.find_element_by_name("tallenna") # no id
    save.click()
    driver.quit() #close browser window
except:
    print("WARN: save button not found")
    # if saving fails, browser window is not closed
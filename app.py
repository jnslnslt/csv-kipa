from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd

driver = webdriver.Chrome()

driver.get('http://10.0.0.4/kipa/LLHK18/syota/tehtava/139/')

df = pd.read_excel('TESTI.xlsx', sheet_name = 'Taul1')

for index, row in df.iterrows():
    id = "id_" + str(row['vartio']) + str(row['tag'])
    element = driver.find_element_by_id(id)
    element.clear()
    element.send_keys(row['tulos'])
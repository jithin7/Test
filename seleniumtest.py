from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.flightradar24.com/data/airports/pnq")
myElem = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ot-sdk-row')))
button = myElem.find_element(By.ID,"onetrust-accept-btn-handler")
button.click()

table = driver.find_element(By.XPATH,"(//table[@class='table table-condensed table-hover data-table m-n-t-15'])[1]")

rows = table.find_elements(By.XPATH,".//tr[@class='hidden-xs hidden-sm ng-scope']")

a = ["Delhi","Allahabad","Goa"]

for row in rows:
    input = row.find_element(By.XPATH,".//td//div//span")
    place = input.text
    if place in a:
        output = row.find_element(By.XPATH,".//td[last()]")
        print(output.text)
    print(place)


driver.quit()



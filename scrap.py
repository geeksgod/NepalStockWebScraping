from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get("https://nepalstock.com.np/floor-sheet")
select = Select(driver.find_element(By.XPATH,"//span[contains(text(),'Items Per Page')]/../select"))
select.select_by_value('500')

driver.find_element(By.XPATH,"//button[contains(text(),'Filter')]").click()
time.sleep(2)
nextBtn = driver.find_element(By.XPATH,"//a[contains(text(),'Next')]")
i = 0
while(1):
    table = driver.find_element(By.XPATH,"(//table)[1]")
    rows = table.find_elements(By.TAG_NAME, "tr")
    table_data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        cols_data = [col.text for col in cols]
        table_data.append(cols_data)

    if(nextBtn.is_enabled() and nextBtn.is_displayed()):       
        nextBtn.click()    
        i=i+1
        print(i)
        time.sleep(1)
    else :
        break
    



# Step 5: Convert to a Pandas DataFrame
df = pd.DataFrame(table_data)

# Step 6: Export the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

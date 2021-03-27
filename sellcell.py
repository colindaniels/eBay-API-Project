
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
model_list = ['iphone-6', 'iphone-6-plus', 'iphone-6s', 'iphone-6s-plus', 'iphone-7', 'iphone-7-plus', 'iphone-8', 'iphone-8-plus', 'iphone-se-2020', 'iphone-x', 'iphone-xr', 'iphone-xs', 'iphone-xs-max', 'iphone-11', 'iphone-11-pro', 'iphone-11-pro-max', 'iphone-12', 'iphone-12-mini', 'iphone-12-pro', 'iphone-12-pro-max']


#options = Options()
#options.add_argument("--headless")
#options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(executable_path='/Users/colindaniels/eBay-API-Project/chromedriver')


all_models = []
for model in model_list:
    driver.get(f'https://www.sellcell.com/phones/apple-{model}/')
    for capacity in driver.find_elements_by_class_name('capacity-logos-sprite'):
        for carrier in driver.find_elements_by_class_name('network-logos-sprite'):
            for condition in driver.find_elements_by_class_name('condition'):
                time.sleep(3)
                capacity.click()
                time.sleep(3)
                carrier.click()
                time.sleep(3)
                condition.click()
                time.sleep(3)
                capacity_name = capacity.find_element_by_name('capacity').get_attribute('data-attribute')
                carrier_name = carrier.find_element_by_name('network').get_attribute('data-attribute')
                price = driver.find_elements_by_class_name('price')[1].text
                condition_name = condition.find_element_by_name('condition').get_attribute('value')
                all_models.append((capacity_name, carrier_name, condition_name, price))
                print((model, capacity_name, carrier_name, condition_name, price))

                time.sleep(5)
print(all_models)
time.sleep(10)
driver.quit()

with open('sellcell.csv', 'w') as file:
    file.write('model,storage,carrier,condition,price\n')
    writer = csv.writer(file)
    for model, storage, carrier, condition, price in all_models:
        writer.writerow((model, storage, carrier, condition, price))

    file.close()

#chrome_options.add_argument("--headless")
#driver = webdriver.Chrome(executable_path='/Users/colindaniels/eBay-API-Project/chromedriver', options=chrome_options)

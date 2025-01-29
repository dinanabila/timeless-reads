from selenium import webdriver
from selenium.webdriver.common.by import By

# ini biar pop up chrome browser nya tetep kebuka terus
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.goodreads.com/list/show/264?ref=ls_pl_car_1")


book_link = driver.find_element(By.XPATH, value='//*[@id="all_votes"]/table/tbody/tr[1]/td[3]/a/span')
print(book_link.text)
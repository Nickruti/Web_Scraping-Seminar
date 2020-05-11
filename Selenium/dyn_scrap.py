from ask_user import *
from selenium import webdriver 
opts = webdriver.ChromeOptions()
opts.headless =True
driver = webdriver.Chrome(executable_path= r"D:\PythonL\Learning\Webscraper\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://www.jiosaavn.com/')
search_form = driver.find_element_by_id('search')
search_form.send_keys(x)
driver.find_element_by_name("q").send_keys(u'\ue007')
driver.find_elements_by_class_name('search-ellip-contain')[0].find_elements_by_tag_name('a')[0].click()
driver.find_element_by_xpath('//*[@id="main"]/div/section/div/div[2]/div/div/button').click()

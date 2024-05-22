# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# set driver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/")

# functions
def test1():
    elementOne = driver.find_element(By.ID, value="element-one")
    ActionChains(driver).double_click(elementOne).perform()

def test2():
    elementTwo = driver.find_element(By.ID, value="element-two")
    elementTwo.click()
    # ActionChains(driver).move_to_element(elementTwo).perform()

def test3():
    elementThree = driver.find_element(By.ID, value="element-three")
    elementThree.click()

def test4():
    elementFour = driver.find_element(By.ID, value="element-four")
    ActionChains(driver).move_to_element(elementFour).perform()
    driver.save_screenshot("test5.png")
    elementFour.click()
    

# test1: dupla kattintás után szerepel-e az "animation" class
test1()
time.sleep(1)
driver.save_screenshot("test1.png")
# ha rámegy az egér, utána létezik-e box-shadow
test2()
driver.save_screenshot("test2.png")
time.sleep(1)
# kattintás után eltűnik-e
test3()
driver.save_screenshot("test3.png")
time.sleep(1)

# kattintás után a háttere zöld lesz-e
test4()
driver.save_screenshot("test4.png")
time.sleep(1)

# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
#test5()

driver.quit()
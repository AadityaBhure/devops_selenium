from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("D:\\codefiles\\dev\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

def setup():
    driver = webdriver.Chrome(service=service)
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)
    return driver


#  Test 1: Valid Registration
def test_valid():
    driver = setup()

    driver.find_element(By.ID, "name").send_keys("Aaditya")
    driver.find_element(By.ID, "age").send_keys("21")
    driver.find_element(By.ID, "gender").send_keys("Male")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")
    driver.find_element(By.ID, "address").send_keys("Pune, India")
    driver.find_element(By.ID, "password").send_keys("123456")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    assert "Registration successful" in driver.page_source
    print(" Valid Registration Passed")

    driver.quit()


#  Test 2: Age below 18
def test_invalid_age():
    driver = setup()

    driver.find_element(By.ID, "name").send_keys("Aaditya")
    driver.find_element(By.ID, "age").send_keys("15")
    driver.find_element(By.ID, "gender").send_keys("Male")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")
    driver.find_element(By.ID, "address").send_keys("Pune")
    driver.find_element(By.ID, "password").send_keys("123456")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    assert "Age must be 18+" in driver.page_source
    print(" Invalid Age Test Passed")

    driver.quit()


#  Test 3: Invalid Phone
def test_invalid_phone():
    driver = setup()

    driver.find_element(By.ID, "name").send_keys("Aaditya")
    driver.find_element(By.ID, "age").send_keys("21")
    driver.find_element(By.ID, "gender").send_keys("Male")
    driver.find_element(By.ID, "phone").send_keys("123")
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")
    driver.find_element(By.ID, "address").send_keys("Pune")
    driver.find_element(By.ID, "password").send_keys("123456")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    assert "Invalid phone number" in driver.page_source
    print(" Invalid Phone Test Passed")

    driver.quit()


#  Test 4: Weak Password
def test_weak_password():
    driver = setup()

    driver.find_element(By.ID, "name").send_keys("Aaditya")
    driver.find_element(By.ID, "age").send_keys("21")
    driver.find_element(By.ID, "gender").send_keys("Male")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")
    driver.find_element(By.ID, "address").send_keys("Pune")
    driver.find_element(By.ID, "password").send_keys("123")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    assert "Password must be at least 6 characters" in driver.page_source
    print(" Weak Password Test Passed")

    driver.quit()


if __name__ == "__main__":
    test_valid()
    test_invalid_age()
    test_invalid_phone()
    test_weak_password()

    print("\n ALL TESTS COMPLETED")
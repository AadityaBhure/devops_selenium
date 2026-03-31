from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Headless mode for Jenkins
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL = "http://localhost:5000"


def wait_for_message():
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text


def test_valid():
    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("John")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "phone").send_keys("1234567890")

    driver.find_element(By.ID, "submit").click()

    message = wait_for_message()
    print("DEBUG:", message)

    assert "Registration successful" in message
    print("Valid Test Passed")


def test_invalid_age():
    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("John")
    driver.find_element(By.ID, "age").send_keys("15")
    driver.find_element(By.ID, "phone").send_keys("1234567890")

    driver.find_element(By.ID, "submit").click()

    message = wait_for_message()
    assert "Invalid age" in message
    print("Invalid Age Test Passed")


def test_invalid_phone():
    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("John")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "phone").send_keys("12345")

    driver.find_element(By.ID, "submit").click()

    message = wait_for_message()
    assert "Invalid phone number" in message
    print("Invalid Phone Test Passed")


if __name__ == "__main__":
    test_valid()
    test_invalid_age()
    test_invalid_phone()
    driver.quit()
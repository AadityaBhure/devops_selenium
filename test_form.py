from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL = "http://localhost:5000"


def wait_for_message():
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    return element.text.strip()


def test_valid():
    driver.get(URL)

    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys("John")

    driver.find_element(By.ID, "age").clear()
    driver.find_element(By.ID, "age").send_keys("25")

    driver.find_element(By.ID, "phone").clear()
    driver.find_element(By.ID, "phone").send_keys("1234567890")

    driver.find_element(By.ID, "submit").click()

    message = wait_for_message()
    print("DEBUG MESSAGE:", message)

    assert message != "NO_MESSAGE", "Form did not submit properly"
    assert "registration" in message.lower()


def test_invalid_phone():
    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("John")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "phone").send_keys("123")

    driver.find_element(By.ID, "submit").click()

    message = wait_for_message()
    assert "phone" in message.lower()


if __name__ == "__main__":
    test_valid()
    test_invalid_phone()
    driver.quit()
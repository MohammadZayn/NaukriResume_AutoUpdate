import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_Naukri_update():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get('https://www.naukri.com/nlogin/login')
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'usernameField')))
        username_field.send_keys('mohammadshaik776@gmail.com')
        password_field = driver.find_element(By.ID, 'passwordField')
        password_field.send_keys("Mohammad47@")
        login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
        login_button.click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.url_contains('https://www.naukri.com/mnjuser/homepage'))
        driver.get('https://www.naukri.com/mnjuser/profile?id=&orgn=homepage')
        file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
                                                     )
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView(true);", file_input)
        resume_path = os.path.abspath(r"C:\Users\moham\OneDrive\Documents\Mohammad_Automation_Engineer.pdf")
        file_input.send_keys(resume_path)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),"
                                                                                  "'Resume uploaded successfully')]")))
        print("Resume updated successfully!")
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_Naukri_update()
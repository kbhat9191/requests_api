from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# --- Setup Chrome WebDriver ---
#chro = Options()
#chro.add_argument("--start-maximized")

# ✅ Correct path to chromedriver.exe (make sure it's unzipped)
driver_path = r"C:\Users\Karthik.bhat\Downloads\chromedriver-win64\chromedriver.exe"
ser = Service(driver_path)

# Launch browser
driver = webdriver.Chrome(service=ser)

try:
    # Step 1: Open login page
    driver.get("https://craftsilicon.hrstop.com/Account/Login?ReturnUrl=%2FDashboard%2FIndex")

    # Step 2: Enter Email
    email_field = driver.find_element(By.ID, "Email")
    email_field.clear()
    email_field.send_keys("karthik.bhat@craftsilicon.com")

    # Step 3: Enter Password
    password_field = driver.find_element(By.ID, "Password")
    password_field.clear()
    password_field.send_keys("Myname@2376")

    # Step 4: Click 'Keep me signed in'
    keep_signed_in_checkbox = driver.find_element(By.ID, "RememberMe")
    if not keep_signed_in_checkbox.is_selected():
        keep_signed_in_checkbox.click()

    # Step 5: Click 'Sign In'
    sign_in_button = driver.find_element(By.XPATH, "//button[text()='Sign In']")
    sign_in_button.click()

    # Step 6: Wait for page load (update this to WebDriverWait for dynamic waits)
    time.sleep(5)

    # Step 7: Basic success check (optional)
    if "Dashboard" in driver.current_url:
        print("✅ Login successful.")
    else:
        print("❌ Login failed or redirected elsewhere.")

finally:
    # Step 8: Clean exit
    driver.quit()

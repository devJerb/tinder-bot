import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

EMAIL = "your-email"
PASSWORD = "your-password"

# driver
chrome_driver_path = "your-chrome-driver-path"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("https://tinder.com/")

# log in
time.sleep(1)
tinder_login_btn = driver.find_elements(By.CSS_SELECTOR, ".w1u9t036 .l17p5q9z")[1]
tinder_login_btn.click()

time.sleep(3)
tinder_fb_login_btn = driver.find_elements(By.CLASS_NAME, "l17p5q9z")[6]
tinder_fb_login_btn.click()

time.sleep(3)
child = driver.window_handles
driver.switch_to.window(child[1])
print(f"Current window is on: {driver.title}")

# fb login
time.sleep(5)
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
fb_login_btn = driver.find_element(By.NAME, "login")

email.send_keys(EMAIL)
password.send_keys(PASSWORD)
fb_login_btn.click()

time.sleep(3)
driver.switch_to.window(child[0])
print(f"Current window is on: {driver.title}")

# location
time.sleep(5)
allow_location_btn = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div/div/div[3]/button[1]')
allow_location_btn.click()

# notifications
time.sleep(3)
not_interested_btn = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div/div/div[3]/button[2]')
not_interested_btn.click()

# dark mode
time.sleep(5)
dark_mode_close_btn = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[2]/button')
dark_mode_close_btn.click()


like_btn = driver.find_element(By.XPATH,
                               '//*[@id="o-1773584476"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                               '3]/div/div[4]/button')

dislike_btn = driver.find_element(By.XPATH,
                                  '//*[@id="o-1773584476"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                                  '3]/div/div[2]/button')

home_screen_option = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[2]/button[2]')

# free account is limited to 100 swipes
for action in range(100):
    try:
        driver.implicitly_wait(5)
        # like()
        dislike_btn.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

            home_screen_option = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[2]/button[2]')
            home_screen_option.click()

        except NoSuchElementException:
            time.sleep(3)
        except ElementNotInteractableException:
            print("Oh snap!")
    driver.implicitly_wait(5)
driver.quit()

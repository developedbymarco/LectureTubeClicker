import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
# --------------------------------
# !!! MAKE YOUR CHANGES HERE !!!
# --------------------------------
# Login credentials
username = "yourusername"
password = "yourpassword"

# time in seconds that program will wait before clicking the next button
# if you are getting timeouts, errors or program can't find the button anymore
# increase this value in 0.1 increments until it works
button_wait = 0.5

# Search credentials
prof = "profsname"
year = "year"

# --------------------------------------------------------------------
# !!! NO CHANGES HERE !!! (except u want to fix a bug that you found)
# --------------------------------------------------------------------
# browser set up
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://tuwel.tuwien.ac.at/mod/lti/view.php?id=882790")

driver.implicitly_wait(30)

# clicking on the login field
login_button = driver.find_element(By.LINK_TEXT, 'TU Wien Login')
login_button.click()

# logging in
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'samlloginbutton').click()

notFound = True

try:
    # switiching into the iframe
    iframe = WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "contentframe"))
    )
    print("iFrame gefunden und gewechselt.")

    # loop that clicks the next button until it finds the wanted lectures
    while notFound:
        if prof in driver.page_source and year in driver.page_source:
            notFound = False
            print("Prof wurde gefunden")
        else:
            driver.implicitly_wait(30)

            button_xpath = '//*[@id="root"]/div/footer/ul/li[8]'
            try:
                button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, button_xpath))
                )
                time.sleep(button_wait)
                ActionChains(driver).move_to_element(button).perform()
                time.sleep(0.05)
                button.click()
            except:
                print("Der Button wurde nicht gefunden oder das Laden dauerte zu lange.")
                break
except TimeoutException:
    print("Das iFrame konnte nicht gefunden werden.")

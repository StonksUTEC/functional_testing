
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/stocks/login")
username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")


testvector = [("75432663","1234","error-handling1","error-handling"),
                ("75432663","4321","error-handling","error-handling1"),
                ("hola","1234","error-handling","error-handling1"),
                ("hola","adios","error-handling","error-handling1")]
errors = 0
test = 0
for user,passw,_id_a,_id_b in testvector:
    username.send_keys(user)
    password.send_keys(passw)
    driver.find_element(By.ID,"login_button").submit()
    username.clear()
    password.clear()
    time.sleep(2)

    a = driver.find_element(By.ID,_id_a).get_attribute("style") 
    b = driver.find_element(By.ID,_id_b).get_attribute("style") 

    try:
        assert a == "display: block;" and b == "display: none;" 
        print(f"Test {test}:",user,passw)
    except:
        errors += 1
        print(f"Failed with user {user} and password {passw}")
    test += 1

print(f"\nExited with {errors} errors")

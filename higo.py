from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
import time

driver = webdriver.Chrome()
driver.get("https://higo.id/")

def test_form_contact_us_success():
        driver.find_element(By.XPATH, "//a[.='Hubungi Kami']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='second-content']")))
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").click()
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//div[@class='form-item email']/input[1]").send_keys("test@gmail.com")
        driver.find_element(By.XPATH, "//div[@class='form-item telepon']/input[1]").send_keys("08718892910")
        driver.find_element(By.XPATH, "//div[@id='company']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("test")
        # WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.XPATH, "//button[contains(.,'Kirim')]").click()
        time.sleep(10)
        
        message = driver.find_element(By.CSS_SELECTOR, ".is-bottom").text
        assert message == "Success Thanks for Submitting"

def test_form_contact_us_invalid_email():
        driver.find_element(By.XPATH, "//a[.='Hubungi Kami']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='second-content']")))
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").click()
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//div[@class='form-item email']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//div[@class='form-item telepon']/input[1]").send_keys("08718892910")
        driver.find_element(By.XPATH, "//div[@id='company']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("test")
        # WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.XPATH, "//button[contains(.,'Kirim')]").click()
        time.sleep(10)
        
        message = driver.find_element(By.XPATH, "//p[.='*Isi dengan email yang valid']").text
        assert message == "*Isi dengan email yang valid"

def test_form_contact_us_not_fill_name():
        driver.find_element(By.XPATH, "//a[.='Hubungi Kami']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='second-content']")))
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").click()
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").send_keys("")
        driver.find_element(By.XPATH, "//div[@class='form-item email']/input[1]").send_keys("test@gmail.com")
        driver.find_element(By.XPATH, "//div[@class='form-item telepon']/input[1]").send_keys("08718892910")
        driver.find_element(By.XPATH, "//div[@id='company']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("test")
        # WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.XPATH, "//button[contains(.,'Kirim')]").click()
        time.sleep(10)
        
        message = driver.find_element(By.XPATH, "//p[.='*Isi nama kamu']").text
        assert message == "*Isi nama kamu"

def test_form_contact_us_invalid_phone():
        driver.find_element(By.XPATH, "//a[.='Hubungi Kami']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='second-content']")))
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").click()
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//div[@class='form-item email']/input[1]").send_keys("test@gmail.com")
        driver.find_element(By.XPATH, "//div[@class='form-item telepon']/input[1]").send_keys("08910")
        driver.find_element(By.XPATH, "//div[@id='company']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("test")
        # WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.XPATH, "//button[contains(.,'Kirim')]").click()
        time.sleep(10)
        
        message = driver.find_element(By.XPATH, "//p[.='*Isi dengan nomor telepon kamu']").text
        assert message == "*Isi dengan nomor telepon kamu"

def test_form_contact_us_not_fill_company():
        driver.find_element(By.XPATH, "//a[.='Hubungi Kami']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='second-content']")))
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").click()
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//div[@class='form-item email']/input[1]").send_keys("test@gmail.com")
        driver.find_element(By.XPATH, "//div[@class='form-item telepon']/input[1]").send_keys("0891080192")
        driver.find_element(By.XPATH, "//div[@id='company']/input[1]").send_keys("")
        driver.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("test")
        # WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.XPATH, "//button[contains(.,'Kirim')]").click()
        time.sleep(10)
        
        message = driver.find_element(By.XPATH, "//p[.='*Isi nama usaha kamu']").text
        assert message == "*Isi nama usaha kamu"

def test_form_contact_us_not_fill_komentar():
        driver.find_element(By.XPATH, "//a[.='Hubungi Kami']").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='second-content']")))
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").click()
        driver.find_element(By.XPATH, "//div[@class='form-item name']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//div[@class='form-item email']/input[1]").send_keys("test@gmail.com")
        driver.find_element(By.XPATH, "//div[@class='form-item telepon']/input[1]").send_keys("0891080192")
        driver.find_element(By.XPATH, "//div[@id='company']/input[1]").send_keys("test")
        driver.find_element(By.XPATH, "//textarea[@id='comment']").send_keys("")
        # WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.XPATH, "//button[contains(.,'Kirim')]").click()
        time.sleep(10)
        
        message = driver.find_element(By.XPATH, "//p[.='* Isi dengan pesan kamu']").text
        assert message == "* Isi dengan pesan kamu" 
    
import time

from selenium import webdriver

class Testsample:
    def test_sample1(self):
        driver = webdriver.chrome()
        driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
        driver.execute_script("window.scrollTo(500,500);")
        driver.execute_script("window.scrollBy(0,docment.body.scrollHeight);")
        time.sleep(4)
        driver.get_screenshot_as_file("screen.png")


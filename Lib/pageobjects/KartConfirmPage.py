from selenium.webdriver.common.by import By

class KartConfirmPage:
    def __init__(self,driver):
        self.driver = driver


    country= (By.XPATH,"//label[text()='Choose Country']/parent::div/div/select")
    agree= (By.CLASS_NAME,"chkAgree")
    proceed = (By.XPATH,"//button[text()='Proceed']")

    def getcountry(self):
        return self.driver.find_element(*KartConfirmPage.country)

    def getAgree(self):
        return self.driver.find_element(*KartConfirmPage.agree)

    def getproceed(self):
        return self.driver.find_element(*KartConfirmPage.proceed)
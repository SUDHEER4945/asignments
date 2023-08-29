from selenium.webdriver.common.by import By


class KartPages:
    def __init__(self,driver):
        self.driver= driver

    rate = (By.XPATH,"//tbody/tr/td[5]/p")
    total = (By.CLASS_NAME,"totAmt")
    promoCode = (By.CSS_SELECTOR,"input[class='promoCode']")
    promoBtn = (By.XPATH,"//button[text()='Apply']")
    promoInfo = (By.CSS_SELECTOR,"span[class='promoInfo']")
    discount = (By.CSS_SELECTOR,"span[class='discountAmt']")
    placeOrder = (By.XPATH,"//button[contains(text(),'Place Order')]")


    def getRates(self):
        return self.driver.find_element(*KartPages.rate)

    def getTotal(self):
        return self.driver.find_element(*KartPages.total)

    def getpromocode(self):
        return self.driver.find_element(*KartPages.promoCode)
    def getpromoBtn(self):
        return self.driver.find_element(*KartPages.promoBtn)
    def getpromoInfo(self):
        return self.driver.find_element(*KartPages.promoInfo)
    def getdiscount(self):
        return self.driver.find_element(*KartPages.discount)
    def getplaceorder(self):
        return self.driver.find_element(*KartPages.placeOrder)



from selenium.webdriver.common.by import By


class KarthomePage:
    def  __init__(self,driver):
        self.driver=driver

    products = (By.CSS_SELECTOR,"h4[class='product-name']")
    addtocart= (By.CSS_SELECTOR,"div[class='product-action'] button")
    cartbtn = (By.CLASS_NAME,"cart_icon")
    proceedtocheckout = (By.XPATH,"//button[text()='PROCEED TO CHECKOUT'] ")


    def getproducts(self):
        return self.driver.find_elements(*KarthomePage.products)

    def getAddToCart(self):
        return self.driver.find_elements(*KarthomePage.addtocart)

    def getCartButton(self):
        return self.driver.find_elements(*KarthomePage.cartbtn)

    def getProceedToCheckout(self):
        return self.driver.find_elements(*KarthomePage.proceedtocheckout)




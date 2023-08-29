
class Homepage:

    def __init__(self,driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.Xpath,"//label[text()='Name']/following-sibling::input")
    email =(By.Name,"email")
    password = (By.ID,"exampleInputPassword1")
    checkbox = (By.ID,"exampleCheck1")
    gender = (By.ID,"exampleFormControlSelect1")
    Employment = (By.ID,"inlineRadio1")
    dob = (By.NAME,"bday")
    submit = (By.XPATH,"//input[@type='submit']")
    successmsg = (By.XPATH,"//div[contains(@class,'alert')]")


    def shopItem(self):
        return  self.driver.find_element(*Homepage.shop)

    def shopItems(self):
        return  self.driver.find_element(*Homepage.shop)

    def getname(self):
        return  self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return  self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return  self.driver.find_element(*Homepage.password)

    def getCheckbox(self):
        return  self.driver.find_element(*Homepage.checkbox)

    def getGender(self):
        return  self.driver.find_element(*Homepage.Gender)

    def Employment(self):
        return  self.driver.find_element(*Homepage.Employment)

    def dob(self):
        return  self.driver.find_element(*Homepage.dob)

    def submitForm(self):
        return  self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return  self.driver.find_element(*Homepage.successmsg)


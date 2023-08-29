import pytest


@pytest.mark.usefixtures("setup")
class Testone:
    def test_e2e(self):
        homepage=Homepage(self.driver)
        homepage.getName().send_keys("sudheer")
        homepage.getEmail().send_keys("sudheer@12.com")
        homepage.getPassword().send_keys("1234ssg")
        homepage.submitForm().click()
        msg = homepage.getSuccessMessage().text
        print(msg)


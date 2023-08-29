import time

import pytest
from selenium.webdriver.common.by import by
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import webdriver
from pageobjects.KartConfirmPage import KartConfirmPage
from pageobjects.KarthomePage import KarthomePage
from pageobjects.KartPage import KartPage


@pytest.mark.usefixtures("setup")
class Testone:
    def test_sample2(self):
        KarthomePage = KarthomePage(self.driver)
        products = KarthomePage.getProducts()

        name = product.text

        i=-1
        for product in products:
            i=i+1
            if "Tomato" in name:
                 KarthomePage.getAddTOCart()[i].click()
            if "Mushroom" in name:
                 KarthomePage.getAddTOCart()[i].click()
            if "Orange" in name:
                 KarthomePage.getAddTOCart()[i].click()
            if "Raspberry" in name:
                 KarthomePage.getAddTOCart()[i].click()
            if "Alomonds" in name:
                 KarthomePage.getAddTOCart()[i].click()
            if "Walnuts" in name:
                 KarthomePage.getAddTOCart()[i].click()

        KarthomePage.getcartbtn().click()
        KarthomePage.getproceedtocheckout.click()
        time.sleep(3)

        KartPage = KartPage(self.driver)
        sum = 0
        rates = KartPage.getRates()
        for rate in rates:
            sum = sum + int(rate.text)
        print(sum)
        total = int(KartPage.getTotal().text)
        assert sum == total

        KartPage.getpromoCode().send_keys("rahulshettyacademy")
        KartPage.getpromoBtn().click()
        time.sleep(7)
        text = KartPage.getpromoInfo().text

        discount = float(KartPage.getDiscount().text)

        KartPage.getPlaceOrder().click()
        time.sleep(3)

        kartConfirmPage =  kartConfirmPage(self.driver)
        country = Select(kartConfirmPage.getCountry())
        country.select_by_visible_text('India')
        time.sleep(2)
        kartConfirmPage.getAgree().click()
        kartConfirmPage.getProceed().click()


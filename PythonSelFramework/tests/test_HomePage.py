
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from BusinessFunctions.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_enterVehicledata(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        #log.info("first name is "+getData["firstname"])
        homepage.get_Make().send_keys(getData["make"])
        homepage.get_Setas().send_keys(getData["seat"])
        homepage.get_Fuel().send_keys(getData["fuel"])
        homepage.get_Performance().send_keys(getData["performance"])
        homepage.get_Date().send_keys(getData["date"])
        homepage.get_Price().send_keys(getData["price"])
        homepage.get_Mileage().send_keys(getData["mileage"])

        log.info("Enter vehicle data succesfully completed")


        homepage.get_Next().click()



        self.driver.refresh()



    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param




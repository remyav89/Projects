from selenium.webdriver.common.by import By

from BusinessFunctions.DownloadTrial import DownloadTrial


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    make=(By.ID, 'make')
    numberofseats=(By.ID, 'numberofseats')
    fuel=(By.ID,'fuel')
    engineperformance=(By.ID, 'engineperformance')
    dateofmanufacture = (By.ID, 'dateofmanufacture')
    listprice = (By.ID, 'listprice')
    annualmileage = (By.ID, 'annualmileage')
    nextenterinsurantdata = (By.ID, 'nextenterinsurantdata')
    downloadtrial=(By.ID,'downloadtrial')

    def get_Make(self):
        return self.driver.find_element(*HomePage.make)

    def get_Setas(self):
        return self.driver.find_element(*HomePage.numberofseats)

    def get_Fuel(self):
        return self.driver.find_element(*HomePage.fuel)

    def get_Performance(self):
        return self.driver.find_element(*HomePage.engineperformance)

    def get_Date(self):
        return self.driver.find_element(*HomePage.dateofmanufacture)

    def get_Price(self):
        return self.driver.find_element(*HomePage.listprice)

    def get_Mileage(self):
        return self.driver.find_element(*HomePage.annualmileage)

    def get_Next(self):
        return self.driver.find_element(*HomePage.nextenterinsurantdata)

    def download_Trial (self):
        self.driver.find_element(*HomePage.downloadtrial).click()
        downloadTrial = DownloadTrial(self.driver)
        return downloadTrial






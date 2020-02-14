import unittest
import MobileUtilities
import BusinessFunctions


class LoginErikBank(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        MobileUtilities.InitializeDriver()
        MobileUtilities.Launch_APP()

    def setUp(self):
        pass

    def testcase(self):
        BusinessFunctions.select_option()
        BusinessFunctions.choose_from_the_options()
        BusinessFunctions.choose_the_category()
        BusinessFunctions.select_item()
        BusinessFunctions.add_product_to_basket()


    def tearDown(self):
        MobileUtilities.driver.execute_script("seetest:client.setReportStatus(\"PASSED\",\"test passed\")")
        pass

    @classmethod
    def tearDownClass(cls):
        MobileUtilities.driver.execute_script(
            "seetest:client.applicationClose(\"" + MobileUtilities.activityName + "\")")
        MobileUtilities.driver_quit()

    if __name__ == '__main__':
        unittest.main()
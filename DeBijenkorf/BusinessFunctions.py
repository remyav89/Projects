import MobileUtilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions

driver = MobileUtilities.InitializeDriver()


def select_option():
    print("Click the options")
    Options=driver.find_element_by_xpath("xpath=//*[@id='toolBar']")
    if(Options.click()):
        WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(By.XPATH, "xpath=//*[@id='worldItemImage' and (./preceding-sibling::* | ./following-sibling::*)[@text='Dames']]"))

    else:
        assert("Options are not displayed")


def choose_from_the_options():
    print("Click on Dames to select the product")

    driver.find_element_by_xpath("xpath=//*[@id='worldItemImage' and (./preceding-sibling::* | ./following-sibling::*)[@text='Dames']]").click()
    print("Categories of dames")
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(By.XPATH, "xpath=//*[@text='Kleding']"))
        print("Categories are displayed")
    except:
        assert "Categories are not displayed"

    MobileUtilities.scroll_Screen()

def choose_the_category():

    print("Click on the category selected")
    driver.find_element_by_xpath("xpath=//*[@text='Kleding']").click()

    print("Click on the item selected")
    Product=driver.find_element_by_xpath("xpath=//*[@text='jeans']").click()

    try:
        WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(By.XPATH,"xpath=//*[@id='productListerThumbnail' and (./preceding-sibling::* | ./following-sibling::*)[@text='Alleen online']]"))
        print("Product found")
    except:
        assert "Product not found"

        MobileUtilities.scroll_Screen()


def select_the_item():
    print("Select the item ")
    driver.find_element_by_xpath("xpath=//*[@id='productListerThumbnail' and (./preceding-sibling::* | ./following-sibling::*)[@text='Alleen online']]").click()

    driver.execute_script(
        "seetest:client.swipeWhileNotFound(""\"Down\", 1000, 2000, \"NATIVE\", \"//*[@text='L']\", 0, 1000, 5, true)")
    print("choose the size of the item")
    driver.find_element_by_xpath("xpath=//*[@text='L']").click()
    time.sleep(5)


def add_product_to_basket():

    AddCart=driver.find_element_by_xpath("xpath=//*[@text='In winkelmand']").click()
    cart=driver.find_element_by_xpath("xpath=//*[@class='android.widget.FrameLayout' and ./*[@text='2']]").click()
    assert WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(By.XPATH,"xpath=//*[@text='GERRY WEBER']"))
    print("Item added succesfully")











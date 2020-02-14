from appium import webdriver


driver = None
dc={}
activityName="nl.debijenkorf/nl.debijenkorf.view.ui.activity.common.MainActivity"


def InitializeDriver():

    global driver
    if driver is None:

        dc['udid'] = 'ce0118219a08123f03'
        dc['appPackage'] = 'nl.debijenkorf'
        dc['appActivity'] = '.view.ui.activity.common.SplashScreen'
        dc['platformName'] = 'android'
        driver = webdriver.Remote('http://localhost:4723/wd/hub',dc)

    return driver

def Launch_APP():

    driver.execute_script(
        "seetest:client.launch(\"" + activityName + "\", \"false\", \"true\")")

def scroll_Screen():

    driver.execute_script("mobile: scroll", {"direction": "down"})


def driver_quit():
    driver.quit()







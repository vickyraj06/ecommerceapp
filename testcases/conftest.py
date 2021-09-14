import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("LAUNCHING CHROME BROWSER.......")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("LAUNCHING FIREFOX BROWSER......")
    else:
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())




    return driver

# To run testcase in different browser

def pytest_addoption(parser):     #This will get the value from CLI/ hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):      #This will return the Browser value to setup method
    return request.config.getoption("--browser")


#To generate HTML report

# It is hook for adding environment info to HTML report

def pytest_configure(config):
    config._metadata['Project Name']='E-Commerce APP'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='RAJ'



# It is hook for delete/modify environment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


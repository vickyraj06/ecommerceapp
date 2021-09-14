from pageObjects.LoginPage import Login
from selenium import webdriver
import pytest
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_login:
    baseURL=ReadConfig.getAplicationurl()
    email=ReadConfig.getEmail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homepagetitle(self,setup):

        self.logger.info("***************** TEST__001_LOGIN *******************")
        self.logger.info("**************** VERIFYING HOMEPAGE TITLE ******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title_home=self.driver.title
        if actual_title_home=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** TEST PASSED ******************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_homepagetitle.png")
            self.driver.close()
            self.logger.error("***************** TEST FAILED *******************")
            assert False


    #@pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):

        self.logger.info("********************* VERIFYING LOGINPAGE TITLE ********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.ip=Login(self.driver)
        self.ip.setEmail(self.email)
        self.ip.setPassword(self.password)
        self.ip.clicklogin()
        actual_title_login=self.driver.title
        if actual_title_login=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******************* TEST PASSED *********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("******************** TEST FAILED ********************")
            assert False
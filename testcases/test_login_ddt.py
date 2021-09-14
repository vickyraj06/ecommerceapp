from pageObjects.LoginPage import Login
from selenium import webdriver
import pytest
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlutilies
import time



class Test_002_DDT_login:
    baseURL=ReadConfig.getAplicationurl()
    path=".\\TestData\\login_data.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("***************** TEST_002_DDT_LOGIN *******************")
        self.logger.info("********************* VERIFYING LOGIN DDT TEST ********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.ip=Login(self.driver)

#datadriven test

        self.rows = xlutilies.getRowcount(self.path)
        print("Number of Rows in Excel",self.rows)

        lst_status=[]  #empty list variable

        for r in range(2, self.rows + 1):
            self.email = xlutilies.readdata(self.path, r, 1)
            self.password = xlutilies.readdata(self.path, r, 2)
            self.exp_results = xlutilies.readdata(self.path, r, 3)


            self.ip.setEmail(self.email)
            self.ip.setPassword(self.password)
            self.ip.clicklogin()
            time.sleep(5)

            actual_title_login=self.driver.title
            exp_title_login="Dashboard / nopCommerce administration"

            if actual_title_login==exp_title_login:
                if self.exp_results=="pass":
                    self.logger.info("********** PASSED ************")
                    self.ip.clicklogout()
                    lst_status.append("pass")

                elif self.exp_results == "fail":
                    self.logger.info("********** FAILED ************")
                    self.ip.clicklogout()
                    lst_status.append("fail")

            elif actual_title_login!=exp_title_login:
                if self.exp_results=="pass":
                    self.logger.info("********** FAILED ************")
                    lst_status.append("fail")

                elif self.exp_results == "fail":
                    self.logger.info("********** PASSED ************")
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("******************* LOGIN DDT TEST PASSED *********************")
            self.driver.close()
            assert True

        else:
            self.logger.error("******************* LOGIN DDT TEST FAILED *********************")
            self.driver.close()
            assert False




        self.logger.info("******************* END OF LOGIN DDT TEST *********************")
        self.logger.info("******************* COMPLETED TEST_002_DDT_LOGIN *********************")

from pageObjects.LoginPage import Login
from pageObjects.Addcustomers import  Add_Customer
from selenium import webdriver
import pytest
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string





class Test_002_Addcustomer:
    baseURL=ReadConfig.getAplicationurl()
    email=ReadConfig.getEmail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customers(self,setup):

        self.logger.info("***************** TEST__002_ADDCUSTOMER *******************")
        self.logger.info("********************* VERIFYING LOGIN ********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.ip=Login(self.driver)
        self.ip.setEmail(self.email)
        self.ip.setPassword(self.password)
        self.ip.clicklogin()
        self.logger.info("********************* SUCCESSFULLY LOGIN ********************")

        self.logger.info("********************* VERIFYING ADDCUSTOMER PAGE ********************")

        self.add_cust= Add_Customer(self.driver)
        self.add_cust.click_customers_menu()
        self.add_cust.click_customers_submenu()
        self.add_cust.add_new()


        self.email=random_generator()+"@gmail.com"
        self.add_cust.set_email(self.email)
        self.add_cust.set_password("raj123")
        self.add_cust.set_firstname("vignesh")
        self.add_cust.set_lastname("raj")
        self.add_cust.select_gender("male")
        self.add_cust.set_companyname("RAJ SOFTAWARE")
        self.add_cust.set_dob("11/6/2021")
        self.add_cust.select_newsletter("teststore")
        self.add_cust.select_customerroles("guests")
        self.add_cust.select_manager_vendor("Vendor 1")
        self.add_cust.set_admincontent("HI IM RAJ SOFTWARE TESTER FROM ABROAD")
        self.add_cust.click_save()
        self.logger.info("******************* SAVING CUSTOMER INFORMATION..*********************")

        self.logger.info("******************* NEW CUSTOMER VALIDATION STARTED *********************")

        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)


        if "The new customer has been added successfully." in self.msg:
            assert True
            self.driver.close()
            self.logger.info("******************* NEW CUSTOMER ADDED SUCCESSFULLY *********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_addcustomer.png")
            self.driver.close()
            self.logger.error("******************** TEST FAILED ********************")
            assert False

def random_generator(size=8,chrs=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chrs) for x in range(size))


from selenium.webdriver.support.ui import Select
import time

class Add_Customer:
    customers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    customers_submenu_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    addnew_xpath="//a[normalize-space()='Add new']"
    email_id="Email"
    password_id="Password"
    firstname_id="FirstName"
    lastname_id="LastName"
    gender_male_id="Gender_Male"
    gender_female_id="Gender_Female"
    dob_id="DateOfBirth"
    companyname_id="Company"
    is_tax_exempt_id="IsTaxExempt"
    newsletter_xpath="//div[@class='input-group-append']//div[@role='listbox']"
    li_newsletter_id="SelectedNewsletterSubscriptionStoreIds_listbox"
    customer_role_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    li_administrative_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    li_forummoderators_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    li_guests_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    li_registered_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    li_vendors_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    manager_of_vendors_xpath="//select[@id='VendorId']"
    admincomment_xpath="//textarea[@id='AdminComment']"
    save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def click_customers_menu(self):
        self.driver.find_element_by_xpath(self.customers_menu_xpath).click()

    def click_customers_submenu(self):
        self.driver.find_element_by_xpath(self.customers_submenu_xpath).click()

    def add_new(self):
        self.driver.find_element_by_xpath(self.addnew_xpath).click()

    def set_email(self,email):
       self.driver.find_element_by_id(self.email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def set_firstname(self,firstname):
       self.driver.find_element_by_id(self.firstname_id).send_keys(firstname)

    def set_lastname(self,lastname):
       self.driver.find_element_by_id(self.lastname_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender=="male":
            self.driver.find_element_by_id(self.gender_male_id).click()

        elif gender=="female":
            self.driver.find_element_by_id(self.gender_female_id).click()

        else:
            self.driver.find_element_by_id(self.gender_male_id).click()

    def set_companyname(self,companyname):
        self.driver.find_element_by_id(self.companyname_id).send_keys(companyname)

    def set_dob(self,dob):
        self.driver.find_element_by_id(self.dob_id).send_keys(dob)

    def select_newsletter(self,store):
        self.driver.find_element_by_xpath(self.newsletter_xpath).click()
        time.sleep(2)
        if store=="teststore":
            self.driver.find_element_by_id(self.li_newsletter_id).click()
        else:
            self.driver.find_element_by_id(self.li_newsletter_id).click()


    def select_customerroles(self,role):

        if role=="registered":
            self.items=self.driver.find_element_by_xpath(self.li_registered_xpath)
        elif role=="forummoderators":
            self.items=self.driver.find_element_by_xpath(self.li_forummoderators_xpath)
        elif role == "administrative_xpath":
            self.items=self.driver.find_element_by_xpath(self.li_administrative_xpath)
        elif role=="guests":
            time.sleep(3)

            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.driver.find_element_by_xpath(self.customer_role_xpath).click()
            self.items = self.driver.find_element_by_xpath(self.li_guests_xpath)



        elif role=="vendors":
            self.items=self.driver.find_element_by_xpath(self.li_vendors_xpath)

        else:
            self.items=self.driver.find_element_by_xpath(self.li_guests_xpath)

        time.sleep(2)
        self.items.click()









    def select_manager_vendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.manager_of_vendors_xpath))
        drp.select_by_visible_text(value)

    def set_admincontent(self,content):
        self.driver.find_element_by_xpath(self.admincomment_xpath).send_keys(content)


    def click_save(self):
        self.driver.find_element_by_xpath(self.save_xpath).click()











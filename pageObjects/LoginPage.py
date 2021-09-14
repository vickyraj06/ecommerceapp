class Login:
    textbox_email_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//div[@class='buttons']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

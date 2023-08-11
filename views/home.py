from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from views.base import Base

class Home(Base):  

    
    HEADER_ITEM = (By.XPATH,"//body/h1")
    def verify_header(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        return self.wait_for(self.HEADER_ITEM)
    
    SUGG_ITEM = (By.XPATH, "//input[@id='autocomplete']")
    MEX_ITEM = (By.XPATH, "//div[text() = 'Mexico']")
    def select_sugg_class(self):
        self.find(self.SUGG_ITEM).click()
        ActionChains(self.driver).send_keys("Me").perform()
        mex_element = self.wait_for(self.MEX_ITEM)
        country = mex_element.text
        mex_element.click()
        return country
    
    DROP_ITEM = (By.XPATH, "//select[@id='dropdown-class-example']")
    OP2_ITEM = (By.XPATH, "//select[@id='dropdown-class-example']/option[3]")
    def select_dropdown_OP2(self):
        self.find(self.DROP_ITEM).click()
        op_element = self.wait_for(self.OP2_ITEM)
        option = op_element.text
        op_element.click()
        return option        
        
    OP3_ITEM = (By.XPATH, "//select[@id='dropdown-class-example']/option[4]")     
    def select_dropdown_OP3(self):
        op_element = self.wait_for(self.OP3_ITEM)
        option = op_element.text
        op_element.click()
        return option       
    
    WIN_LINK = (By.ID, "openwindow")
    TAB_LINK = (By.ID, "opentab") 
    def go_academy(self, action):
        from views.externo import Externo
        if action == 'window':
            self.find(self.WIN_LINK).click()
        if action == 'tab':
            self.find(self.TAB_LINK).click()
        return Externo(self.driver)   

    ALERT_BUT = (By.CSS_SELECTOR, "#alertbtn")
    CONFIRM_BUT = (By.CSS_SELECTOR, "#confirmbtn")
    ALERT_MSG = (By.CSS_SELECTOR, "#name")    
    def select_alert(self, message, button):
        self.find(self.ALERT_MSG).click()
        ActionChains(self.driver).send_keys(message).perform()
        if button == 'alert':
            self.find(self.ALERT_BUT).click()
        if button == 'confirm':
            self.find(self.CONFIRM_BUT).click()
        return self.alert_message()
    
    SEC_WEB = (By.XPATH,"//table[@name = 'courses']/tbody/tr/td[2]")
    TER_WEB = (By.XPATH,"//table[@name = 'courses']/tbody/tr/td[3]")            
    def count_course(self, value):
        col2s = self.finds(self.SEC_WEB)
        col3s = self.finds(self.TER_WEB)
        qty_courses = 0
        for i in range(len(col2s)):
            if int(col3s[i].text) == value:
                print(col2s[i].text,"-" ,col3s[i].text)
                qty_courses += 1
        return qty_courses
    
    
    EN1_WEB = (By.XPATH,"//div[@class = 'tableFixHead']/table/tbody/tr/td[1]")
    EN2_WEB = (By.XPATH,"//div[@class = 'tableFixHead']/table/tbody/tr/td[2]")       
    def count_engineer(self, value):
        col1s = self.finds(self.EN1_WEB)
        col2s = self.finds(self.EN2_WEB)
        qty = 0
        for i in range(len(col2s)):
            if col2s[i].text.lower().strip() == value:
                print(col1s[i].text,"-" ,col2s[i].text)
                qty += 1
        return qty

    IFRAME_ITEM = (By.XPATH,"/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[2]")
    def print_iframe(self):
        self.driver.switch_to.frame("iframe-name")
        return self.find(self.IFRAME_ITEM).text.strip()
        
        
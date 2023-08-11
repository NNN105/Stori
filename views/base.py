from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Base(object):  
    def __init__(self,myDriver):
        self.driver = myDriver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def finds(self, locator):
        return self.driver.find_elements(*locator)
    
    def alert_message(self):
        # switch to the alert
        self.alert = self.driver.switch_to.alert
        # get the text from alert
        alert_text = self.alert.text
        print(alert_text)
        return alert_text
    

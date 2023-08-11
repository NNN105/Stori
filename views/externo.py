from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
from views.base import Base

class Externo(Base):
    PAGE_LABEL = (By.XPATH, "//h2[text() = '30 DAY MONEY BACK GUARANTEE']")
    COURSE_BUTTON = (By.XPATH,"//a[@class = 'main-btn' and text() = 'Apply Now']")
    ALLOW_BUTTON = (By.CSS_SELECTOR, ".button float-left")
    
    def switch_to(self):
        # Change the current window
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for(self.ALLOW_BUTTON)
        
    def scroll_to(self,locator):
        # Scroll to the locator
        self.driver.implicitly_wait(5)
        button = self.wait_for(locator)
        ActionChains(self.driver).scroll_to_element(button).perform()
        time.sleep(2) # Only for visibility
        
    def take_photo_to(self,name):
        #saves image as screenshot
        return self.driver.get_screenshot_as_file(name)
        
    def check_guarantee_title(self):
        self.switch_to()   
        guarantee_title = self.wait_for(self.PAGE_LABEL)
        guarantte = ''
        if guarantee_title:
            guarantte = guarantee_title.text
        self.driver.close()
        return guarantte        
        
    def check_image(self): 
        self.switch_to()
        self.scroll_to(self.COURSE_BUTTON)
        return self.take_photo_to("test_05_switch_tab.png")
        
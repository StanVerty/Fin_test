from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import configs
from selenium.webdriver import Chrome
from pages.base_page import BasePage



class GoogleFinancePage(BasePage):
    #LOCATORS

    _you_may_be_interested_list = "//div[@class='H8Ch1']//div[@class='COaKTb']"

    def google_finance_title(self):
        return self.driver.title


    def you_may_be_interested_collection(self):

        elements = WebDriverWait(self.driver, 40).until((
            EC.presence_of_all_elements_located((By.XPATH, self._you_may_be_interested_list))
        ))
        return [element.text for element in elements]
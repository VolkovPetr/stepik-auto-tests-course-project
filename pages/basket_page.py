from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Found some elements in basket"
    
    def should_be_basket_is_empty(self, selector):
        #assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Empty basket message not found"
        #assert self.is_element_present(By.CSS_SELECTOR, "#content_inner p a[href='" + self.user_language + "']"), "Empty basket message not found"
        assert self.is_element_present(By.CSS_SELECTOR, selector), "Empty basket message not found"
    

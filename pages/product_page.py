from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        
    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        
    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        
    def should_be_book_name(self, book_name):
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERTINNER_NAME).text == book_name, "Can't find alertinner with right book name"
        #assert self.is_element_present(*ProductPageLocators.BASKET_ALERTINNER_NAME), "Can't find alertinner with right book name"
        
    def should_be_book_price(self, book_price):
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERTINNER_PRICE).text == book_price, "Can't find alertinner with right book price"
        #assert self.is_element_present(*ProductPageLocators.BASKET_ALERTINNER_PRICE), "Can't find alertinner with right book price"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
from playwright.sync_api import expect
import time
from pages.locators.myntra_locators import MyntraLocators

import logging


class MyntraPage:
    def __init__(self, page):
        self.page = page

  
    def verify_myntra_logo(self):
        myntra_logo_element = self.page.locator(MyntraLocators.myntra_logo)
        expect(myntra_logo_element).to_be_visible()
        logging.info("Verifying the myntra logo")

    def verify_home_furnishing_text(self):
        home_furnishing_element = self.page.locator(MyntraLocators.home_furnishing)
        expect(home_furnishing_element).to_contain_text("Home Furnishing")
        logging.info("Verifying the Home Furnishing Text")

    def click_filters_men(self):
        men_filter_element = self.page.locator(MyntraLocators.filters_men)
        men_filter_element.click()
        self.page.wait_for_timeout(2000)
        logging.info("Clicked the Men filter")

    def click_filters_women(self):
        women_filter_element = self.page.locator(MyntraLocators.filters_women)
        women_filter_element.click()
        self.page.wait_for_timeout(2000)
        logging.info("Clicked the Women filter")

    def click_filters_boys(self):
        boys_filter_element = self.page.locator(MyntraLocators.filters_boys)
        boys_filter_element.click()
        self.page.wait_for_timeout(2000)
        logging.info("Clicked the boys filter")
    
    def click_filters_girls(self):
        girls_filter_element = self.page.locator(MyntraLocators.filters_girls)
        girls_filter_element.click()
        self.page.wait_for_timeout(2000)
        logging.info("Clicked the girls filter")
        
    def click_size(self):
        #  size_element.wait_for_selector(MyntraLocators.size)
         size_element = self.page.locator(MyntraLocators.size)
         size_element.click()

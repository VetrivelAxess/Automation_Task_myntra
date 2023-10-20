import sys
import os

# Get the absolute path to the project directory (parent directory of the script's directory)
project_directory = os.path.dirname(os.path.dirname(__file__))

# Add the project directory to sys.path
sys.path.append(project_directory)


from pages.page_objects.myntra_page import MyntraPage
import pytest

@pytest.mark.nondestructive
def test_myntra_furnishing(browser):
    page = browser.new_page()
    page.goto('https://www.myntra.com/home-furnishing?src=bc', timeout=30000)
   
   # Create an instance of the MyntraPage class
    myntra = MyntraPage(page)

    # Verify Myntra logo
    myntra.verify_myntra_logo()

    # Verify Home Furnishing text
    myntra.verify_home_furnishing_text()
    myntra.click_filters_men()
  
 

'''
this module contains shared fixtures.
'''

import pytest
import selenium.webdriver


@pytest.fixture
def browser(): 
    #initialize the ChromeDriver instance
    b= selenium.webdriver.Chrome()
    
    # make the call wait up to 10 for elements to appear
    b.implicitly_wait(10)
    
    # return the webdriver instance for the setup
    yield b 

    #quit the webdriver instance for the cleanup
    b.quit()

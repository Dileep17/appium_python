from screen import Screen
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginScreen(Screen):
    locator_name_username = "username"
    locator_name_password = "password"
    locator_classname_signin = "button-primary"
    locator_css_text_experience = ".ng-pristine"
    locator_css_popup_ok = '.popup-buttons'

    def __init__(self, driver):
        super(LoginScreen, self).__init__(driver)

    def wait_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

    def login(self, username, password):
        self.switchToWebContext()
        self.wait_page_load()
        self.driver.find_element_by_name(LoginScreen.locator_name_username).send_keys(username)
        self.driver.find_element_by_name(LoginScreen.locator_name_password).send_keys(password)
        self.driver.find_element_by_class_name(LoginScreen.locator_classname_signin).click()

    def set_experience(self, experience):
        self.driver.find_element_by_css_selector(LoginScreen.locator_css_text_experience).send_keys(experience)
        self.driver.find_element_by_class_name(LoginScreen.locator_css_popup_ok).click()
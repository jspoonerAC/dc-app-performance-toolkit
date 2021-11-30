import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS

""" TODO Add selenium actions for the following:
    View Search Page
    View Global config Page
    View Compliance Space Settings

"""

def app_login_page(webdriver, datasets):
    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.wait_for_page_loaded()
            login_page.set_credentials(username=username, password=password)
            login_page.click_login_button()
            if login_page.is_first_login():
                login_page.first_user_setup()
            all_updates_page = AllUpdates(webdriver)
            all_updates_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
    measure()


def view_config_page(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_approvals_view_config_page")
    def measure():
        # TODO Uncomment code and replace
        # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/servlet/server-classification/classification")
        page.go_to_url("http://localhost:1990/confluence/plugins/servlet/server-classification/classification")
        page.wait_until_visible((By.CLASS_NAME, "admin-heading"))
        # Check whether get started page has been rendered
        page.wait_until_visible((By.XPATH, "//h3[text()='Get Started']"))
        # Check whether all tabs are visible
        page.wait_until_visible((By.XPATH, "//div[text()=' Get Started ']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Classification Levels ']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Global Options']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Spaces']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Statistics']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Enforce Restrictions']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Optimizations']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Macro Options']"))
        page.wait_until_visible((By.XPATH, "//div[text()=' Bulk Change']"))
    measure()


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.wait_for_page_loaded()
    #         login_page.set_credentials(username=username, password=password)
    #         login_page.click_login_button()
    #         if login_page.is_first_login():
    #             login_page.first_user_setup()
    #         all_updates_page = AllUpdates(webdriver)
    #         all_updates_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()

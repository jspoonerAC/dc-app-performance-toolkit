import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


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
        # page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action/plugins/servlet/approvalmacro/system/configuration")
        page.go_to_url("http://localhost:1990/confluence/plugins/servlet/approvalmacro/system/configuration")
        page.wait_until_visible((By.CLASS_NAME, "admin-heading"))
        # Check whether form has been rendered on page
        page.wait_until_visible((By.XPATH, "//h3[text()='General']"))
    measure()


def view_search_page(webdriver, datasets):
    # TODO Implement
    def measure():
        pass


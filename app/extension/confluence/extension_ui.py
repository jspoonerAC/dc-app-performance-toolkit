import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS

# TODO Update space keys with those from testing instance
SPACE_KEYS = ["TS", "CS"]

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
        page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/servlet/approvalmacro/system/configuration")
        page.wait_until_visible((By.CLASS_NAME, "admin-heading"))
        # Check whether form has been rendered on page by checking headings
        page.wait_until_visible((By.XPATH, "//h3[text()='General']"))
        page.wait_until_visible((By.XPATH, "//h3[text()='Notifications']"))
        page.wait_until_visible((By.XPATH, "//h3[text()='Permissions']"))
        page.wait_until_visible((By.XPATH, "//h3[text()='Terminology']"))
    measure()


def view_search_page(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_approvals_view_search_page")
    def measure():
        page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/servlet/approvalmacro/main")
        # check my approvals tab has rendered
        page.wait_until_visible((By.XPATH, "//div[text()='My Approvals']"))
        # check statistics tab has rendered
        page.wait_until_visible((By.XPATH, "//div[text()='Statistics']"))
    measure()


def view_space_settings(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_approvals_view_space_settings")
    def measure():
        space_key = random.choice(SPACE_KEYS)
        page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/plugins/approvalmacro/space/configure.action?key={space_key}")

    # Check settings container has rendered
        page.wait_until_visible((By.CLASS_NAME, "ac-approval-container"))
        # Check whether form has been rendered on page by checking headings
        page.wait_until_visible((By.XPATH, "//h3[text()='Configuration']"))
        page.wait_until_visible((By.XPATH, "//h3[text()='Permissions']"))
        page.wait_until_visible((By.XPATH, "//h3[text()='Teams']"))
    measure()

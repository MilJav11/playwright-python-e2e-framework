from .base_page import BasePage


class TheInternetLoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def open(self):
        self.navigate(self.URL)

    def login(self, username, password):
        self.page.locator("#username").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def flash_message(self):
        return self.page.locator("#flash")

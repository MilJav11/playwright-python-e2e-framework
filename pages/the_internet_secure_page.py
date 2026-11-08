from .base_page import BasePage


class TheInternetSecurePage(BasePage):
    def heading(self):
        return self.page.get_by_role("heading", level=2)

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()

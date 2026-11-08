from .base_page import BasePage


class TheInternetUploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    def open(self):
        self.navigate(self.URL)

    def upload(self, file_path):
        self.page.locator("#file-upload").set_input_files(str(file_path))
        self.page.locator("#file-submit").click()

    def uploaded_files(self):
        return self.page.locator("#uploaded-files")

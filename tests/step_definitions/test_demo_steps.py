import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

from pages.the_internet_login_page import TheInternetLoginPage
from pages.the_internet_secure_page import TheInternetSecurePage
from pages.the_internet_upload_page import TheInternetUploadPage

scenarios("demo_the_internet.feature")

# Demo credentials are published on https://the-internet.herokuapp.com/login
DEMO_USER = "tomsmith"
DEMO_PASSWORD = "SuperSecretPassword!"


@pytest.fixture
def demo_login_page(page):
    return TheInternetLoginPage(page)


@pytest.fixture
def demo_secure_page(page):
    return TheInternetSecurePage(page)


@pytest.fixture
def demo_upload_page(page):
    return TheInternetUploadPage(page)


@given("the user opens the demo login page")
def open_login(demo_login_page):
    demo_login_page.open()


@given("the user opens the demo upload page")
def open_upload(demo_upload_page):
    demo_upload_page.open()


@given("the user logs in with the published demo credentials")
@when("the user logs in with the published demo credentials")
def login_ok(demo_login_page):
    demo_login_page.login(DEMO_USER, DEMO_PASSWORD)


@when("the user logs in with a wrong password")
def login_bad(demo_login_page):
    demo_login_page.login(DEMO_USER, "wrong-password")


@when(parsers.parse('the user uploads a file named "{name}"'))
def upload_file(demo_upload_page, tmp_path, name):
    file_path = tmp_path / name
    file_path.write_text("demo upload content", encoding="utf-8")
    demo_upload_page.upload(file_path)


@when("the user logs out")
def logout(demo_secure_page):
    demo_secure_page.logout()


@then("the secure area is displayed")
def secure_area(page, demo_secure_page):
    expect(page).to_have_url(r"https://the-internet.herokuapp.com/secure")
    expect(demo_secure_page.heading()).to_contain_text("Secure Area")


@then("an invalid password error is displayed")
def invalid_password(demo_login_page):
    expect(demo_login_page.flash_message()).to_contain_text("Your password is invalid!")


@then(parsers.parse('the uploaded file name "{name}" is displayed'))
def uploaded_name(demo_upload_page, name):
    expect(demo_upload_page.uploaded_files()).to_have_text(name)


@then("the login page shows a logged out message")
def logged_out(page, demo_login_page):
    expect(page).to_have_url(r"https://the-internet.herokuapp.com/login")
    expect(demo_login_page.flash_message()).to_contain_text("You logged out of the secure area!")

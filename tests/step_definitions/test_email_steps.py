import os
from dotenv import load_dotenv
from pytest_bdd import scenarios, given, when, then

load_dotenv()
scenarios("email_workflow.feature")

@given("the user is logged into their email account")
def log_in(login_page):
    login_page.navigate("https://login.szn.cz/")
    user_email = os.getenv("TEST_EMAIL")
    user_password = os.getenv("TEST_PASSWORD")
    login_page.login(user_email, user_password)

@when("the user composes a new email for a contact from the list")
def compose_email(mail_page):
    mail_page.compose_email_to(os.getenv("TEST_EMAIL"))

@when("the user attaches a document to the email")
def attach_document(mail_page):
    with open("test_attachment.txt", "w", encoding="utf-8") as f:
        f.write("Automated test attachment.")
    mail_page.attach_file("test_attachment.txt")

@when("the user sends the email")
def send_email(mail_page):
    mail_page.send_email()

@then("the email should be successfully sent")
def verify_sent_email(page):
    # Wait up to 15 seconds for the success notification
    page.locator("text=odeslán").wait_for(state="visible", timeout=15000)

@then("the user logs out")
def log_out(mail_page):
    mail_page.logout()
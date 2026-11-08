# Playwright E2E Automation Portfolio Project

[![Demo Tests](https://github.com/MilJav11/playwright-python-e2e-framework/actions/workflows/demo-tests.yml/badge.svg)](https://github.com/MilJav11/playwright-python-e2e-framework/actions/workflows/demo-tests.yml)

Professional E2E test suite automating the Seznam.cz email workflow using Playwright and Python.

## 🎯 What is Tested (Test Description)

This test suite covers the critical business path (Happy Path) of sending an email via the Seznam.cz web client:

1. Successfully log into a Seznam.cz email account (handling dynamic cookie/ad banners).
2. Navigate directly to the mailbox and initialize a new email to a contact configured via `TEST_EMAIL`.
3. Dynamically generate and attach a local text document (`test_attachment.txt`).
4. Send the email and explicitly wait for the UI notification verifying successful delivery.
5. Safely log out of the account via the profile menu.

## 📊 Test Coverage Info

As an E2E UI automation suite, coverage is focused on **Functional Business Flows**:

- **UI Coverage:** Login Page, Mailbox Dashboard, Email Composer Modal, File Upload Dialog, Success Notification, Logout Flow.
- **Browser Coverage:** Configured for Chromium (Headless mode in CI/CD pipeline, headed mode for local development).
- **Resilience Coverage:** Handles strict-mode violations, dynamic element locators, and conditional UI states (e.g., cookie banners).

## 🚀 Features

- **BDD Framework:** Human-readable tests using Gherkin (`pytest-bdd`).
- **Page Object Model (POM):** Clean separation of test logic and UI locators.
- **CI/CD Integrated:** Automated test execution on every push via GitHub Actions.
- **Security:** Credential management using environment variables.

## 📁 Project Structure

```text
├── .github/workflows/
│   ├── demo-tests.yml      # Gating CI: credential-free demo suite
│   └── tests.yml           # Manual live Seznam suite (workflow_dispatch)
├── pages/                  # Page Object Model classes (Seznam + the-internet demo)
├── tests/
│   ├── features/           # Gherkin: email_workflow.feature (@live), demo_the_internet.feature (@demo)
│   ├── step_definitions/   # BDD steps: test_email_steps.py, test_demo_steps.py
│   └── conftest.py         # Playwright fixtures and setup
├── .env.example            # Template for environment variables
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
├── test_attachment.txt     # Sample attachment used by the tests
└── README.md
```

## 🔧 Setup & Execution

### Prerequisites

- Python 3.10+

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MilJav11/playwright-python-e2e-framework.git
cd playwright-python-e2e-framework
```

2. Configuration: copy `.env.example` to `.env` in the root directory and fill in your credentials. Use a dedicated Seznam TEST account for this purpose. Never commit your `.env` file — it is git-ignored. In CI/CD, `TEST_EMAIL` and `TEST_PASSWORD` are read from repository secrets.

```
TEST_EMAIL=your_test_email@seznam.cz
TEST_PASSWORD=your_password
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install chromium
```

### Demo suite (no account needed)

Runs against the public automation site https://the-internet.herokuapp.com (login, invalid password, file upload, logout). No credentials or `.env` required. This is the suite that gates CI.

```bash
pytest -m demo -v
```

### Live Seznam suite

The Seznam email scenario (`@live`) needs a dedicated test account (`TEST_EMAIL` / `TEST_PASSWORD`). It is run manually (GitHub Actions `workflow_dispatch`, or locally) because the third-party Seznam UI changes and can break the test independently of this code.

```bash
pytest -m live -v
```

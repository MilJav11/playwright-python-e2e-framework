Feature: Email Client Workflows

  @level3 @smoke @live
  Scenario: Send an email with an attachment to a saved contact
    Given the user is logged into their email account
    When the user composes a new email for a contact from the list
    And the user attaches a document to the email
    And the user sends the email
    Then the email should be successfully sent
    And the user logs out
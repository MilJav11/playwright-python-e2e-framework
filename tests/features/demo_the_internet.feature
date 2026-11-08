Feature: Demo suite on the-internet.herokuapp.com

  @demo
  Scenario: Successful login with the published demo credentials
    Given the user opens the demo login page
    When the user logs in with the published demo credentials
    Then the secure area is displayed

  @demo
  Scenario: Invalid password shows an error
    Given the user opens the demo login page
    When the user logs in with a wrong password
    Then an invalid password error is displayed

  @demo
  Scenario: Uploaded file name is shown
    Given the user opens the demo upload page
    When the user uploads a file named "demo_upload.txt"
    Then the uploaded file name "demo_upload.txt" is displayed

  @demo
  Scenario: Logout returns to the login page
    Given the user opens the demo login page
    And the user logs in with the published demo credentials
    When the user logs out
    Then the login page shows a logged out message

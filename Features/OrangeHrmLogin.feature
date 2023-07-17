Feature: OrangeHRM Login
  Scenario: OrangeHRM Login with parameters
    Given Launch Chrome Browser
    When I Opened OrangeHRM Login Page
    And Entered Username "admin" and Password "admin123"
    And Click On Login Button
    Then User Must Successfully Login To Dashboard Page
    Scenario Outline: Login to OrangeHrM with multiple parameters
    Given Launch Chrome Browser
    When I Opened OrangeHRM Login Page
    And Entered Username "<username>" and Password "<password>"
    And Click On Login Button
    Then User Must Successfully Login To Dashboard Page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | admin xyz|admin 123 |
      |admin     |admin xyz |
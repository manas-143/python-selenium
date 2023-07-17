Feature: OrangeHRM Login

  Scenario: login to OrangeHRM with valid parameters
    Given I launch chome browser
    When I open OrangeHRM homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page



  Scenario Outline: login to OrangeHRM with valid parameters
    Given I launch chome browser
    When I open OrangeHRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page
    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | manas    | admin123 |
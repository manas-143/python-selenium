Feature: OrangeHrm Logo
  Scenario: Logo is Present on HomePage
    Given I launch Chrome Browser
    When I Opened OrangeHrm HomePage
    Then Verified Logo is Present or Not
    And Close The Browser

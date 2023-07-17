Feature: OrangeHRM Login
  Background:
     Given I launch chrome browser
    When I opened OrangeHRM homepage
    And Enter the username "admin" and password "admin123"
    And Click on log-in button


  Scenario: login to OrangeHRM with valid parameters
    Then User must successfully login to the Dashboard

  Scenario: Search user
    When navigate to search page
    Then search page should display


  Scenario: Advanced Search user
    When navigate to Advanced search page
    Then Advanced search page should display


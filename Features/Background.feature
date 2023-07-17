Feature: OrangeHRM Login
  Background: Common Steps
    Given Open Browser
    When Open Application
    And Enter Username "admin" and Password "admin123"
    And Click On Login

  Scenario: Login To OrangeHrm Page
    Then User Must Login To Dashboard Page

  Scenario: Profile Check
    When Click to Myinfo
    Then Close Window
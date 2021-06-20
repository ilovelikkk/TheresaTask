# encoding: utf-8
Feature: API-Automation Feature
  Scenario: Get respond from 9-days forecast
    When I send a request with Get method
    Then Verify the status code


  Scenario: Get relative humidity for the day after tomorrow
    When I send a request with Get method
    Then I can get relative humidity for the day after tomorrow
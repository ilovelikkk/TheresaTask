Feature: UI-Automation for CRO/USDC trade page
  Scenario: Navigate to CRO/USDC trade page
    When Navigate to CRO trade page
    Then Verify the CRO trade page is showing

  Scenario: Verify CRO/USDC trade page header
    When Navigate to CRO trade page
    Then Verify the CRO trade page header is showing

  Scenario: Verify current trade info on CRO/USDC page
    When Navigate to CRO trade page
    Then Verify the current trade info is showing

  Scenario: Verify the TV trade chart module
    When Navigate to CRO trade page
    Then Verify the TV trade chart module is showing

  Scenario: Verify the order book module
    When Navigate to CRO trade page
    Then Verify the order book module is showing

  Scenario: Verify the Trading History module
    When Navigate to CRO trade page
    Then Verify the Trading History module is showing

  Scenario: Verify login button in Buy and Sell CRO module
    When Navigate to CRO trade page
    Then Verify login button in Buy CRO module

  Scenario: Verify Open Order in the Order list box module
    When Navigate to CRO trade page
    When Navigate to Open Order in the Order list box module
    Then Verify the Open Order module is showing

  Scenario: Verify Order History in the Order list box module
    When Navigate to CRO trade page
    When Navigate to Order History in the Order list box module
    Then Verify the Order History module is showing
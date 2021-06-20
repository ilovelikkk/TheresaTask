Feature: UI-Automation for CRO/USDC trade page
  Scenario: Navigate to CRO/USDC trade page
    When Navigate to CRO trade page
    Then Verify the CRO trade page is showing

  Scenario: Verify CRO/USDC trade page header
    When Navigate to CRO trade page
    Then Verify the CRO trade page header is showing

  Scenario: Verify login button in Buy and Sell CRO module
    When Navigate to CRO trade page
    Then Verify login button in Buy CRO module

#  Scenario: Verify login button in Buy and Sell CRO module
#    When Navigate to CRO trade page
#    Then Verify login button in Buy CRO module

#  Scenario: Verify Order book module
#    When Navigate to CRO trade page
#    Then Verify login button in Buy CRO module
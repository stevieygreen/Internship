Feature: User can verify Policy links


  Scenario: User can access link under our policy footer section
    Given Open Cureskin main page
    When Click "Terms of Service"
    When Verify Terms of service is shown
    When Go back to home page

    When Click "Refund policy"
    When Verify Refund policy is shown
    When Go back to home page

    When Click "Privacy Policy"
    When Verify Privacy policy is shown
    When Go back to home page

    When Click "Shipping Policy"
    When Verify Shipping policy is shown
    When Go back to home page
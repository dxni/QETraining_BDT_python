
Feature: Test Google

  Scenario: Search in Google
    Given the word on Search field
    When I click on "Buscar en Google"
    Then Display a list with all results on the page

  Scenario: Translate a word
    Given A text to Translate from English to Spanish
    When I Click on "Translate" button
    Then the text should be translated to spanish

  Scenario: log in to Gmail
    Given a e-mail address and password
    When I click on the Log in button
    Then the Inbox page should be display

  Scenario: Search Address on Google Maps
    Given An address to introduce in search field
    When I click on "magnifying glass" icon
    Then on map should be displayed the  Location
And should be displayed the relevant pictures of location on the left side on the page
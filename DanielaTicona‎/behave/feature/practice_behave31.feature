Feature: New Gmail Account form
  Scenario: Validating form fields
    Given User first name is Daniela
      And user last name is Ticona
      And  username is dticona
      And password is 4444
      And confirm password contains 4444
      And birthday month is March
      And birthday day is 19
      And birthday year is 1988
      And gender is Female
      And Mobile phone is 59179152648
      But the current mail is dticonahotmailoom
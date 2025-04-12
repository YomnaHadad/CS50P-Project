import validator_collection
if validator_collection.checkers.is_email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")

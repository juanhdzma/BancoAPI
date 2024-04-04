class ITransactionCases:
    invalidDestination = {
        "source_account": 1,
        "destination_account": "a",
        "value": 10.0
    }
    invalidSource = {
        "source_account": "a",
        "destination_account": 1,
        "value": 10.0
    }
    invalidValue = {
        "source_account": 1,
        "destination_account": 2,
        "value": -10.0
    }
    validData = {
        "source_account": 1,
        "destination_account": 2,
        "value": 10.0
    }

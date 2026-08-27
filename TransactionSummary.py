transactions = [
    {"name": "Andi", "amount": 50000},
    {"name": "Budi", "amount": 75000},
    {"name": "Andi", "amount": 25000},
    {"name": "Citra", "amount": 100000},
    {"name": "Budi", "amount": 50000}
]

def total_transactions(transactions):

    result = {}

    for transaction in transactions:

        name = transaction["name"]
        amount = transaction["amount"]

        if name in result:
            result[name] = result[name] + amount
        else:
            result[name] = amount    

    return result

print(total_transactions(transactions))
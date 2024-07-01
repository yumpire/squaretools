def categorize_tips(transactions, debug=False):
    tips = {
        'gratuity': 0,
        'delivery': 0,
        'dinein': 0,
        'takeout': 0,
    }
    i = 1
    for transaction in transactions:
        if debug:
            print("-------------------------")
            print("Round ", i)
            print("-------------------------")
            print(transaction)
        i += 1
        try:

            # source_type tells us if it's direct or from a delivery app (EXTERNAL)
            source_type = transaction.get('source_type', '')
            # if soure_type is EXTERNAL then skip the transaction as there are no tips involved
            if source_type == 'EXTERNAL':
                continue

            # employee_id tells us if done online or dine in/walk0in
            employee_id = transaction.get('employee_id', '')
            # This is a placeholder logic. Adjust according to your actual data structure
            tip_money = transaction.get('tip_money', {})
            tip_amount = tip_money.get('amount', 0)
            
            # Placeholder categorization logic
            source = transaction.get('external_details.source', '').upper()
            note = transaction.get('note', '').upper()
            is_takeout = transaction.get('is_takeout', False)

            if employee_id:
                tips['dinein'] += tip_amount
            else:
                tips['takeout'] += tip_amount

            if 'GRATUITY' in note:
                tips['gratuity'] += tip_amount
            
            if debug:
                print(f"Transaction ID: {transaction.get('id')}")
                print(f"Tip amount: {tip_amount}")
                print(f"Categorized as: {next(category for category, amount in tips.items() if amount == tip_amount)}")
                print("----")
        except KeyError as e:
            print(f"KeyError: Missing key {e} in transaction {transaction.get('id', 'unknown')}")
        except Exception as e:
            print(f"An error occurred while categorizing transaction {transaction.get('id', 'unknown')}: {str(e)}")
    
    return tips
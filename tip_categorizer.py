from team_fetcher import fetch_team_member_details

def categorize_tips(transactions, square_client, debug=False):
    tips = {
        'gratuity': 0,
        'delivery': 0,
        'dinein': 0,
        'takeout': 0,
        'team': {},
        'other': 0
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
            # if source_type is EXTERNAL then skip the transaction as there are no tips involved
            if source_type == 'EXTERNAL':
                continue

            # employee_id tells us if done online or dine in/walk-in
            employee_id = transaction.get('employee_id', '')
            if employee_id:
                if employee_id not in tips['team']:
                    team_member = fetch_team_member_details(square_client, employee_id, debug)
                    print(team_member)
                    if team_member:
                        employee_name = f"{team_member.get('given_name', '')} {team_member.get('family_name', '')}".strip()
                        tips['team'][employee_name] = 0
                    else:
                        tips['team'][employee_id] = 0
            # This is a placeholder logic. Adjust according to your actual data structure
            tip_money = transaction.get('tip_money', {})
            tip_amount = tip_money.get('amount', 0)
            note = transaction.get('note', '').upper()

            if employee_id:
                if team_member:
                    tips['team'][employee_name] += tip_amount
                else:
                    tips['team'][employee_id] += tip_amount
                tips['dinein'] += tip_amount
            else:
                tips['takeout'] += tip_amount
                tips['other'] += tip_amount

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
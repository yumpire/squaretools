from datetime import datetime, timezone

def get_transactions(square_client, start, end, debug=False):
    # Convert dates to datetime if they're not already
    start_datetime = start if isinstance(start, datetime) else datetime.combine(start, datetime.min.time())
    end_datetime = end if isinstance(end, datetime) else datetime.combine(end, datetime.max.time())
    
    # Ensure timezone is set
    start_datetime = start_datetime.replace(tzinfo=timezone.utc)
    end_datetime = end_datetime.replace(tzinfo=timezone.utc)
    
    start_at = start_datetime.isoformat()
    end_at = end_datetime.isoformat()

    transactions = []
    cursor = None

    if debug:
        print(f"Fetching transactions from {start_at} to {end_at}")

    while True:
        try:
            result = square_client.payments.list_payments(
                begin_time=start_at,
                end_time=end_at,
                cursor=cursor,
                limit=200
            )
            if result.is_success():
                new_transactions = result.body.get('payments', [])
                transactions.extend(new_transactions)
                
                if debug:
                    print(f"Retrieved {len(new_transactions)} transactions in this batch")
                
                cursor = result.body.get('cursor')
                if not cursor:
                    break
            elif result.is_error():
                print(f"Error fetching transactions: {result.errors}")
                break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break

    if debug:
        print(f"Total transactions retrieved: {len(transactions)}")

    return transactions

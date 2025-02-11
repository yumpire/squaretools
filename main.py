#
# This is the main entry point for the application.
#

import argparse
from square_client import get_square_client
from transaction_fetcher import get_transactions
from tip_categorizer import categorize_tips
from payout_calculator import calculate_payouts
from team_fetcher import fetch_team_member_details
from utils import parse_datetime, get_default_start_end

def main():
    parser = argparse.ArgumentParser(description='Square POS Tip Calculator')
    parser.add_argument('--start', type=parse_datetime, required=False, help='Start date (YYYY-MM-DD) or datetime (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--end', type=parse_datetime, required=False, help='End date (YYYY-MM-DD) or datetime (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    start, end = (args.start or get_default_start_end()[0]), (args.end or get_default_start_end()[1])

    square_client = get_square_client()
    transactions = get_transactions(square_client, start, end, args.debug)
    tips = categorize_tips(transactions, args.debug)
    payouts = calculate_payouts(tips)

    print(f"\nTip Summary for {args.start} to {args.end}")
    print("----------------------------------------")
    print(f"Dine-in/Walk-in Tips: ${tips['dinein']/100:.2f}")
    print(f"Takeout/Delivery Tips: ${tips['takeout']/100:.2f}")
    print(f"Gratuity: ${tips['gratuity']/100:.2f}")
    print("\nPayout Summary After Deductions")
    print("----------------------------------------")
    print(f"Dine-in/Walk-in Payout: ${payouts['dinein']/100:.2f}")
    print(f"Takeout/Delivery Payout: ${payouts['takeout']/100:.2f}")
    print(f"Gratuity Payout: ${payouts['gratuity']/100:.2f}")

    # Debugging team details
    team_details = {}
    for employee_id, amount in tips['team'].items():
        try:
            team_member = fetch_team_member_details(square_client, employee_id, args.debug)  # Ensure this function returns the correct object
            team_details[employee_id] = team_member.team
        except AttributeError as e:
            print(f"An error occurred while fetching team member details for employee_id {employee_id}: {e}")
            team_details[employee_id] = None

    print(f"Team: {team_details}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
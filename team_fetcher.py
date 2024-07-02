#
# fetch team member details
#

def fetch_team_member_details(square_client, employee_id, debug=False):
    try:
        result = square_client.team.retrieve_team_member(team_member_id=employee_id)

        if result.is_success():
            team_member = result.body.get('team_member', {})
            if debug:
                print(f"Successfully retrieved team member details for employee_id: {employee_id}")
            return team_member
        elif result.is_error():
            print(f"Error fetching team member details: {result.errors}")
            print(result)
            return None
    except Exception as e:
        print(f"An error occurred while fetching team member details for employee_id {employee_id}: {str(e)}")
        return None


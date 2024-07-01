def calculate_payouts(tips):
    payouts = {
        'dinein': tips['dinein'] * 0.95,
        'takeout': tips['takeout'] * 0.85,
        'gratuity': tips['gratuity'] * 0.90,    
    }
    return payouts
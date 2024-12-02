'''
WE WONT BE USING THIS POLICY WE WILL BE USING REIFORCEMENT LEARNING OR DEEP -Q TO
OPTIMISE THIS POLICY


def simple_policy(state):
    """
    Simple policy to decide whether to approve the mortgage and what interest rate to set.
    :param state: Current state of the customer (ltv, income, credit, trend)
    :return: Action (approve, interest_rate_level)
    """
    ltv, income, credit, trend = state['ltv'], state['income'], state['credit'], state['trend']

    if ltv > 0.9 or credit < 600:  # High risk if LTV > 0.9 or credit score < 600
        return (0, None)  # Deny mortgage
    elif income > 50000 and credit > 700:
        return (1, 0)  # Approve with low rate
    else:
        return (1, 1)  # Approve with high rate

'''
# KRepProject
We will use:

NumPy for numerical computations.
pandas for data manipulation.
gym for reinforcement learning environment (optional, but helpful for structure).

Define the state variables:

Loan-to-Value (LTV)
Credit History
Income
Repayment Trend

major credit companies: experian equifax and trans union
we used experian (state why) can also use an average of all the companies 
but since they are calculated differently went ith experian,.

Excellent. 961 - 999. You should get the best credit cards, loans and mortgages (but there are no guarantees).
Good. 881 - 960. You should get most credit cards, loans and mortgages but you might not get the very best deals.
Fair. 721 - 880. ...
Poor. 561 - 720. ...
Very Poor. 0 - 560.

income range considering the median instead of mean to avoid outliers influnecing values.
(add graphs to your report).

transition function:

This models how the state changes when an action is applied, influenced by external factors (exogenous information).

Parameters:

action: A tuple (approve, rate).
exogenous_info: Tuple (house_value_change, credit_change, income_change) representing random external market dynamics.
Steps:

Action Implications:

If approve == 1:
Loan-to-Value (ltv): Updated based on payments and house value changes.
Loan balance reduces (assumes a fixed repayment amount of 5000).
House value fluctuates by house_value_change.
New ltv is clipped between 0.5 and 1.5 to avoid extreme ratios.
Credit Score: Changes by credit_change and is clipped within the valid range (300-850).
Income: Updated by income_change.
Repayment Trend Update:

trend reflects payment behavior:
If trend == 2 (defaulted), it remains in default.
Otherwise, there's a 20% chance (random.random() < 0.2) of delayed payment.
Updates the state dictionary and returns it.


# (copy the contents of doc 2 for actions transition function and rewards)

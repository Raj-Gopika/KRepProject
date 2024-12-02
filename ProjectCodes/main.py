'''from mortgage_model import MortgageModel
from policy import simple_policy

def main():
    # Initial state (ltv, income, credit, trend)
    ltv = 0.85
    income = 60000
    credit = 700
    trend = 0  # Timely repayment

    # Initialize the mortgage model
    model = MortgageModel(ltv, income, credit, trend)

    # Run the simulation for 100 steps using the simple policy
    total_reward = model.simulate(steps=100, policy=simple_policy)
    print(f"Total reward from simulation: {total_reward}")

if __name__ == "__main__":
    main()
'''
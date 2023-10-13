import numpy as np
import matplotlib.pyplot as plt

# Define historical stock prices
historical_prices = [1448250.00, 1448175.00, 1448300.00, 1448000.00, 1447850.00]

# Define parameters for simulation
num_simulations = 10000
num_days = 5

# Calculate daily returns
returns = np.diff(historical_prices) / historical_prices[:-1]

# Generate simulations
simulations = []
for _ in range(num_simulations):
    prices = [historical_prices[-1]]
    for _ in range(num_days):
        daily_return = np.random.choice(returns)
        price = prices[-1] * (1 + daily_return)
        prices.append(price)
    simulations.append(prices)

# Plot simulations
for sim in simulations:
    plt.plot(sim)
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Monte Carlo Simulation: Stock Price Prediction')
plt.show()
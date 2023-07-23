## Tesla Stock Price Simulation using Geometric Brownian Motion (GBM)

Welcome to the Tesla Stock Price Simulation repository! In this Python script, we simulate the movement of Tesla's stock price using Geometric Brownian Motion (GBM) based on historical data.

### Simulation Details

- The script simulates the stock price of Tesla Inc. (TSLA) over a specified time period using the GBM model.
- The initial stock price (`S0`) is set to $5.65, reflecting the price after a stock split on June 29, 2010.
- The drift (`drift`) represents the average annual return after the stock split, set to 0.6%.
- The volatility (`volatility`) is the standard deviation of the annual returns after the stock split, set to 14.3%.
- The simulation is run for a specified number of scenarios (`n`) over a time period of 252 trading days (equivalent to one year).
- Random noise (`Z`) is generated from a standard normal distribution using the NumPy library.
- The GBM formula is applied to each scenario to simulate the daily stock price movements of Tesla.

### Results

The script visualizes the simulated stock price movements for each scenario using matplotlib. The graph shows how Tesla's stock price evolves over the specified time period.

Additionally, the simulation calculates the following metrics:

- Expected stock price of Tesla at the end of the simulation period.
- Risk (standard deviation) of Tesla's stock price at the end of the simulation period.
- Probability of Tesla's stock price being higher than $10 at the end of the simulation.
- Probability of Tesla's stock price being lower than $2 at the end of the simulation.

### Usage

Simply run the script to perform the simulation. You can adjust the `n` and `T` parameters to explore different scenarios and gain insights into the potential movements of Tesla's stock price using the GBM model.

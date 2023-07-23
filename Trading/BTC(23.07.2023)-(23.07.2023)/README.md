## Monte Carlo Simulation for BTC/USDT Price Movement

This Python script performs a Monte Carlo simulation to model the potential movement of BTC/USDT price. The simulation uses historical price data from the "prices.csv" file, and it allows you to specify different time intervals for analysis.

### Getting Started

1. Make sure you have the "prices.csv" file with historical price data of BTC/USDT in the same directory as this script.

2. To customize the simulation, you can modify the following parameters in the script:
   - `T`: Number of days (trading days) for the simulation.
   - `n`: Number of simulations to run.
   
3. Additionally, ensure you have the "CSV Converter" tool, which is located in the "tools" folder. This converter is essential for preprocessing your data and making it compatible with the simulation.

### Simulation Process

1. The script reads the historical price data from the "prices.csv" file and calculates daily returns.

2. Using the daily returns, it estimates the drift and volatility to model the geometric Brownian motion (GBM) for BTC/USDT price.

3. The simulation generates multiple scenarios of price movements for BTC/USDT over the specified time interval (`T`) using the GBM model and random noise.

4. The script then plots the price trajectories for each scenario to visualize the potential movement of BTC/USDT price.

5. The simulation calculates the expected price and risk (standard deviation of price) for BTC/USDT at the end of the time interval.

6. Lastly, it computes the probabilities of BTC/USDT price being higher than $100,000 and lower than $20,000 at the end of the simulation period.

### Usage

1. Run the CSV Converter tool first to convert your investment data into the required format.

2. Customize the `T` and `n` parameters in the script to suit your analysis needs.

3. Execute the script to perform the Monte Carlo simulation.

Please note that this simulation provides potential price trajectories and probabilities, but it does not constitute financial advice. Use the results for informational and educational purposes only. Always exercise caution and conduct thorough analysis before making any investment decisions.


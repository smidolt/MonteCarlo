## Monte Carlo Simulations Repository

Welcome to the Random Monte Carlo Simulations repository! Here, you'll find a collection of different Monte Carlo simulations covering various scenarios. Let's briefly describe each simulation:

### 1) TailsorHeads.py

This simulation involves flipping a coin (fairly weighted) for a specified number of times (`n`). It calculates the number of times the coin landed on "heads" and "tails" and then determines the probabilities of each outcome. The results are printed in the console.

### 2) Dancers.py

This simulation models the progress of a dancer based on various factors such as age, training intensity, competition intervals, and luck. It generates a large number of trials (`trials`) to simulate the dancer's progress scores. The final progress scores are then plotted in a histogram to visualize the distribution.

### 3) Birthday.py

The "Birthday.py" simulation explores the classic birthday paradox. It generates random samples of people's birthdays and checks if any two or more people share the same birthday. This process is repeated for a large number of cases (`n`), and the probability of two or more people having the same birthday is calculated and printed in the console.

### 4) Trading Example

In this simulation, a geometric Brownian motion model is used to simulate the price movements of two assets, A and B, over a specified period (`T`). The model considers parameters such as average returns, volatilities, and correlation coefficients. The resulting price trajectories for both assets are plotted to visualize the simulated price movements. Additionally, the simulation calculates annualized expected returns, volatility, and Sharpe ratios for each asset.

### 5) Martingale Roulette Simulation

Welcome to the Martingale Roulette Simulation! This Python script simulates the Martingale betting strategy in a roulette game.

#### Simulation Details

- `bank`: The initial bankroll in euros, set to 10000.
- `min_bet`: The minimum bet amount in euros, set to 100.
- `n`: The number of simulations to run, set to 100.
- `bet`: The current bet amount in euros, initially set to `min_bet`.
- `win`: The number of successful bets (red outcome).
- `lose`: The number of unsuccessful bets (green or black outcome).

#### Simulation Process

The simulation loops `n` times, simulating the outcome of each bet in roulette. The roulette wheel has 37 pockets, numbered from 0 to 36. The colors of the pockets are as follows: green (0), red (1-18), and black (19-36).

- If the pocket is green (0), the player loses the bet, doubles their bet, and records the loss.
- If the pocket is red (1-18), the player wins the bet, resets the bet amount to the `min_bet`, and records the win.
- If the pocket is black (19-36), the player loses the bet, doubles their bet, and records the loss.

The simulation continues until the bankroll (`bank`) falls below the current bet amount (`bet`), indicating that the player has lost their remaining funds.

#### Results

After running the simulation, the script will display the following results:

- The final bankroll after `n` simulations.
- The number of wins and losses during the simulations.
- The probability of exhausting the bankroll using the Martingale strategy.

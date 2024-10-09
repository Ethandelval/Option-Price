# Option Pricing Tool

## Overview

This Python script is designed to help users price European Call and Put options using the Black-Scholes pricing model. It takes user input for various parameters related to the stock and options to calculate their values.

## Features

- Prices both Call and Put options based on user input.
- Calculates values using current stock price, exercise price, risk-free rate, expected future stock price, lowest future stock price, and time to expiration.
- Outputs the calculated values for both Call and Put options, as well as checks for arbitrage opportunities using Put-Call Parity.

## How to Use

1. Run the script in a Python environment.
2. Follow the prompts to input the required parameters:
    - Stock Price when purchased
    - Exercise Price
    - Risk-Free Rate (as a percentage)
    - Expected Future Price of the Stock
    - Lowest Future Price of the Stock
    - Time to Expiration (in years)
3. The script will then calculate and display:
    - The value of the Call option
    - The value of the Put option
    - The values of the stock combined with the Put and Call options
    - A message indicating whether there is an arbitrage opportunity


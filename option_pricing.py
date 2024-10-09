
## how to price and option
#call option 
#type_of_option = input("Are you pricing a Option or Put? ")
# Ask user for input on the type of option
print("Ready to price Calls & Puts !? ")
input("Press enter ")

#input by user
todays_price = float(input("What is the Stock Price when purchased? "))
excer_price = float(input("What is the Exercise Price? "))
r_r_f = float(input("What is the Risk-Free Rate (%)? ")) / 100  # Convert percentage to decimal
future_price_stock = float(input("What is the expected future price of the stock? "))
bottom_price = float(input("What is the lowest future price of the stock? "))
expiration_date = float(input("What is the time to Expiration? "))

# things both call & put need
rate = 1 + r_r_f # calculates rate factor
diff = future_price_stock - bottom_price
    
# Call pricing
x_call = future_price_stock - excer_price
delta_call = x_call / diff
part1_call = delta_call * bottom_price
b_call = part1_call / rate 
v_call = delta_call * todays_price - b_call
print(f"The value of the call is: {v_call:.2f}")

# Put pricing
diff_put = bottom_price - excer_price
delta_put = diff_put / diff
part1_put = delta_put * future_price_stock
b_put = part1_put / rate
v_put = delta_put * todays_price - b_put
print(f"The value of the put is: {v_put:.2f}")

#Put-Call Parity
v_of_s0_nd_put = todays_price + v_put
v_of_s0_nd_call = (excer_price/rate) + v_call

print(f'Value of Stock & Put is: {v_of_s0_nd_put:.2f}')
print(f'Value of Stock & Call is: {v_of_s0_nd_call:.2f}')
if v_of_s0_nd_call == v_of_s0_nd_put:
    print("There is no albitrage. Put & Call were priced the same")
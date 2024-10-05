
## how to price and option
#call option 
#type_of_option = input("Are you pricing a Option or Put? ")
# Ask user for input on the type of option
type_of_option = input("Are you pricing a Call Option or Put Option? ").lower()

if type_of_option == "call":
    s_price = float(input("What is the Stock Price when purchased? "))
    excer_price = float(input("What is the Exercise Price? "))
    r_r_f = float(input("What is the Risk-Free Rate (%)? ")) / 100  # Convert percentage to decimal
    price_stock = float(input("What is the current price of the stock? "))
    bottom_price = float(input("What is the lowest price of the stock? "))

    if price_stock > excer_price:
        base_price = (1 + r_r_f) * s_price  # Calculate the premium of the stock with Risk Free rate
        premium = price_stock - base_price
        difference = price_stock - bottom_price
        delta = base_price / difference if difference != 0 else 0  # Handle divide by zero
        b = (delta * bottom_price) / r_r_f if r_r_f != 0 else 0  # Handle divide by zero for r_r_f
        v_call = delta * s_price - b
        print(f"The value of the call is: {v_call:.2f}")
    else:
        print("Do not exercise the option!!!")
else:
    print("Currently, only Call option pricing is supported.")

#put option 
#if type_of_option == "Call" or "call":

capital = 200000
risk_percentage = 1 / 100  # Convert percentage to decimal
position_size_percentage = 20 / 100  # Convert percentage to decimal
risk_amount = capital * risk_percentage
position_size = capital * position_size_percentage

def calculate_stop_loss(entry_price, risk_amount, position_size):
    """
    Calculate the stop loss price and the number of shares to buy.
    :param entry_price: The price at which the trade is entered.
    :param risk_amount: The amount of money risked per trade.
    :param position_size: The total amount to be invested in the trade.
    :return: Stop loss price, number of shares, and risk per share.
    """
    money_allocated = position_size
    number_of_shares = money_allocated / entry_price
    rounded_shares = round(number_of_shares)
    risk_per_share = risk_amount / rounded_shares
    stop_loss_price = entry_price - risk_per_share
    
    return stop_loss_price, rounded_shares, risk_per_share

def calculate_targets(entry_price, risk_per_share):
    """
    Calculate target prices based on different risk-reward ratios.
    :param entry_price: The price at which the trade is entered.
    :param risk_per_share: The risk amount per share.
    :return: Target prices for different risk-reward ratios.
    """
    target1 = entry_price + risk_per_share  # 1:1 risk-reward ratio
    target2 = entry_price + 2 * risk_per_share  # 1:2 risk-reward ratio
    target3 = entry_price + 3 * risk_per_share  # 1:3 risk-reward ratio
    
    return target1, target2, target3

def main():
    # Ask user for the entry price
    entry_price = float(input("Enter the entry price: "))

    # Calculate the stop loss price, number of shares, risk per share, and loss amount
    stop_loss_price, rounded_shares, risk_per_share = calculate_stop_loss(entry_price, risk_amount, position_size)
    
    # Calculate target prices
    target1, target2, target3 = calculate_targets(entry_price, risk_per_share)
    loss_amount = rounded_shares * risk_per_share
    
    # Print the results
    print(f"Entry Price: {entry_price}")
    print(f"SL: {stop_loss_price:.2f}")
    print(f"No.of shares: {rounded_shares}")
    print(f"T1: {target1:.2f}")
    print(f"T2: {target2:.2f}")
    print(f"T3: {target3:.2f}")
    # print(f"Loss Amount: {loss_amount:.2f}")

if __name__ == "__main__":
    main()

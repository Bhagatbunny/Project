
capital = 200000 #2L
position_size = (20/100) * capital # 20% 
risk_per_trade = (1/100) * capital #1% risk on capital per trade 2000

def calc_stop_loss(entry_price,position_size, risk_per_trade):
    
    no_of_shares = round(position_size/entry_price)   #1000
    risk_per_share = risk_per_trade/no_of_shares  #2
    stop_loss = entry_price-risk_per_share    #38

    return no_of_shares, risk_per_share, stop_loss

def Calc_target(entry_price,risk_per_share):

    target1 = entry_price + risk_per_share  # 1:1 RR
    target2 = entry_price + 2 * risk_per_share  # 1:2 RR
    target3 = entry_price + 3 * risk_per_share  # 1:3 RR

    return target1, target2, target3

def main():
    entry_price = int(input("Entry Price:"))  #40

    no_of_shares,risk_per_share,stop_loss = calc_stop_loss(entry_price,position_size, risk_per_trade)
    target1, target2, target3 = Calc_target(entry_price,risk_per_share)

    print(f"{entry_price} \nSL: {stop_loss:.1f} \nNo.of shares: {no_of_shares}")
    print(f"T1: {target1:.1f}, T2: {target2:.1f}, T3: {target3:.1f}")

if __name__ == '__main__':
    main()
    
    










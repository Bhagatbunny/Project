from django.shortcuts import render

capital = 200000
position_size = (20 / 100) * capital
risk_per_trade = (1 / 100) * capital

def calc_stop_loss(entry_price, position_size, risk_per_trade):
    no_of_shares = round(position_size / entry_price)
    risk_per_share = risk_per_trade / no_of_shares
    stop_loss = entry_price - risk_per_share
    return no_of_shares, round(risk_per_share, 1), round(stop_loss, 1)

def calc_target(entry_price, risk_per_share):
    target1 = entry_price + risk_per_share  # 1:1 RR
    target2 = entry_price + 2 * risk_per_share  # 1:2 RR
    target3 = entry_price + 3 * risk_per_share  # 1:3 RR
    return round(target1, 1), round(target2, 1), round(target3, 1)

def index(request):
    if request.method == 'POST':
        entry_price = float(request.POST.get('entry_price', 0))
        no_of_shares, risk_per_share, stop_loss = calc_stop_loss(entry_price, position_size, risk_per_trade)
        target1, target2, target3 = calc_target(entry_price, risk_per_share)
        return render(request, 'index.html', {
            'entry_price': round(entry_price, 1),
            'stop_loss': stop_loss,
            'no_of_shares': no_of_shares,
            'target1': target1,
            'target2': target2,
            'target3': target3,
        })
    return render(request, 'index.html')

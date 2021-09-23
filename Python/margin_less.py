margin = 5

USDT = 9000

price_borrow = 10.68
price_buy = 10.1

USDT_borrow = USDT * margin - USDT

token_borrow = USDT_borrow / price_borrow

USDT_for_repay = token_borrow * price_buy


remaining = USDT * margin - USDT_for_repay


print(remaining)
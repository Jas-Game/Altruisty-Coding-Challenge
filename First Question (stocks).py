days = int(input("Give the Number of days = "))
prices= []
for i in range(days):
    price = int(input(f"Enter stock price of day {i+1} :"))
    prices.append(price)

def maxprofit(prices):
        if len(prices) < 2:
            return 0
        else:
            minprice = float('inf')  
            maxprofit = 0  
            buyday = sellday = -1  
            minday = 0  
            for i, price in enumerate(prices):
                if price < minprice:
                    minprice = price
                    minday = i + 1  

                if price - minprice > maxprofit:
                    maxprofit = price - minprice
                    buyday = minday  
                    sellday = i + 1 

            return maxprofit, buyday, sellday
        
profit, bday, sday = maxprofit(prices)

if profit > 0:
    print(f"Maximum Profit: {profit}")
    print(f"Buy on Day: {bday}")
    print(f"Sell on Day: {sday}")
else:
    print("Maximum Profit: 0")
    print("No transaction possible")



                 


             





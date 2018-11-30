def l122(prices):
    a = 0
    for i in range(len(prices)-1):
        if prices[i+1]-prices[i]>0:
            a = a + prices[i+1]-prices[i]
    return a




print(l122([1,2,3,4,5]))
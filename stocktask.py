import requests as rq
import pandas as pd
stockprice = pd.read_csv('stockprice.csv')
stockdict= stockprice.to_dict(orient='records')

for s in stockdict:
    currencyUrl = 'https://api.coinbase.com/v2/exchange-rates'
    currencyHeader = {"User-Agent": 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    

    currencyParams = {"currency":s['currency']}
    
    currencyResp = rq.get(url=currencyUrl, headers=currencyHeader,params=currencyParams)
    currencyData = currencyResp.json()
    
    INRp= currencyData['data']['rates']['INR']
    s['INRprice'] = s['price'] * float(INRp)
print(stockdict)
Stk=pd.DataFrame(stockdict)
Stk.to_csv('stockdict') 

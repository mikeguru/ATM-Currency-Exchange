"""
Write a program that converts currency. Specifically, convert euros to U.S. dollars.
Prompt for the amount of money in euros you have, and prompt for the current exchange rate
of the euro. Print out the new amount in U.S. dollars. The formula for currency conversion is given.
"""

# Wen Jiang

# Currency-Exchange 

import json
from urllib.request import urlopen


def main():

    amount_from=eval(input("How many euros are you exchanging?"))

    #Wire up your application to an external API1 that provides the current exchange rates.
    webservice_url ="https://openexchangerates.org/api/latest.json?app_id=171cfa200b5f42c2b3d926a075230ab3"
    data = urlopen(webservice_url).read().decode("utf8")
    result = json.loads(data)

    #Build a dictionary of conversion rates, include all countries
    buildDict = result['rates']

    #Prompt for the countries instead of the rates exchange_rate=eval(input("What is the exchange rate?"))
    x=input("What is the country?")

    #Add &base=EUR to the url works if pay for upgrade from the free developer account, which is no use
    if(x=="USD"):
        x="EUR"
  
    dollars=amount_from/buildDict[x]
    dollars=float("{0:.2f}".format(dollars))

    #Specifically, convert euros to U.S. dollars.
    print(amount_from,"euros at an exchange rate of",1/buildDict[x],"is")
    print(dollars)

main()

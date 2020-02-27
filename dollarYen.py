# coding: utf-8
# ドル円 為替を求める

import requests
import math

def f():
    uri = 'https://api.exchangeratesapi.io/latest?base=USD'
    response = requests.get(uri)
    resJson = response.json()

    date = resJson['date']
    result = math.floor(resJson['rates']['JPY'] * 10 ** 2) / (10 ** 2)

    return '{} 1ドル = {} 円'.format(date, result)


if __name__=="__main__":
    print(f())

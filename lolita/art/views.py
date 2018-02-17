from stellar_base.address import Address as STELLAR

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from currency_converter import CurrencyConverter

from django.template import loader
from .forms import AdressForm
import urllib3
urllib3.disable_warnings()
import requests
# Create your views here.

donations = "GBI77GL7DQRUOCQ4QLH2PJEA6KAB54D2CU2YMDRAL6FEMVHHV46WVCFC"


def request_market(url,params=None):
    response = requests.get(url, params=params,verify=False)
    response.raise_for_status()
    return response.json()




def index(request):
    template =loader.get_template('art/index.html')

    c = CurrencyConverter()


    url = ("https://api.coinmarketcap.com/v1/ticker/stellar")
    response = request_market(url)










    symbol = response[0]['symbol']
    price_usd = response[0]['price_usd']
    price_btc = response[0]['price_btc']
    rank = response[0]['rank']

    market_cap = float(response[0]['market_cap_usd'])
    x24h_volume = float(response[0]['24h_volume_usd'])
    x1h_change = response[0]['percent_change_1h']
    x24h_change = response[0]['percent_change_24h']
    x7d_change = response[0]['percent_change_7d']
    market_cap = format(round(int(market_cap)), ',d')
    x24h_volume = format(round(int(x24h_volume)), ',d')

    cena_eur = c.convert(price_usd, 'USD', 'EUR')
    cena_eur = float("{0:.5f}".format(cena_eur))

    cena_yen = c.convert(price_usd, 'USD', 'CNY')
    cena_yen = float("{0:.5f}".format(cena_yen))

    up_green = "#2ECC40"
    down_red = "#FF4136"
    change_1h = ""
    change_24h = ""
    change_7d = ""
    if float(x1h_change) < 0:
        change_1h = down_red
    elif float(x1h_change) > 0:
        change_1h = up_green

    if float(x24h_change) < 0:
        change_24h = down_red
    elif float(x24h_change) > 0:
        change_24h = up_green

    if float(x7d_change) < 0:
        change_7d = down_red
    elif float(x7d_change) > 0:
        change_7d = up_green



    adress = ''

    if request.method == 'POST':
        adress = request.POST.get('adress_form')


        redir = (''+ adress+'')


        return HttpResponseRedirect(redir)


    context = {
        'donations':    donations,
        'adress':       adress,
        'symbol':       symbol,
        'price_usd':    price_usd,
        'price_btc':    price_btc,
        'rank':         rank,
        'change_1h':    change_1h,
        'change_24h':   change_24h,
        'change_7d':    change_7d,
        'cena_eur':     cena_eur,
        'cena_yen':     cena_yen,
        'market_cap':   market_cap,
        '24h_volume':   x24h_volume,
        '1h_change':    x1h_change,
        '24h_change':   x24h_change,
        '7d_change':    x7d_change,
        "x1h_change":   x1h_change,
        'x24h_change':  x24h_change,
        'x7d_change':   x7d_change,

    }

    return HttpResponse(template.render(context, request))



def adress(request, adress):
    c = CurrencyConverter()











    url = ("https://api.coinmarketcap.com/v1/ticker/stellar")
    response = request_market(url)
    symbol = response[0]['symbol']
    price_usd = response[0]['price_usd']
    price_btc = response[0]['price_btc']
    rank = response[0]['rank']
    market_cap = float(response[0]['market_cap_usd'])
    x24h_volume = float(response[0]['24h_volume_usd'])
    x1h_change = response[0]['percent_change_1h']
    x24h_change = response[0]['percent_change_24h']
    x7d_change = response[0]['percent_change_7d']
    market_cap = format(round(int(market_cap)), ',d')
    x24h_volume = format(round(int(x24h_volume)), ',d')

    cena_eur = c.convert(price_usd, 'USD', 'EUR')
    cena_eur = float("{0:.5f}".format(cena_eur))

    cena_yen = c.convert(price_usd, 'USD', 'CNY')
    cena_yen = float("{0:.5f}".format(cena_yen))

    up_green = "#2ECC40"
    down_red = "#FF4136"
    change_1h = ""
    change_24h = ""
    change_7d = ""
    if float(x1h_change) < 0:
        change_1h = down_red
    elif float(x1h_change) > 0:
        change_1h = up_green

    if float(x24h_change) < 0:
        change_24h = down_red
    elif float(x24h_change) > 0:
        change_24h = up_green

    if float(x7d_change) < 0:
        change_7d = down_red
    elif float(x7d_change) > 0:
        change_7d = up_green


    publickey = adress
    address = STELLAR(address=publickey,network='public')  # address = Address(address=publickey,network='public') for livenet
    address.get()  # get the updated information
    balans = address.balances[0]['balance']









    template = loader.get_template('art/balance.html')
    context = {
        'balance':      balans,
        'donations':    donations,
        'adress':       adress,
        'symbol':       symbol,
        'price_usd':    price_usd,
        'price_btc':    price_btc,
        'rank':         rank,
        'change_1h':    change_1h,
        'change_24h':   change_24h,
        'change_7d':    change_7d,
        'cena_eur':     cena_eur,
        'cena_yen':     cena_yen,
        'market_cap':   market_cap,
        '24h_volume':   x24h_volume,
        '1h_change':    x1h_change,
        '24h_change':   x24h_change,
        '7d_change':    x7d_change,
        "x1h_change":   x1h_change,
        'x24h_change':  x24h_change,
        'x7d_change':   x7d_change,

    }
    return HttpResponse(template.render(context,request))
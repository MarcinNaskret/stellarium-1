import requests
# Create your views here.




def request(url,params=None):
    """
    Take url , take params, return
    :param url:
    :param params:
    :return: json
    """

    response = requests.get(url, params=params,verify=False)
    response.raise_for_status()
    return response.json()

adress = 'DCTk3aSwRmTs1taDPQec2T4SK4SaMMw5zF'
url = ("https://verge-blockchain.info/ext/getbalance/" + adress)
response = request(url)

symbol = response


print (symbol)
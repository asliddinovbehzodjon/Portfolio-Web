def sendTelegram(xabar):
    import requests
    api="5298626841:AAF6iNaV3DUy0EvFiZoPpoNkwc_IhMCkFW0"
    url=f'https://api.telegram.org/bot{api}/sendMessage?chat_id=5159670228&text={xabar}'
    requests.get(url)

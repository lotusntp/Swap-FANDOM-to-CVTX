import requests
import time
from line import LINE
from log import Log
from log import Log
line = LINE('TEST')
log = Log()

def list_land():

    url = 'https://web-supergraph.lootrush.com/graphql'
    headers = {
        'Cookie': 'ajs_anonymous_id=fe132314-ba1d-48f7-a3d6-4e9554bef3f1; _gcl_au=1.1.1190567516.1712739949; _hjSessionUser_2897853=eyJpZCI6IjIwM2FjNDFjLWI1YjUtNWMyYy05MDY4LWE4MmUxMmEyMjBlNyIsImNyZWF0ZWQiOjE3MTI3Mzk5NDg3NzcsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1712739949035.196343877; _fbc=fb.1.1713244653380.IwAR3sr63bfboYVYDBZPW19GVsQNQfVROymGVWd505V8q-rxkIiiDwZg22ibw; ajs_user_id=de6cc81c-1c1d-4f9b-8174-645910e4b4ac; _gid=GA1.2.257145299.1713407568; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZTZjYzgxYy0xYzFkLTRmOWItODE3NC02NDU5MTBlNGI0YWMiLCJqdGkiOiI4ZWZjZTQwYy00OWUxLTRjNzItYmE3NC1kNjY0NmNjMWEyNWEiLCJzdGF0dXMiOiJQZW5kaW5nRW1haWxWYWxpZGF0aW9uIiwiaWF0IjoxNzEzNDExNzU2LCJleHAiOjE3MTQ2MjEzNTYsImVtYWlsIjoibG90dXNuYXR0aGFwaG9ybkBnbWFpbC5jb20iLCJvdHAiOm51bGx9.EYctHnXyYhe8Qh7fE9WwoGKICZSBKfgWHmasesUxGKE; _iidt=gSOx/mh6Xgsb+6rpgd3eRmjTVQs5nRXjCfDPJmIzhTcRB10yX0/W4Iin575bj3a6Xp+ljUthL648x+28QinFubhUB+AVl5zVKjG6syc=; _vid_t=U1Ym04YNLXHoth4ZtkGn3PumppA8upUMXjoDuG73WZW6zBl64TTOTjNC+gS8qfFx7Pv/WzOK3/RRJoGo+YJfpqVZyaf65P1Uz1/vGq0=; cf_clearance=kCx9aZPrjSZOLYS4qpyibkJZcs3BYTCCzc1OxckOj9g-1713595641-1.0.1.1-eOcaUy9HGAGocoIBZaxIJ11V8MXFT3QXA29kKVhqMTiSoAUKI0C0pjUzzywZpN0UjdUTzyfKH0kHtStypLsIjg; _hjSession_2897853=eyJpZCI6IjczOTRjNDYzLWU2NzUtNDQyMy1hMThlLTllM2NmOTc2YWVjNSIsImMiOjE3MTM1OTU2NTY5NjIsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _rdt_uuid=1712739948826.40133414-715f-4bfd-a1d2-49cc55f97a7f; _ga=GA1.2.1522709899.1712739949; _ga_2P40HCBEZ4=GS1.1.1713595656.10.1.1713595661.0.0.0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }
    data = {
        "operationName": "nftsV2",
        "variables": {
            "gameSlug": "pixels---farm-land807754",
            "langIsoCode": "en-US",
            "pageSize": 20,
            "currentPage": 1,
            "filterBy": {
                "limitRange": {},
                "rentalFeeRange": {},
                "metadata": [
                    {
                        "name": "environment",
                        "values": []
                    },
                    {
                        "name": "house",
                        "values": []
                    },
                    {
                        "name": "land",
                        "values": []
                    },
                    {
                        "name": "size",
                        "values": []
                    },
                    {
                        "name": "treeDensity",
                        "values": []
                    },
                    {
                        "name": "windmill",
                        "values": []
                    },
                    {
                        "name": "coop",
                        "values": []
                    },
                    {
                        "name": "silo",
                        "values": []
                    }
                ]
            },
            "searchBy": "*",
            "orderBy": "LOWER_RENTAL_FEE"
        },
        "query": "query nftsV2($gameSlug: String!, $langIsoCode: String!, $orderBy: NftSortBy!, $pageSize: Int, $currentPage: Int, $searchBy: String, $filterBy: NftFilters) {\n  queryNfts(\n    gameSlug: $gameSlug\n    langIsoCode: $langIsoCode\n    orderBy: $orderBy\n    pageSize: $pageSize\n    currentPage: $currentPage\n    searchBy: $searchBy\n    filterBy: $filterBy\n  ) {\n    nftsPageInfo {\n      hasNextPage\n      currentPage\n      pageSize\n      numberOfPages\n      totalCount\n      __typename\n    }\n    nodes {\n      id\n      feeAmountUsd\n      creditAmountUsd\n      name\n      ownerProfileId\n      marketingAsset\n      onAuction\n      slug\n      listedWallet\n      ownerWallet\n      isCouponAllowed\n      rentConstraints\n      blockchainIdentifier\n      content {\n        name\n        metadata {\n          traitType\n          value\n          __typename\n        }\n        tokenId\n        description\n        imageUrl\n        __typename\n      }\n      pricing {\n        credit {\n          id\n          productId\n          amount\n          amountPrecision\n          amountCurrencyId\n          status\n          isDefault\n          percentage\n          pricingType\n          __typename\n        }\n        dailyFee {\n          id\n          productId\n          amount\n          amountPrecision\n          amountCurrencyId\n          status\n          isDefault\n          percentage\n          pricingType\n          __typename\n        }\n        __typename\n      }\n      gameSlug\n      supportsCustodialWallet\n      gameId\n      __typename\n    }\n    metadata {\n      counts {\n        count\n        value\n        __typename\n      }\n      fieldName\n      __typename\n    }\n    __typename\n  }\n}"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()

    else:
        log.console(f'Status not equal 200 is {response.status_code}',color='red')
        return None





if __name__ == '__main__':

    min_amount = 0
    while True:
        result = list_land()
        
        if result != None and result['data']['queryNfts']['nodes'] != None:
            lands = result['data']['queryNfts']['nodes']
            for data in lands:
                if  data['pricing']['dailyFee']['amount'] != 0 and data['pricing']['dailyFee']['amount'] != min_amount:
                    min_amount = data['pricing']['dailyFee']['amount']
                    log.console(f"{data['name']} Cost: {min_amount}",color='yellow')
                    line.sendtext(f"{data['name']} Cost: {min_amount}")
        print('Got list land')      
        time.sleep(10)
import os

import requests
from yoomoney import Client, Authorize


async def get_payment_info():
    # Authorize(
    #     client_id=os.getenv("CLIENT_ID"),
    #     redirect_uri=os.getenv("YOUR_REDIRECT_URI"),
    #     scope=["account-info",
    #            "operation-history",
    #            "operation-details",
    #            "incoming-transfers",
    #            "payment-p2p",
    #            "payment-shop",
    #            ]
    # )

    client_id = os.getenv("CLIENT_ID")
    redirect_uri = os.getenv("YOUR_REDIRECT_URI")
    scope = ["account-info",
             "operation-history",
             "operation-details",
             "incoming-transfers",
             "payment-p2p",
             "payment-shop",
             ]

    url = "https://yoomoney.ru/oauth/authorize?client_id={client_id}&response_type=code" \
          "&redirect_uri={redirect_uri}&scope={scope}".format(client_id=client_id,
                                                              redirect_uri=redirect_uri,
                                                              scope='%20'.join([str(elem) for elem in scope]),
                                                              )

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers)
    print(response.url)

    # token = os.getenv("YOOMONEY_TOKEN")
    # client = Client(token)
    # user = client.account_info()
    # print("Account number:", user.account)
    # print("Account balance:", user.balance)
    # print("Account currency code in ISO 4217 format:", user.currency)
    # print("Account status:", user.account_status)
    # print("Account type:", user.account_type)
    # print("Extended balance information:")
    # for pair in vars(user.balance_details):
    #     print("\t-->", pair, ":", vars(user.balance_details).get(pair))
    # print("Information about linked bank cards:")
    # cards = user.cards_linked
    # if len(cards) != 0:
    #     for card in cards:
    #         print(card.pan_fragment, " - ", card.type)
    # else:
    #     print("No card is linked to the account")

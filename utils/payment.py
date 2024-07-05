import os

from yoomoney import Client, Authorize


async def get_payment_info():
    Authorize(
        client_id=os.getenv("CLIENT_ID"),
        redirect_uri=os.getenv("YOUR_REDIRECT_URI"),
        scope=["account-info",
               "operation-history",
               "operation-details",
               "incoming-transfers",
               "payment-p2p",
               "payment-shop",
               ]
    )

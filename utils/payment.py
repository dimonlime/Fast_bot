import os
from yoomoney import Quickpay
from yoomoney import Client, Authorize


# Функция для первичной авторизации, чтобы получить Token доступа(не нужна после первого использования, оставил для
# вида)
async def authorization():
    Authorize(
        client_id=os.getenv("CLIENT_ID"),
        redirect_uri=os.getenv("REDIRECT_URI"),
        scope=["account-info",
               "operation-history",
               "operation-details",
               "incoming-transfers",
               "payment-p2p",
               "payment-shop",
               ]
    )


# Функция для получения всей информации по счету
async def get_payment_info():
    token = os.getenv("ACCESS_TOKEN")
    client = Client(token)
    user = client.account_info()
    print("Account number:", user.account)
    print("Account balance:", user.balance)
    print("Account currency code in ISO 4217 format:", user.currency)
    print("Account status:", user.account_status)
    print("Account type:", user.account_type)
    print("Extended balance information:")
    for pair in vars(user.balance_details):
        print("\t-->", pair, ":", vars(user.balance_details).get(pair))
    print("Information about linked bank cards:")
    cards = user.cards_linked
    if len(cards) != 0:
        for card in cards:
            print(card.pan_fragment, " - ", card.type)
    else:
        print("No card is linked to the account")


# Функция которая генерирует и возвращает ссылку на оплату(соответственно эта ссылка попадает в кнопку "Оплатить")
async def invoice_for_payment():
    quickpay = Quickpay(
        receiver=os.getenv('RECIEVER'),
        quickpay_form="shop",
        targets="Support My Bot",
        paymentType="SB",
        sum=2,
    )
    return quickpay.base_url
    # print(quickpay.base_url)
    # print(quickpay.redirected_url)
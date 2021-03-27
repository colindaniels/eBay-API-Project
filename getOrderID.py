from ebaysdk.trading import Connection
import yaml
itemID = input('Item ID: ')
api = Connection(config_file="ebay.yaml", domain="api.ebay.com", debug=False)
request = {
    'ItemID': itemID
}

response = api.execute("GetItemTransactions", request)
order = response.reply
title = order.Item.Title
price = order.Item.SellingStatus.CurrentPrice.value
status = order.Item.SellingStatus.ListingStatus

item_url = order.Item.ListingDetails.ViewItemURL
paymentStatus = order.TransactionArray.Transaction.Status.CompleteStatus
order_id = order.TransactionArray.Transaction.OrderLineItemID
if status == 'Completed' and paymentStatus == 'Complete':
    print(title)
    print('ITEM HAS SOLD PRINT THE LABEL AT:')
    print('https://gslblui.ebay.com/gslblui/single/' + order_id)
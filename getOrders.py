from ebaysdk.trading import Connection
import yaml
if __name__ == '__main__':
    api = Connection(config_file="ebay.yaml", domain="api.ebay.com", debug=False)
    request = {
        'CreateTimeFrom': '2021-02-24T20:34:44.000Z',
        'CreateTimeTo': '2021-03-24T20:34:44.000Z',
        'OrderRole': 'Seller'
    }

    response = api.execute("GetOrders", request)
    orders = response.reply.OrderArray.Order
    #print(yaml.dump(response.reply, default_flow_style=False))

    for order in orders:
        for transaction in order.TransactionArray.Transaction:
            print(transaction.Item.Title)
            print(transaction.Item.ItemID)
            print(f'Order Status: {order.OrderStatus}')
            print(f'Payment Status: {order.CheckoutStatus.Status}')
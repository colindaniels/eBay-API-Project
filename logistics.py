from ebaysdk.trading import Connection
import config
if __name__ == '__main__':
    api = Connection(domain="api.ebay.com", debug=True)
    request = {
    }

    api.execute(request)



from ebaysdk.trading import Connection
import config
print(config.description)
if __name__ == '__main__':
    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
        "Item": {
            "Title": config.title,
            "Country": "US",
            "Site": "US",
            "ConditionID": "7000",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "colin.daniels@nandor.net",
            "PrimaryCategory": {"CategoryID": "33963"},
            "Description": config.description,
            "ListingDuration": "Days_10",
            "StartPrice": "785",
            "Currency": "USD",

            "ShippingDetails": {
                "ShippingServiceOptions": {
                    "FreeShipping": "",
                    "ShippingService": ""
                }
            },
            "DispatchTimeMax": "1"
        }
    }

    api.execute("AddItem", request)



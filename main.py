from ebaysdk.trading import Connection
import config
if __name__ == '__main__':
    api = Connection(config_file="../Desktop/untitled folder/ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
        "Item": {
            "Country": "US",
            "Site": "US",
            "Title": config.title,
            "PrimaryCategory": {"CategoryID": config.category_ID},
            "ConditionID": config.condition_ID[config.condition],
            "ConditionDescription": config.condition_description,

            "PictureDetails": {
                "PictureURL": config.pictures,
            },

            "Description": "description test",
            "ListingDuration": "Days_10",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "colin.daniels@nandor.net",
            "StartPrice": config.start_price,
            "AutoPay": True,
            "Currency": "USD",
            "PostalCode": "60093",

            "ReturnPolicy": {
                "InternationalReturnsAcceptedOption": "ReturnsNotAccepted",
                "ReturnsAcceptedOption": "ReturnsNotAccepted"
            },

            "ShippingDetails": {
                "CalculatedShippingRate": {
                    "OriginatingPostalCode": "60093",
                    "PackagingHandlingCosts": 0.00
                },
                "ShippingServiceOptions": {
                    "FreeShipping": False,
                    "ShippingService": ""
                }
            },
            "DispatchTimeMax": "1"
        }
    }

    api.execute("AddFixedPriceItem", request)



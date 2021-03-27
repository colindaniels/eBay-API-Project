from ebaysdk.trading import Connection
import config
if __name__ == '__main__':
    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
            "Item": {
                "Title": "Apple iPhone 11 Pro 256GB Gray (Unlocked) Excellent Condition",
                "Description": "Apple iPhone 11 Pro 256GB Gray (Unlocked) Excellent Condition\r\nSerial Number: 2387632935\r\nIMEI: 00138981012045030\r\nEXAMPLE DESCRIPTION",
                "ConditionDescription": "This iPhone 11 Pro is in perfect condition with no damage whatsoever",
                "PrimaryCategory": {
                    "CategoryID": "9355"
                },
                "CategoryMappingAllowed": "true",
                "ConditionID": "7000",
                "Country": "US",
                "Currency": "USD",
                "DispatchTimeMax": "1",
                "ListingDuration": "GTC",
                "ItemSpecifics": {
                    "NameValueList": [
                        {"Name": "Color", "Value": "Gray"},
                        {"Name": "Storage Capacity", "Value": "256GB"},
                        {"Name": "Model", "Value": "Apple iPhone 11 Pro"},
                        {"Name": "Brand", "Value": "Apple"}
                    ]
                },
                "PaymentMethods": "VisaMC",
                "PictureDetails": [
                        {"PictureURL": "https://i.ebayimg.com/images/g/d~8AAOSwrExgWkEZ/s-l500.jpg"},
                        {"PictureURL": "https://i.ebayimg.com/images/g/JtMAAOSwG95gWkEb/s-l500.jpg"},
                        {"PictureURL": "https://i.ebayimg.com/images/g/VU4AAOSwAHRgWkEc/s-l500.jpg"},
                        {"PictureURL": "https://i.ebayimg.com/images/g/YnwAAOSw97RgWkEe/s-l500.jpg"}
                    ],
                "PostalCode": "60611", "Quantity": "1",
                "ReturnPolicy": {
                    "ReturnsAcceptedOption": "ReturnsAccepted",
                    "RefundOption": "MoneyBack",
                    "ReturnsWithinOption": "Days_30",
                    "ShippingCostPaidByOption": "Seller"
                },
                "StartPrice": "500.0",
                "ListingType": "FixedPriceItem",
                "ShippingDetails": {
                    "CalculatedShippingRate": {
                        "OriginatingPostalCode": "60611"
                    },
                    "SalesTax": {
                        "SalesTaxPercent": "6.25",
                        "SalesTaxState": "IL"
                    },
                    "ShippingServiceOptions": [
                        {
                            "FreeShipping": "true",
                            "ShippingService": "USPSPriority",
                            "ShippingServicePriority": "1"
                        },
                        {
                            "ShippingService": "UPSGround",
                            "ShippingServicePriority": "2"
                        },
                        {
                            "ShippingService": "UPSNextDay",
                            "ShippingServicePriority": "3"
                        }
                    ],
                    "ShippingType": "Calculated"
                },
                "ShippingPackageDetails": {
                    "MeasurementUnit": "English",
                    "PackageDepth": "3",
                    "PackageLength": "7",
                    "PackageWidth": "5",
                    "ShippingPackage": "PackageThickEnvelope",
                    "WeightMajor": "0",
                    "WeightMinor": "10"
                },
                "Site": "US"}
    }

    api.execute("AddItem", request)



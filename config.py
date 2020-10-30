iPhone_make = input("iPhone Make: ")
storage = input("Storage: ")
color = input("Color: ")
carrier = input("Carrier: ")

condition = input("Condition: ")
spicific_condition = ''
if condition == "new":
    spicific_condition = condition
if condition == "used" or "for parts":
    spicific_condition = input("Be more specific: ")

condition_description = input("Condition Description")

model_number = input("Model Number: ")
serial_number = input("Serial Number: ")
IMEI = input("IMEI: ")
accessroeis = input("Accessories: ")
start_price = input("Price: ")

title = f"Apple {iPhone_make} - {storage} - {color}({carrier}) - {spicific_condition}"




description = f"{title}:\n" \
              "<meta name='viewport' content='width=device-width, initial-scale=1'>" \
              f"{condition_description}\n" \
              "Specifications:\n" \
              f"Model Number: {model_number}\n" \
              f"Serial Number: {serial_number}\n" \
              f"IMEI: {IMEI}\n" \
              "Accessories:\n" \
              f"{accessroeis}\n" \
              "Payment Option:\n" \
              "We Currently Only Accept PayPal and Credit Card Payment.\n" \
              "Shipping Information:\n" \
              "Orders are generally shipped within 24 via FedEx Ground or FedEx Home Delivery with tracking number. \n" \
              "Shipment is recorded in order to protect against fraud.\n" \
              "Returns and Refund Policy:\n" \
              "If you are not satisfied with your purchase, you may return it for exchange or refund (excluding shipping and handling charges) within 30 days. PLEASE contact us before leaving negative or neutral feedback so we can resolve the issue as best we can!\n" \
              "A refund will be given only if the item received is significantly different from the listing's description. If you feel this is the case, please contact us within 3 days and we will work out a resolution that is agreeable to both parties.  We must receive the return item within 7 days from the day return instruction is provided by our customer service representative.\n" \
              "More pictures/information upon request."

condition_description = "This is the condition description"

# 9355: Cell Phones & Accessories > Cell Phones & Smartphones
categoryID = "9355"

# Under 9335 category conditions:
conditionID = {"new": 1000, "used": 3000, "for parts": 7000}



iPhone_pictures = {
                   "6": "https://ecommet.net/uploads/pre_loaded_product/15efb6a2abea3e.png",
                   "6 Plus": "https://ecommet.net/uploads/pre_loaded_product/15f0a101843360.png",
                   "6s": "https://ecommet.net/uploads/pre_loaded_product/15f09878fdbf68.png",
                   "6s Plus": "https://ecommet.net/uploads/pre_loaded_product/15f0a0fb688386.png",
                   "7": "https://ecommet.net/uploads/pre_loaded_product/15f0a104dd7fda.png",
                   "7 Plus": "https://ecommet.net/uploads/pre_loaded_product/15f0a10644e628.png",
                   "8": "https://ecommet.net/uploads/pre_loaded_product/15f0a107b73f5b.png",
                   "8 Plus": "https://ecommet.net/uploads/pre_loaded_product/15f0a17618ea0f.png",
                   "X": "https://ecommet.net/uploads/pre_loaded_product/15f0a1738c0eea.png",
                   "Xs": "https://ecommet.net/uploads/pre_loaded_product/15f0a2437e4948.png",
                   "Xs Max": "https://ecommet.net/uploads/pre_loaded_product/15f0a240fbaaf8.png",
                   "Xr": "https://ecommet.net/uploads/pre_loaded_product/15f0a1c2717585.png",
                   "11": "https://ecommet.net/uploads/pre_loaded_product/15f0a23d418b18.png",
                   "11 Pro": "https://ecommet.net/uploads/pre_loaded_product/15f0a2a1d4f49c.png",
                   "11 Pro Max": "https://ecommet.net/uploads/pre_loaded_product/15f0a2a0527a25.png"}

selectedPicture = iPhone_pictures['8']
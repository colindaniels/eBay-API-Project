# static variables:

# 9355: Cell Phones & Accessories > Cell Phones & Smartphones
category_ID = "9355"

# Under 9335 category conditions:
condition_ID = {"new": 1000, "used": 3000, "for parts": 7000} # These are the only conditions available for the category



# Example listing config
iPhone_make = 'iPhone XR' # Must be from list of types of iPhones (Used in title, description)
storage = '64GB' # Storage the phone has (Used in title, description)
color = 'White' # iPhone color  (Used in title, description)
carrier = 'AT&T' # iPhone Carrier (Used in title, description)

condition = condition_ID['used'] # Condition of iPhone. Only available condition types for the category are: 1000, 3000, 7000

title_specifier = 'A+ Condition' # Anything the admin wants to put after the title. (*80 Character max title for eBay listings*)

condition_description = 'This iPhone XR is in mint condition. There is absolutely no damage, wear or faults whatsoever' # A separate area to describe more details about the phone (Used in description) (*1000 character limit*)

pictures = "listing.ecommet.net/pictures/A5Js3k8F.jpg" # Will be multiple photos uploaded by the user. For every listing, there will be new photos. (I have not been able to upload more than one picture. I am probably reviewing documentation wrong. If you could help that would be great!)

product_type = 'A1984' # Number found in iPhone settings (Used in description)
product_model = 'MT482LL/A' # Number found in iPhone settings (Used in description)
IMEI = '353063102944031' # Number found in iPhone settings (Used in description)
serial_number = 'F4GY456SKXKP' # Number found in iPhone settings (Used in description)
battery_life = '95%' # Number found in iPhone settings (Used in description)

accessroeis = 'Original box and charger included' # Details about what else is included other than the phone (Used in description)
start_price = 456 #Listing price (Type:Intiger)

title = f"Apple {iPhone_make} - {storage} - {color}({carrier}) - {title_specifier}"

# Each phone needs to have attributes to be inputed into the item spificics for eBay. For example, iPhone XR:
    # Brand: Apple (Given)
    # Model: Apple iPhone XR (Which will be inputed from user from the title)
    # Storage Capacity: 64GB (Which will be inputed from user from the title)
    # Color: White (Which will be inputed from user from the title)
    # Network: AT&T (Which will be inputed from user from the title)
    # Screen Size: 4.7 in
    # Screen Resolution: 12.0 MP (Same for all iPhone models)
    # Processor: Hexa Core
    # Operating System: iOS

# The reason I'm doing this project is so I don't have to enter the same details every time I was to list, it takes up a lot of my time. This will simplify the proccess.



#HTML Format (I don't know how to format correctly, but here is an example of  the HTML.)
# description = "<font rwr="1" style="" face="Times New Roman" size="4"><div style="text-align: center;"><b style="">Apple iPhone XR - 64GB - White (AT&amp;T) ++ PERFECT CONDITION ++</b></div><div style="text-align: left;"><b style="">Condition:</b></div><div style="">This iPhone XR is in mint condition. There is absolutely no damage, wear or faults whatsoever</div><div style=""><br></div><div style=""><b style="">Specifications:</b></div><div style=""><br></div><div style=""><div style="">Product Type: A1984</div><div style="">Product Model: MT482LL/A</div><div style="">IMEI: 353063102944031</div><div style="">Serial Number: F4GY456SKXKP</div><div style="">battery Life: 95%</div><div style=""><br></div></div><div style=""><b style="">Accessories:</b></div><div style="">None</div><div style=""><br></div><div style=""><div style=""><b>Payment Option:</b></div><div style="">We Currently Only Accept PayPal &amp; Credit Card Payment.</div><div style=""><br></div><div style=""><br></div><div style=""><b>Shipping Information:</b></div><div style="">Orders are generally shipped within 24&nbsp; &nbsp;via FedEx Ground&nbsp;or FedEx Home Delivery with tracking number.&nbsp;</div><div style=""><b><u>Shipment is recorded in order to protect against fraud.</u></b></div><div style=""><br></div><div style=""><br></div><div style=""><b>Returns and Refund Policy:</b></div><div style="">If you are not satisfied with your purchase, you may return it for exchange or refund (excluding shipping and handling charges) within 30 days. PLEASE contact us before leaving negative or neutral feedback so we can resolve the issue as best we can!</div><div style=""><br></div><div style="">A refund will be given only if the item received is significantly different from the listing's description. If you feel this is the case, please contact us within 3 days and we will work out a resolution that is agreeable to both parties.&nbsp; We must receive the return item within 7 days from the day return instruction is provided by our customer service representative.</div><div style=""><br></div><div style=""><font style="">More pictures/information upon req</font><font style="">uest.</font></div></div></font>"


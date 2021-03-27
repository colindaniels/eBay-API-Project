from ebaysdk.finding import Connection
import csv
from datetime import datetime, timedelta

date_N_days_ago = datetime.now() - timedelta(days=30)

datenow = datetime.now().strftime(f"%Y-%m-%dT%H:%M:%S.000Z")
month_ago = date_N_days_ago.strftime(f"%Y-%m-%dT%H:%M:%S.000Z")
print(datenow)
print(month_ago)
max_pages = 10
'2017-01-25T00:00:00.000Z'
model_list = []

api = Connection(config_file='ebay.yaml', debug=True, siteid="EBAY-US")


request = {
    'keywords': 'iPhone X'
}
response = api.execute('findCompletedItems', request)
for item in response.reply.searchResult.item:
    print(item.title, item.sellingStatus.currentPrice.value)


'''
def make_request():
    request = {
        
        'keywords': 'a1865 64gb',
        'categoryId': '9355',

        'sellingStatus': {
            'sellingState': 'Ended'
        },
        'condition': {
            'conditionId': '3000'
        },
        'itemFilter': [
            {'name': 'MaxPrice', 'value': 500},
            {'name': 'StartTimeFrom', 'value': '2021-02-10T00:00:00.000Z'}


        ],
        'paginationInput': {
            'entriesPerPage': 100,
            'pageNumber': 1
        },
        'sortOrder': 'BestMatch',

    }
    response = api.execute('findItemsByKeywords', request)
    for item in response.reply.searchResult.item:
        model_list.append((item.title, item.sellingStatus.currentPrice.value))


make_request()

with open('model.csv', 'w') as file:
    file.write('model,price\n')
    writer = csv.writer(file)
    for model, price in model_list:
        writer.writerow((model, price))


def get_average(lst):
    sum = 0
    length = len(lst)
    for model, price in lst:
        price = float(price)
        sum = sum + price
    return round(sum/length, 2)


print(get_average(model_list))
'''
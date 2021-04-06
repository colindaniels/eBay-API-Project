import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def get_average(lst):
    sum = 0
    length = len(lst)
    for price in lst:
        sum = sum + price
    return round(sum/length, 2)

def reject_outliers(data):
    m = 2
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__uzma=153d2ce7-2b56-4b07-a0f9-67dbd700f16a; __uzmb=1609641196; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=00a67e99-3384-4391-989d-3bd46024cd6f; __uzmbj2=1609641197; cid=RJQzkFk3wdXkM8EF%23888252336; __uzme=3519; QuantumMetricUserID=2bd37bb459955dee3cf4da60f27929d1; D_HID=756BB114-57A3-3061-9DF8-BDE71FE4579A; D_IID=D8F94D47-FBE9-34C8-9D37-BE7AA4124D07; D_ZID=BEDBB469-A805-39DD-87F7-634DFF9A3194; D_SID=136.30.186.46; D_UID=4BFB31BA-2532-3460-A20F-1A9104230D68; D_ZUID=7B7F1DE0-B642-302C-BA02-30B06D47C299; ak_bmsc=05B873EEA3EC2E0FCC5AD979ED2FF8BA173724741125000055D65A60606AB377~plY8+D6y5MoM3R8P4k3rIkHhgZTwB6DHjmKNA9RfRzXOH8JVrgfg7lGMpuQMASL/Mv1Zf2hGeH6ArNBGH4xWyMxvW/LCzO7Nkgizv7uAzBMJ5KspliO0yms13tfM1mOtYHVBo+1y6bzfUUApb8pm077ZAmelktHJDzdm/Zc7ZjxFK/Il34xrfZ2Hh8Vth3sRHQ3760j8sSW2P4i4WrrM6PeFvaT0c+2xExwImGm3Ox+HY; bm_sv=7F49B02EB16C4F246E8CBC24E0F2A4B5~BrK4enLXyR9vj2/pMRhgqvGEo+mjVfeuWQn03eP3BbQSb2Nev9qGXiRZyP91KLdPDN2NCWEUc2oPPeqOCrtAbncuuwsYUpK6VYcUbP4JnK51w9BbgotIpvhkKSyDPQxLYsWfbC19cDELFowJlwCJYfR9d7V3mC4jqlmQlgiWpeM; __gads=ID=22a669b96385a75d:T=1616567106:S=ALNI_MadiVhftMTIvAvcXovRsBu8G4-8CQ; DG_SID=136.30.186.46:utVROTmCHo4YRg89JHs+rC7NlJwWgNCJuoTJJuDXh70; AMCVS_A71B5B5B54F607AB0A4C98A2%40AdobeOrg=1; DG_ZID=56B436DA-6F29-3177-87DB-B52CF327B536; DG_ZUID=27D8E81D-04A5-3F2F-9036-2307F98DEE0B; DG_HID=B14F6E97-3A4C-36C6-AEA2-99DCEB4B2D81; DG_IID=2D00D6C1-2C26-3F20-8DE9-4036412BD4E5; DG_UID=AE0E6545-E25C-3256-B9F1-CAA41368A6DD; ds1=ats/1616801548863; cssg=dfbb17c41760aad90773076cffad71d1; JSESSIONID=5A868D4C5BB649455FD5596A25131490; shs=BAQAAAXiVB3iwAAaAAVUAD2I/oowyMDQxMzMxNTMyMDA1LDI3EqX+YbI9WwO9P6xTQw6Mc3wkhg**; AMCV_A71B5B5B54F607AB0A4C98A2%40AdobeOrg=-408604571%7CMCMID%7C18721502967304683392404039235057215343%7CMCAAMLH-1618020143%7C7%7CMCAAMB-1618020143%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-682630538%7CMCOPTOUT-1617422543s%7CNONE%7CvVersion%7C4.6.0; __uzmc=5240174832516; __uzmd=1617417269; ds2=; __uzmcj2=8245639490559; __uzmdj2=1617417270; npii=btguid/dfbb17c41760aad90773076cffad71d1642a3b37^cguid/fd53d9ec1760aadc3ca082ddfbee5a4a642a3b37^; ebay=%5EsfLMD%3D0%5Esin%3Din%5Edv%3D6067ce56%5Esbf%3D%2320000000000010008000044%5Ecos%3D2%5Elrtjs%3D0.1%5Ecv%3D15555%5Ejs%3D1%5E; cpt=%5Ecpt_prvd%3Drecaptcha_v2%5Ecpt_guid%3D831b42ed-cf49-4217-9582-7d8535bbbbad%5E; ns1=BAQAAAXiVB3iwAAaAAKUADWJJCgwxODU3MzA5MzczLzA7ANgASmJJCgxjNjl8NjAxXjE2MTY4MDMzMjMzMDZeXjFeM3wyfDV8NHw3fDExXl5eNF4zXjEyXjEyXjJeMV4xXjBeMV4wXjFeNjQ0MjQ1OTA3NXVwsOIz73sZeZqvmhqshkxzOLjP; dp1=bkms/in642a3d8c^u1f/Colin642a3d8c^tzo/12c6067e49c^exc/0%3A0%3A1%3A1608f638c^pcid/88825233662490a0c^mpc/0%7C06075058c^u1p/ZWNvbW1ldF9sbGM*642a3d8c^bl/USen-US642a3d8c^expt/0001616801549533614f08cd^pbf/%232030040a000200050819c0200000462490a0c^; s=BAQAAAXiVB3iwAAWAAPgAIGBpKAxkZmJiMTdjNDE3NjBhYWQ5MDc3MzA3NmNmZmFkNzFkMQFFAAhiSQoMNjA1MWMwNzKSZPoCNcjaAWm9I3KSd4dQd7idKQ**; nonsession=BAQAAAXiVB3iwAAaAAJ0ACGJJCgwwMDAwMDAwMQFkAAdkKj2MIzAwMDAwYQAIABxgj2OMMTYxNzMyMjEwNHgyMzM5MTI5MjgwMTN4MHgyWQAzAA5iSQoMNjAwOTMtMTYyOSxVU0EAywACYGfdlDkyAEAAC2JJCgxlY29tbWV0X2xsYwAQAAtiSQoMZWNvbW1ldF9sbGMAygAgZCo9jGRmYmIxN2M0MTc2MGFhZDkwNzczMDc2Y2ZmYWQ3MWQxAAQAC2I/ooxlY29tbWV0X2xsYwCcADhiSQoMblkrc0haMlByQm1kajZ3Vm5ZK3NFWjJQckEyZGo2QU1sWVdpQ0ptQnBnK2RqNng5blkrc2VRPT3VPd9ALEJvAHeyfBDAJZXsOGrzvQ**',
    'referer': 'https://www.ebay.com/splashui/captcha?ap=1&appName=orch&ru=https%3A%2F%2Fwww.ebay.com%2Fsch%2Fi.html%3F_from%3DR40%26_nkw%3DiPhone%2Bexcellent%26_sacat%3D0%26Model%3DApple%252520iPhone%2525206%26Network%3DUnlocked%26Storage%252520Capacity%3D16%252520GB%26_dcat%3D9355%26LH_ItemCondition%3D3000%26rt%3Dnc%26LH_Sold%3D1%26LH_Complete%3D1%26_ipg%3D200%26_pgn%3D1%26_ipg%3D200%26LH_BIN%3D1&iid=f29fb032-450e-4e52-a94b-13a1c74fd6a7'


}
def requestPage(keyword, added_word, model, network, storage, condition, buying_format):
    raw_model = model.replace(' ', '%2520').replace('(', '%2528').replace(')', '%2529')
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={keyword}+{added_word}&_sacat=0&Model={raw_model}&Network={network}&Storage%2520Capacity={storage}%2520GB&_dcat=9355&LH_ItemCondition={condition}&rt=nc&LH_Sold=1&LH_Complete=1&_ipg=200&_pgn=1&_ipg=200&LH_{buying_format}=1'
    # print(url)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = int(soup.find(class_='srp-controls__count-heading').find(class_='BOLD').text.replace(',', ''))
    return soup, results

def getUnfilteredPrices(soup):
    title_list = [value.text.strip().lower() for value in soup.find_all(class_='s-item__title s-item__title--has-tags')]
    price_list = [value.text.strip().lower() for value in soup.find_all(class_='s-item__price')]
    zipped = list(zip(title_list, price_list))
    return zipped


def getFilteredPrices(title_price_list):
    all_title_and_price = []
    all_prices = []
    for tp in title_price_list:
        if 'to' not in tp[1] and all([w not in tp[0] for w in condition['excludedPhrases']]):
            all_title_and_price.append(tp)
            all_prices.append(float(tp[1][1:].replace(',', '')))
    return all_title_and_price, all_prices

def getAveragePrice(prices):
    average_price = get_average(reject_outliers(prices))
    return average_price


def plot(all_prices, average_price, result):
    plt.hist(reject_outliers(all_prices), bins=30)
    plt.axvline(x=average_price, color='r', linestyle='dashed', linewidth=2)
    plt.title(f'{model} - ({carrierName}) - ({storage}GB) - ({conditionName}) - ({result} results)')
    plt.xlabel(f'Sold Price ($) - Average Price: ({average_price})')
    plt.ylabel('Volume')
    plt.show()

def writeCSV(msp, file_name):
    with open(file_name, 'w') as file:
        file.write('model,storage,carrier,condition,price\n')
        writer = csv.writer(file)
        for model, storage, carrier, condition, price in msp:
            writer.writerow((model, storage, carrier, condition, price))

        file.close()

network_list = [
    {
        'network': 'Unlocked',
        'networkID': 'Unlocked'
    },
    {
        'network': 'Verizon',
        'networkID': 'Unlocked'
    },
    {
        'network': 'AT&T',
        'networkID': 'AT%2526T'
    },
    {
        'network': 'T-Mobile',
        'networkID': 'T%252DMobile'
    },
    {
        'network': 'Sprint',
        'networkID': 'Sprint'
    },


]


buying_format_dict = {'Buy It Now': 'BIN', 'Auction': 'Auction'}


condition_list = [

    {
        'condition': 'Like New',
        'conditionID': '3000',
        'excludedPhrases': ['read', 'face', 'see', 'not', 'lot', 'protector', 'case', 'bad', 'touch', 'fair', 'ic', 'poor', 'lcd'],
        'addedWord': 'excellent'
    },
    {
        'condition': 'Good',
        'conditionID': '3000',
        'excludedPhrases': ['read', 'face', 'see', 'not', 'lot', 'protector', 'case', 'bad', 'touch', 'fair', 'ic', 'poor', 'lcd'],
        'addedWord': ''
    },
    {
        'condition': 'Fair',
        'conditionID': '3000',
        'excludedPhrases': ['face', 'lot', 'protector', 'case', 'touch', 'ic'],
        'addedWord': ''
    },
    {
        'condition': 'Broken',
        'conditionID': '7000',
        'excludedPhrases': ['lot', 'protector', 'case', 'ic'],
        'addedWord': ''
    },


]


model_list = [
    {
        'model': 'Apple iPhone 6',
        'storage': ['16', '32', '64', '128']
    },
    {
        'model': 'Apple iPhone 6 Plus',
        'storage': ['16', '64', '128']
    },

    {
        'model': 'Apple iPhone 6s',
        'storage': ['16', '32', '64', '128']
    },

    {
        'model': 'Apple iPhone 6s Plus',
        'storage': ['16', '32', '64', '128']
    },
    {
        'model': 'Apple iPhone 7',
        'storage': ['32', '128', '256']
    },
    {
        'model': 'Apple iPhone 7 Plus',
        'storage': ['32', '128', '256']
    },
    {
        'model': 'Apple iPhone 8',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone 8 Plus',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone SE (2nd Generation)',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone X',
        'storage': ['64', '256']
    },
    {
        'model': 'Apple iPhone XR',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone XS',
        'storage': ['64', '256', '512']
    },
    {
        'model': 'Apple iPhone XS Max',
        'storage': ['64', '256', '512']
    },
    {
        'model': 'Apple iPhone 11',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone 11 Pro',
        'storage': ['64', '256', '512']
    },
    {
        'model': 'Apple iPhone 11 Pro Max',
        'storage': ['64', '256', '512']
    },
    {
        'model': 'Apple iPhone 12',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone 12 mini',
        'storage': ['64', '128', '256']
    },
    {
        'model': 'Apple iPhone 12 Pro',
        'storage': ['128', '256', '512']
    },
    {
        'model': 'Apple iPhone 12 Pro Max',
        'storage': ['128', '256', '512']
    }
]

keyword = 'iPhone'
buying_format = buying_format_dict['Buy It Now']

all_storage = []
for attributes in model_list:
    all_storage.append(len(attributes['storage']))


LENGTH = len(model_list) * len(condition_list) * len(network_list) * get_average(all_storage)
pbar = tqdm(total=LENGTH)

all_models_and_average = []
for attributes in model_list:
    for storage in attributes['storage']:
        for carrier in network_list:
            for condition in condition_list:
                carrierName = carrier['network']
                carrierID = carrier['networkID']
                conditionName = condition['condition']
                conditionID = condition['conditionID']
                excludedPhrases = condition['excludedPhrases']
                includedPhrase = condition['addedWord']
                model = attributes['model']
                try:
                    soup = requestPage(keyword, includedPhrase, model, carrierID, storage, conditionID, buying_format)

                    title_and_prices = getUnfilteredPrices(soup[0])
                    try:
                        results = soup[1]
                    except:
                        results = 0

                    filtered_prices = getFilteredPrices(title_and_prices)
                    if results >= 25:
                        try:

                            average_price = getAveragePrice(filtered_prices[1])
                            #plot(filtered_prices[1], average_price, results)
                            all_models_and_average.append((model, storage, carrierName, conditionName, average_price))
                        except Exception as e:
                            all_models_and_average.append((model, storage, carrierName, conditionName, e))
                    else:
                        all_models_and_average.append((model, storage, carrierName, conditionName, "**NOT ENOUGH RESULTS**"))
                except Exception as e:
                    print(e)
                pbar.update(n=1)

writeCSV(all_models_and_average, 'model.csv')







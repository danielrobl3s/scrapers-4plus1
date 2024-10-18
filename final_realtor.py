from cdriver import Driver
import time
from bs4 import BeautifulSoup
from lxml import etree
import random
from csv import DictWriter

driver = Driver.get('https://www.realtor.com/propertyrecord-search/Hayden_ID/E-Arena-Loop', cookies=True)

html_content = driver.page_source

# Parse the HTML with BeautifulSoup using 'lxml' parser
soup = BeautifulSoup(html_content, 'lxml')

# Convert BeautifulSoup object to lxml etree
dom = etree.HTML(str(soup))

# Use XPath to get all <a> tags
a_tags = dom.xpath('//a[starts-with(@href, "/propertyrecord-search/Hayden_ID/")]/@href')
for tag in a_tags:
   print(tag)

for tag in a_tags:
    d = Driver.get(str(tag), cookies=True)
    time.sleep(4)
    html_content_ = d.page_source
    soup_ = BeautifulSoup(html_content_, 'lxml')
    
    dom_ = etree.HTML(str(soup_))

    a_tags_ = dom_.xpath('//a[starts-with(@href, "https://www.realtor.com/realestateandhomes-detail/")]/@href')
    
    for tag_ in a_tags_:
        d = Driver.get(str(tag_), cookies=True)

        time.sleep(random.randint(1, 5))

        html_content__ = d.page_source

        soup = BeautifulSoup(html_content__, 'lxml')

        dom = etree.HTML(str(soup))
        
        title = dom.xpath('//h1//text()')

        price = dom.xpath('(//div[@data-testid="ldp-list-price"]//text())[1]')

        beds = dom.xpath('(//ul[@class="PropertyMetastyles__StyledPropertyMeta-rui__sc-1g5rdjn-0 fcA-DfD sc-79f365fd-1 kiccaE"]//li//text())[1]')

        baths = dom.xpath('(//ul[@class="PropertyMetastyles__StyledPropertyMeta-rui__sc-1g5rdjn-0 fcA-DfD sc-79f365fd-1 kiccaE"]//li//text())[3]')

        sqft = dom.xpath('(//ul[@class="PropertyMetastyles__StyledPropertyMeta-rui__sc-1g5rdjn-0 fcA-DfD sc-79f365fd-1 kiccaE"]//li//text())[5]')

        sqft_lot = dom.xpath('(//ul[@class="PropertyMetastyles__StyledPropertyMeta-rui__sc-1g5rdjn-0 fcA-DfD sc-79f365fd-1 kiccaE"]//li//text())[8]')

        property_type = dom.xpath('(//p[@class="base__StyledType-rui__sc-108xfm0-0 jiKtVG sc-2c9812a2-2 eFLSTd listing-key-fact-item-value"])[1]//text()')

        price_per_sqft = dom.xpath('(//p[@class="base__StyledType-rui__sc-108xfm0-0 jiKtVG sc-2c9812a2-2 eFLSTd listing-key-fact-item-value"])[3]//text()')

        year_built = dom.xpath('(//p[@class="base__StyledType-rui__sc-108xfm0-0 jiKtVG sc-2c9812a2-2 eFLSTd listing-key-fact-item-value"])[5]//text()')

        
        with open('houses.csv', 'w', newline='', encoding='utf-8') as f:
            writer = DictWriter(f, fieldnames=['address', 'price', 'beds', 'baths', 'sqft', 'sqft_lot', 'property_type', 'price_per_sqft', 'year_built'])
            writer.writeheader()
            writer.writerow({'address': title, 'price': price, 'beds': beds, 'baths': baths, 'sqft': sqft, 'sqft_lot': sqft_lot, 'property_type': property_type, 'price_per_sqft': price_per_sqft, 'year_built': year_built})
import csv
import requests
import json
from fake_useragent import UserAgent

#ua = UserAgent(browsers=['firefox', 'chrome', 'opera', 'edge'])
#user_agent = ua.random
#headers = {
#   'user-agent': user_agent
#}

#parameters = {"client_id": "rdc-search-new-communities",
#              "schema": "vesta"}

#url = "https://www.realtor.com/api/v1/rdc_search_srp?client_id=rdc-search-new-communities&schema=vesta"
#payload = """ {"query":"\n  query TransformCommunitySearch($query: CommunitySearchCriteria!, $limit: Int) {\n    community_search(query: $query, limit: $limit) {\n      count\n      total\n      results {\n        source {\n          id\n        }\n        community_metrics {\n          leads_month_to_date\n        }\n        builder {\n          builder_id\n          href\n          name\n          source_builder_id\n          logo {\n            href\n          }\n        }\n        property_id\n        description {\n          name\n          baths_min\n          baths_max\n          beds_max\n          beds_min\n          sqft_max\n          sqft_min\n        }\n        location {\n          address {\n            city\n            state_code\n            postal_code\n          }\n        }\n        list_price_max\n        list_price_min\n        primary_photo(https:true) {\n          description\n          href\n        }\n        photos(limit: 5, https: true) {\n          href\n        }\n        permalink\n      }\n    }\n  }\n","variables":{"query":{"sales_builder":true,"search_location":{"location":"Coeur dAlene, ID","buffer":20}},"limit":200},"nrQueryType":"PREMIUM_CARD_SRP","isClient":true,"visitor_id":"a045e905-7751-4deb-9248-d2d884894e38"} """

#response = requests.post(url, data=payload, headers=headers, params=parameters)

#print(response)

url = "https://www.realtor.com/api/v1/rdc_search_srp?client_id=rdc-search-new-communities&schema=vesta"

payload = json.dumps({
  "query": "\n  query TransformCommunitySearch($query: CommunitySearchCriteria!, $limit: Int) {\n    community_search(query: $query, limit: $limit) {\n      count\n      total\n      results {\n        source {\n          id\n        }\n        community_metrics {\n          leads_month_to_date\n        }\n        builder {\n          builder_id\n          href\n          name\n          source_builder_id\n          logo {\n            href\n          }\n        }\n        property_id\n        description {\n          name\n          baths_min\n          baths_max\n          beds_max\n          beds_min\n          sqft_max\n          sqft_min\n        }\n        location {\n          address {\n            city\n            state_code\n            postal_code\n          }\n        }\n        list_price_max\n        list_price_min\n        primary_photo(https:true) {\n          description\n          href\n        }\n        photos(limit: 5, https: true) {\n          href\n        }\n        permalink\n      }\n    }\n  }\n",
  "variables": {
    "query": {
      "sales_builder": True,
      "search_location": {
        "location": "Coeur dAlene, ID",
        "buffer": 20
      }
    },
    "limit": 200
  },
  "nrQueryType": "PREMIUM_CARD_SRP",
  "isClient": True,
  "visitor_id": "a045e905-7751-4deb-9248-d2d884894e38"
})

headers = {
  'Content-Type': 'application/json',
  'Cookie': '__bot=false; __vst=1d123bee-8f4c-416d-8446-fee8b64d9459; split=n; split_tcv=175'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

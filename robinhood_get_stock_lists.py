import json
import time
from pathlib import Path

import requests

def retrieve_robinhood_list_stocks(midlands_lists_json_file):
    with open(midlands_lists_json_file, 'r') as list_data:
        data = json.load(list_data)

    Path("robinhood_stocks").mkdir(exist_ok=True)
    count = 0

    for listing in data:
        for stock in data[listing]:
            if stock.get("object_type") == "instrument":
                stock_uuid = stock.get("object_id", '')

                r = requests.get("https://api.robinhood.com/instruments/" + stock_uuid)
                response_data = r.json()

                simple_name = response_data.get("simple_name", "")
                # handle case where simple_name missing from data
                if not simple_name:
                    simple_name = response_data.get("name", "")

                print("Saving {} , {} to json".format(stock_uuid, simple_name))
                count +=1

                with open("robinhood_stocks/{}_{}.json".format(simple_name, stock_uuid), 'w') as outfile:
                    json.dump(response_data, outfile, indent=2)

                # sleep between requests, for good measure
                time.sleep(0.5)
    print("%d total stocks downloaded from user-generated lists on robinhood." % count)

retrieve_robinhood_list_stocks("robinhood_list_items.json")

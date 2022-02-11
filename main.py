import json
import time

# custom packages
import util
import thn_api as thnapi

# MAIN FUNCTION CALLS:

pre_hour = -1
pre_data = []

while(True):
    ctime = util.current_time()

    if ctime["hour"] != pre_hour:
        pre_hour = ctime["hour"]

        data = thnapi.get_thn_data()

        new_data = [x for x in data if x not in pre_data]

        if len(new_data) > 0:
            for i in new_data:
                pre_data.append(i)
        
            # TODO:
            print(json.dumps(new_data, indent=4))
            print("Length:", len(new_data))

    time.sleep(1)


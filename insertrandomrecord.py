import requests
import logging
import random
import datetime
import json
_featureLayerUrl = "https://services2.arcgis.com/YDRnp3rdop6mVcUC/arcgis/rest/services/DummyPoints/FeatureServer/0"
_APIKey= "AAPTxy8BH1VEsoebNVZXo8HurKpRLeI1EqCfHj0jJkB6oyEl5aJ4I-jJlShQnRFGZe1unEOthj0B1ja8orFK8tpBRtrLT9ewhPnOK3cs6iXbaGXWm0Q8EDiPAa9HIQVXlEEtu9FuGU4UBQDKPqDw3n3e7BsDsfpY6Qokqzdg0_KsI6VLjl8t7Zb69WGpN-YRRraQhmxE1uox87ELhZkNq_yTWQ..AT1_gG0KDOg3"

def main():
    logging.basicConfig(level=logging.DEBUG)

    logging.info("Start")

    #determine random lat an long
    lat,lon = CreateRandomLatLon()
    logging.info(f"Random lat: {lat}, lon: {lon}")

    #create feature to insert
    feature = {
        "attributes": {
            "NAME": "Random",
            "DESCRIPTION": "Random description",
            "ITEMTYPE": "FromScript1",
            "DUMMYDATE": round(datetime.datetime.now().timestamp()*1000)
        },
        "geometry":{
            "x": lon,
            "y": lat,
            "spatialReference": {
                "wkid": 4326
            }
        }
    }

    #insert feature
    response = requests.post(f"{_featureLayerUrl}/addFeatures", {"features": json.dumps([feature]), "f": "json","token":_APIKey	})
    logging.info(f"Response: {response.text}")
    logging.info("End")

        
    

    

def CreateRandomLatLon():
    
    return (random.uniform(51.0, 53.0), random.uniform(4.0, 6.0))

if __name__ == "__main__":
    main()
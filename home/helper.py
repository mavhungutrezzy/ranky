import pandas as pd
from home.models import FoodPlace
from sodapy import Socrata
import requests

from dotenv import load_dotenv
import os


load_dotenv()


API_KEY = os.getenv("API_KEY")
client = Socrata("data.sfgov.org", None)


def query_data():

    food_places = client.get("pyih-qa8i", limit=1000)

    # turn food_places into a dataframe and drop empty rows
    df = pd.DataFrame.from_records(food_places)
    df = df.dropna()

    # turn the dataframe into a list of dictionaries
    food_places_dict = df.to_dict("records")

    return [
        {
            "business_id": i["business_id"],
            "business_name": i["business_name"],
            "address": i["business_address"],
            "inspection_type": i["inspection_type"],
            "inspection_score": i["inspection_score"],
            "phone": i["business_phone_number"],
            "risk_category": i["risk_category"],
            "violation_description": i["violation_description"],
        }
        for i in food_places_dict
    ]


# add the data to the database
def add_data():
    food_places = query_data()
    for i in food_places:
        FoodPlace.objects.create(**i)


def photos_request():

    photos_request = requests.get(
        "https://pixabay.com/api/",
        params={
            "key": API_KEY,
            "q": "restaurant+food",
            "image_type": "photo",
            "category": "food",
            "page": 5,
            "per_page": 100,
        },
    )

    results = photos_request.json()

    return [hit["webformatURL"] for hit in results["hits"]]

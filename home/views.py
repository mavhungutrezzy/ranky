import json
import os

import numpy as np
import pandas as pd
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from dotenv import load_dotenv
from sodapy import Socrata

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


client = Socrata("data.sfgov.org", None)


def photos_request():

    photos_request = requests.get(
        "https://pixabay.com/api/",
        params={
            "key": key,
            "q": "restaurant+food",
            "image_type": "photo",
            "category": "food",
            "page": 5,
            "per_page": 100,
        },
    )

    results = photos_request.json()

    return [hit["webformatURL"] for hit in results["hits"]]


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


def home(request):

    places = query_data()
    photos = photos_request()

    length = len(places)

    page = request.GET.get("page", 1)

    paginator = Paginator(places, 20)

    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages)

    context = {
        "food_places": places,
        "photos": photos,
        "len": length,
    }

    return render(request, "home.html", context)


def detail(request):
    places = query_data()
    photos = photos_request()
    context = {
        "food_places": places[:4],
        "photos": photos,
    }
    return render(request, "detail.html", context)

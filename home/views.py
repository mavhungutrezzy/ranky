import json
import os
from http import HTTPStatus
from os.path import dirname, join

import numpy as np
import pandas as pd
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from dotenv import load_dotenv
from sodapy import Socrata

load_dotenv()


client = Socrata("data.sfgov.org", None)


def photos_request():
    key = os.getenv("API_KEY")

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


@cache_page(60 * 15)
def home(request):

    food_places = client.get("pyih-qa8i", limit=250)

    df = pd.DataFrame.from_records(food_places)
    df = df.dropna()

    # turn the dataframe into a list of dictionaries
    food_places_dict = df.to_dict("records")

    food_places = [
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

    food_places = query_data()
    photos = photos_request()

    length = len(food_places)

    page = request.GET.get("page", 1)

    paginator = Paginator(food_places, 20)

    try:
        food_places = paginator.page(page)
    except PageNotAnInteger:
        food_places = paginator.page(1)
    except EmptyPage:
        food_places = paginator.page(paginator.num_pages)

    context = {
        "food_places": food_places,
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

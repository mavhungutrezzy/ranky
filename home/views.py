from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from home.helper import add_data, photos_request
import random
from home.models import FoodPlace, Comment
from django.contrib.auth.decorators import login_required

# @cache_page(60 * 15)
def home(request):

    if request.method == "POST":
        if not (search := request.POST.get("search_term")):
            return render(
                request, "home.html", {"error": "Please enter a valid search term."}
            )

        places = FoodPlace.objects.filter(business_name__icontains=search)
        photos = photos_request()
        context = {
            "food_places": places,
            "photos": photos,
            "search_term": search,
            "len": len(places),
        }
        return render(request, "home.html", context)
    if FoodPlace.objects.count() == 0:
        add_data()

    places = FoodPlace.objects.all()
    all_places = places
    length = len(places)
    photos = photos_request()
    paginator = Paginator(places, 40)
    page = request.GET.get("page")
    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages)

    context = {
        "all_places": all_places,
        "food_places": places,
        "photos": photos,
        "len": length,
    }

    return render(request, "home.html", context)


def detail(request, place_id):

    place = FoodPlace.objects.get(id=place_id)
    comments = Comment.objects.filter(foodplace=place)
    places = FoodPlace.objects.all()
    places_list = list(places)
    random_places = random.sample(places_list, 4)
    photos = photos_request()
    context = {
        "food_places": random_places,
        "photos": photos,
        "place": place,
        "comments": comments,
    }
    return render(request, "detail.html", context)


@login_required
def add_comment(request, place_id):
    if request.method == "POST":
        if comment := request.POST.get("comment"):
            Comment.objects.create(
                foodplace=FoodPlace.objects.get(id=place_id),
                user=request.user,
                comment=comment,
            )
    return redirect("detail", place_id=place_id)


@login_required
def update_comment(request, place_id, comment_id):
    if request.method == "POST":
        if comment := request.POST.get("comment"):
            Comment.objects.filter(id=comment_id).update(comment=comment)
    return redirect("detail", place_id=place_id)    



from django.shortcuts import render
from app.models import Users
from app.forms import InputUser


def index(request):
    if request.method == "POST":
        form = InputUser(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return database(request)
    return render(request, "app/index.html")

def database(request):
    users = Users.objects.all()
    dict = {"users" : users}
    return render(request, "app/database.html", context=dict )


def input(request):
    form = InputUser()
    if request.method == "POST":
        form = InputUser(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return database(request)

        else:
            dict = {"error":"Error form invalid!"}
            return render(request, "app/input.html", context = dict)


    return render(request, "app/input.html",{"form":form})

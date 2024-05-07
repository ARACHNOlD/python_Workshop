
# Create your views here.


from django.http import HttpResponse


def home(request):
    return HttpResponse("You are at home page")


def about(request):
    return HttpResponse('You are at about page')


def contact(request):
    return HttpResponse('You are at contact page')


def question(request):
    return HttpResponse("what is your name")


def answer(request):
    return HttpResponse("My name is Sumit ")

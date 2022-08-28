from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Главная страница</h1>')

def group_posts(request):
    return HttpResponse('Список блогов')


from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Список групп')

def group_posts_detail(request):
    return HttpResponse('Информация о блоге')
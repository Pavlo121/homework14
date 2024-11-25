from django.http import HttpResponse

def home(request):
    return HttpResponse("Ласкаво просимо на головну сторінку.")

def about(request):
    return HttpResponse("Сторінка про нас")

def contact(request):
    return HttpResponse("Зв'яжіться з нами")

def post_view(request, id):
    return HttpResponse(f"Ви переглядаєте ID: {id}")

def profile_view(request, username):
    return HttpResponse(f"Ви переглядаєте профіль користувача: {username}")

def event_view(request, year, month, day):
    return HttpResponse(f"Дата події: {year}-{month}-{day}")


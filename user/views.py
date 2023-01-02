from user.models import User
from django.http import HttpResponse


def index(request):
    users = User.objects.all()
    res = '<h1>All users</h1>'
    for item in users:
        res += f'<div><p>{item.first_name}</p></div>'
    return HttpResponse(res)

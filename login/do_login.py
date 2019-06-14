from django.shortcuts import render
from django.views.decorators import csrf


def do_login(request):
    ctx = {}
    if request.POST:
        ctx['result'] = request.POST
        print(ctx)
    return render(request, 'post.html', ctx)

from django.shortcuts import render ,redirect


def base(request):

    return render(request,"app/base22.html",locals())  
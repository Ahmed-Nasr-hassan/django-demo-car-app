from django.shortcuts import render


def renderHtml(request):
    user_dict={'users':[{'name':'ahmed','age':27,'salary':1000},{'name':'nasr','age':20,'salary':2000},{'name':'hassan','age':50,'salary':500},]}
    return render(request,'app2/index.html',user_dict)

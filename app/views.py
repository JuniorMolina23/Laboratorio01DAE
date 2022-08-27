from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la vista app!")

def suma(request, n1 ,n2):
    rep = n1 + n2
    rq = "la suma de ",str(n1)," + ",str(n2)," = ",str(rep)
    return HttpResponse(rq)

def resta(request, n1 ,n2):
    rep = n1 - n2
    rq = "la resta de ",str(n1)," - ",str(n2)," = ",str(rep)
    return HttpResponse(rq)

def mul(request, n1 ,n2):
    rep = n1 * n2
    rq = "El producto de ",str(n1)," * ",str(n2)," = ",str(rep)
    return HttpResponse(rq)

def div(request, n1 ,n2):
    rep = n1 / n2
    rq = "La division de ",str(n1)," / ",str(n2)," = ",str(rep)
    return HttpResponse(rq)
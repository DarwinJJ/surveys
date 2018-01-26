from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
    return render (request, 'first_app/index.html')

def formprocess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Your Name": request.POST['name'],
        "Dojo Location": request.POST['dojolocation'],
        "Favorite Language": request.POST['favorlanguage'],
        "Comments": request.POST['comments']
    }
    return redirect('/showresults')

def showresults(request):
    print "Go to show results!"
    print request.session
    return render(request, 'first_app/result.html')

def goback(request):
    request.session
    return render(request, 'first_app/index.html')
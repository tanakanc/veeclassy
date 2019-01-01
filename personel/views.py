from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personel/home.html')

def contact(request):
    return render(request, 'personel/basic.html', {'content':['Line:@veeclassy (มี@นะคะ) ','IG : veeclassy314']})
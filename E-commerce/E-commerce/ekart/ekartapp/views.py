from django.shortcuts import render , redirect
from .models import Ekartcard
from .models import Productcard
from .forms import Bookingform
# Create your views here.
def index(request):
    ekartcard=Ekartcard.objects.all()
    context={'card':ekartcard}
    return render(request,'index.html',context)
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def products(request):
    productcard=Productcard.objects.all()
    context={'card':productcard}
    return render(request,'products.html',context)
def Booking(request):
    if request.method=='POST':
        forms= Bookingform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    forms=Bookingform()
    book={
    'form':forms
    }    
    return render(request,'booking.html',book)


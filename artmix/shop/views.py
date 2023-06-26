from django.shortcuts import render
from shop.models import Frame

# Create your views here.
def main(request):
    return render(request, "shop/index.html")
    
def frame(request):
    data = {
        'frames' : Frame.objects.all()
    }
    print(Frame.objects.all())
    return render(request, "shop/frame.html", data)

def shop(request):
    return render(request, "shop/shop.html")

def picture(request):
    return render(request, "shop/picture.html")

def contact(request):
    return render(request, "shop/contact.html")

def about(request):
    return render(request, "shop/about.html")
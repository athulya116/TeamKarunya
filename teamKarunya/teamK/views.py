from django.shortcuts import render
from .models import HomeSliderImage, HomePageGallery,ServicesPage, GalleryImage, SiteLogo

# Create your views here.


def index(request):
    slider = HomeSliderImage.objects.first()  # only one row
    gallery = HomePageGallery.objects.first()  # only one row
    return render(request, "teamK/index.html", {"slider": slider, "homegallery": gallery})


def gallery(request):
    ambulance_images = GalleryImage.objects.filter(category="ambulance")
    event_images = GalleryImage.objects.filter(category="event")
    return render(request, "teamK/gallery.html", {
        "ambulance_images": ambulance_images,
        "event_images": event_images,
    })

def about(request):
    return render(request,'teamK/about.html')

def contact(request):
    return render(request,'teamK/contact.html')

def services(request):
    service_images = ServicesPage.objects.first()  # Only one row
    return render(request, 'teamK/services.html', {"service_images": service_images})

def site_logo(request):
    logo = SiteLogo.objects.first()
    return {"site_logo": logo}

def custom_404(request, exception):
    return render(request, "teamK/404.html", status=404)



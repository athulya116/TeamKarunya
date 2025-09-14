from django.db import models

# Create your models here.


class HomeSliderImage(models.Model):
    image1 = models.ImageField(upload_to="slider/", blank=True, null=True)
    image2 = models.ImageField(upload_to="slider/", blank=True, null=True)
    image3 = models.ImageField(upload_to="slider/", blank=True, null=True)

    def __str__(self):
        return "Home Page Slider"
    
class HomePageGallery(models.Model):
    image1 = models.ImageField(upload_to="Homegallery/", blank=True, null=True)
    image2 = models.ImageField(upload_to="Homegallery/", blank=True, null=True)
    image3 = models.ImageField(upload_to="Homegallery/", blank=True, null=True)
    image4 = models.ImageField(upload_to="Homegallery/", blank=True, null=True)

    def __str__(self):
        return "Home Page Gallery"
    
class ServicesPage(models.Model):
    ambulance_image = models.ImageField(upload_to="services/", blank=True, null=True)
    mortuary_image = models.ImageField(upload_to="services/", blank=True, null=True)
    event_image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return "Services Page Images"
    

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ("ambulance", "Ambulance Services"),
        ("event", "Event Services"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return f"{self.category} - {self.id}"
    
class SiteLogo(models.Model):
    logo = models.ImageField(upload_to="logo/")
    
    def __str__(self):
        return "Website Logo"
from django.contrib import admin
from .models import HomeSliderImage, HomePageGallery, ServicesPage, GalleryImage, SiteLogo

admin.site.register(HomeSliderImage)
admin.site.register(HomePageGallery)
admin.site.register(ServicesPage)
admin.site.register(SiteLogo)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "image")
    list_filter = ("category",)





# from django.contrib import admin
# from .models import HomeSliderImage,HomePageGallery,ServicesPage,GalleryImage, SiteLogo

# admin.site.register(HomeSliderImage)
# admin.site.register(HomePageGallery)
# admin.site.register(ServicesPage)
# admin.site.register(SiteLogo)

# @admin.register(GalleryImage)
# class GalleryImageAdmin(admin.ModelAdmin):
#     list_display = ("id", "category", "image")
#     list_filter = ("category",)
    

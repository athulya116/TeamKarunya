from .models import SiteLogo

def site_logo(request):
    """Return the site logo object globally."""
    logo = SiteLogo.objects.first()  # get the first (or only) logo
    return {"site_logo": logo}

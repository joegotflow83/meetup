from django.views.generic import TemplateView


class Home(TemplateView):
    """Home page when users login"""
    template_name = 'home/home.html'

from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse

from .models import Group


class Home(TemplateView):
    """Home page when users login"""
    template_name = 'home/home.html'


class CreateGroup(CreateView):
    """Users can create groups"""
    model = Group
    fields = ('name', 'description', 'location', 'meet_date', 'meet_time')

    def form_valid(self, form):
        new_group = form.save(commit=False)
        new_group.user = self.request.user
        new_group.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

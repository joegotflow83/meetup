from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse

from .models import Group


class Home(TemplateView):
    """Home page when users login"""
    template_name = 'home/home.html'


class CreateGroup(CreateView):
    """Users can create groups"""
    model = Group
    fields = ('name', 'description')

    def form_valid(self, form):
        new_group = form.save(commit=False)
        new_group.user = self.request.user
        new_group.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class UserViewGroups(ListView):
    """User can view the groups they have created"""
    model = Group

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)


class GroupDetails(DetailView):
    """Users can view the groups with all the events they have created with that group"""
    model = Group

    def get_queryset(self):
        return Group.objects.get(pk=self.kwargs['pk'])

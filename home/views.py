from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse

from .models import Group, Event


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


class GroupDetail(DetailView):
    """Users can view groups in detail"""
    model = Group

    def get_queryset(self):
        return Group.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(group=self.kwargs['pk'])
        return context


class CreateEvent(CreateView):
    """Users can create events for a particular group"""
    model = Event
    fields = ('name', 'location', 'meet_date', 'meet_time')

    def form_valid(self, form):
        new_event = form.save(commit=False)
        new_event.user = self.request.user
        group = Group.objects.get(pk=self.kwargs['pk'])
        new_event.group = group
        new_event.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('group_detail', kwargs={'pk': self.kwargs['pk']})

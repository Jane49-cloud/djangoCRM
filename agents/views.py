from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
import random


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "Agents.html"
    queryset = Agent.objects.all()
    context_object_name = "agents"


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "Agents-create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy('agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password(f"{random.randint(0, 10000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = "agent-details.html"
    queryset = Agent.objects.all()
    context_object_name = 'agent'


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Agent
    template_name = "Agent_update.html"
    form_class = AgentModelForm
    success_url = reverse_lazy('agent-list')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    queryset = Agent.objects.all()
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('agent_list')

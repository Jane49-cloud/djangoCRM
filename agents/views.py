from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "Agents.html"
    queryset = Agent.objects.all()
    context_object_name = "agents"


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "Agents-create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy('agent_list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = "agent-details.html"
    queryset = Agent.objects.all()
    context_object_name = 'agent'


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Agent
    template_name = "Agent_update.html"
    form_class = AgentModelForm
    success_url = reverse_lazy('agent_list')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    queryset = Agent.objects.all()
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('agent_list')

from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm, UserCustomForm


def landing_page(request):
    return render(request, "landing.html")


class SignupView(CreateView):
    template_name = "signup.html"
    form_class = UserCustomForm
    success_url = reverse_lazy('login')


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailsView(LoginRequiredMixin, DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm
    success_url = reverse_lazy('lead_list')

    def form_valid(self, form):
        send_mail(
            subject="A new lead has been created",
            message="Go to the site and view the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com", "janendirangu49@gmail.com"]

        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    template_name = "lead_update.html"
    form_class = LeadModelForm
    success_url = reverse_lazy('lead_list')


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Lead.objects.all()
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('lead_list')

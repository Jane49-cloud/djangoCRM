"""djcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from leads.views import LeadListView, LeadDetailsView, LeadCreateView, LeadUpdateView, LeadDeleteView, SignupView, landing_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing-page"),
    path('leads/all/', LeadListView.as_view(), name="lead_list"),
    path('leads/create/', LeadCreateView.as_view(), name="create_lead"),
    path('leads/<int:pk>/', LeadDetailsView.as_view(), name="lead_details"),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name="lead_update"),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='delete_lead'),
    # TODO Auth urls
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout")
]

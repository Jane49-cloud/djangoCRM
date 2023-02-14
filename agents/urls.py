from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailsView, AgentUpdateView, AgentDeleteView

app_name = "agents"
urlpatterns = [
    path("", AgentListView.as_view(), name="agent_list"),
    path("create/", AgentCreateView.as_view(), name="create_agent"),
    path("<int:pk>/details/", AgentDetailsView.as_view(), name="agent_details"),
    path("<int:pk>/update/", AgentUpdateView.as_view(), name="update_agent"),
    path("<int:pk>/delete/", AgentDeleteView.as_view(), name="delete_agent"),

]

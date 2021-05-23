from django.urls import path
from .views import BranchesList, hello, BranchesAuto


urlpatterns = [
    path('', hello),
    path('branches/', BranchesList.as_view()),
    path('branches/autocomplete', BranchesAuto.as_view())
]
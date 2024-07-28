from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"person", views.PersonViewSet)
router.register(r"question", views.QuestionViewSet)
router.register(r"help", views.HelpViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('help/amount', views.help_count)
]

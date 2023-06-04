from django.urls import path,include
from rest_framework import routers
from.views import TaskViewset

router = routers.DefaultRouter()
router.register(r'Task',TaskViewset)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import TaskViewSet
from .views import ActivityViewSet

router=DefaultRouter()
router.register("Task",TaskViewSet )
router.register("Activity",ActivityViewSet )

urlpatterns= [
    path("" , include(router.urls))

    
]

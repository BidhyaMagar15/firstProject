from django.urls import path, includes 
from rest_framework.routes import DefaultRouter 
from .views import TaskViewSet

router=DefaultRouter()
router.register("tasks",TaskViewSet )

urlpatterns= [
    path{"" , include(router.urls)}

    
]

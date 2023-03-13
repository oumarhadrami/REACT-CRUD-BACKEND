from django.urls import include, path 
from tutorials import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.TutorialsView, basename="tutorials")
 
urlpatterns = [ 
    path('', include(router.urls)),
]
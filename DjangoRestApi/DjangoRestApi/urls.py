from django.urls import include, path
 
urlpatterns = [ 
    path(r'api/tutorials/', include('tutorials.urls')),
]
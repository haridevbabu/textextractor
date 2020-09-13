# basic URL Configurations
from django.urls import include, path
# import routers 
from rest_framework import routers
from textextract .views import ExtractTextView
from textextract import views

# define the router 
router = routers.DefaultRouter()

# define the router path and viewset to be used 
router.register(r'api', ExtractTextView)

# specify URL Path for rest_framework 
urlpatterns = [
    path('api/', include(router.urls),name='api'),
    path('',views.gettext)

] 

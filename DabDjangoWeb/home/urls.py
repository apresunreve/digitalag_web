from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('submit/', views.submit_form, name='submit_form'),
    path('login/google/', views.google_login, name='google-login'),
    path('login/google/callback/', views.google_callback, name='google-callback'),
    path('logout', views.logout),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
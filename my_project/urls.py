
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
    name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

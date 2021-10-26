from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail_view'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
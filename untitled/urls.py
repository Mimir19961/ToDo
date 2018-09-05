from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('blog/', RedirectView.as_view(url='/todo/', permanent=True)),
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]

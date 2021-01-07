"""planters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import LoginView, LogoutView, SignUpView
from journal.views import CreateEntryView
from myuser.views import index_view, profile, edit_profile
from indoorplants.views import PlantView, LibraryView, add_plant, remove_plant, edit_plant


urlpatterns = [
    path('', index_view, name="homepage"),
    path('add_plant/<int:plant_id>/', add_plant, name='add_plant'),
    path('all_plants/', LibraryView.as_view(), name='library'),
    path('admin_site/', admin.site.urls),
    path('edit/<str:username>/', edit_profile, name='edit_profile'),
    path('journal_entry/<int:plant_id>/', CreateEntryView.as_view(), name='new_entry'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('edit_plant/<int:plant_id>/', edit_plant, name='edit_plant'),
    path('plant/<int:plant_id>/', PlantView.as_view(), name='plant'),
    path('remove_plant/<int:plant_id>/', remove_plant, name='remove_plant'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('<str:username>/', profile, name='profile'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

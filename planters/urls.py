# from plantcalendar import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import LoginView, LogoutView, SignUpView
from plantcalendar.views import CalendarView, CreateCalEntry
from journal.views import CreateEntryView, remove_entry
from myuser.views import index_view, profile, edit_profile
from indoorplants.views import PlantView, LibraryView, add_plant, remove_plant, edit_plant


urlpatterns = [
    path('', index_view, name="homepage"),
    path('add_plant/<int:plant_id>/', add_plant, name='add_plant'),
    path('admin_site/', admin.site.urls),
    path('all_plants/', LibraryView.as_view(), name='library'),
    path('calendar/', CalendarView.as_view(), name="calendar"),
    path('calendar/entry', CreateCalEntry.as_view(), name="calendar_entry"),
    path('calendar/edit/<int:entry_id>/', CreateCalEntry.as_view(), name="edit_entry"),
    path('edit/<str:username>/', edit_profile, name='edit_profile'),
    path('edit_plant/<int:plant_id>/', edit_plant, name='edit_plant'),
    path('journal_entry/<int:plant_id>/', CreateEntryView.as_view(), name='new_entry'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('plant/<int:plant_id>/', PlantView.as_view(), name='plant'),
    path('remove_plant/<int:plant_id>/', remove_plant, name='remove_plant'),
    path('remove_entry/<int:entry_id>/', remove_entry, name='remove_entry'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('<str:username>/', profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

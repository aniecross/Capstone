# from plantcalendar import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import LoginView, LogoutView, SignUpView
from plantcalendar.views import CalendarView
from plantcalendar.views import index
from plantcalendar.views import create_task
from plantcalendar.views import TaskEdit
from plantcalendar.views import task_details
from plantcalendar.views import add_plantmember
from plantcalendar.views import PlantMemberDeleteView
from journal.views import CreateEntryView, remove_entry
from myuser.views import index_view, profile, edit_profile, delete_profile
from indoorplants.views import PlantView, LibraryView, add_plant, remove_plant, edit_plant


urlpatterns = [
    path('', index_view, name="homepage"),
    path('index/', index, name="index"),
    path('calendar/', CalendarView.as_view(), name="calendar"),
    path('add_plant/<int:plant_id>/', add_plant, name='add_plant'),
    path('all_plants/', LibraryView.as_view(), name='library'),
    path('admin_site/', admin.site.urls),
    path('edit/<str:username>/', edit_profile, name='edit_profile'),
    path('journal_entry/<int:plant_id>/', CreateEntryView.as_view(),
         name='new_entry'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('edit_plant/<int:plant_id>/', edit_plant, name='edit_plant'),
    path('plant/<int:plant_id>/', PlantView.as_view(), name='plant'),
    path('remove_plant/<int:plant_id>/', remove_plant, name='remove_plant'),
    path('remove_entry/<int:entry_id>/', remove_entry, name='remove_entry'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('<str:username>/', profile, name='profile'),
    path('task/new/', create_task, name='task_new'),
    path('task/edit/<int:pk>/', TaskEdit.as_view(), name='task_edit'),
    path('task/<int:task_id>/details/', task_details, name='task-detail'),
    path('add_plantmember/<int:task_id>',
         add_plantmember, name='add_plantmember'),
    path('task/<int:pk>/remove',
         PlantMemberDeleteView.as_view(), name="remove_task"),
    path('delete_profile/<int:user_id>/', delete_profile, name='delete_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

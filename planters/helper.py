from django.contrib.sessions.models import Session
from django.utils import timezone
from myuser.models import MyUser

def get_current_user():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    user = MyUser.objects.get(id=user_id_list[0])
    return user
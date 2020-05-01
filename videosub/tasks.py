from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.contrib.sessions.models import Session
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta,datetime
from videosub.models import member_record,membership,subscription
from django.utils import timezone

@shared_task
def check_membership():
    m = member_record.objects.all()
    s = subscription.objects.all()
    
    for i in m:
        remain_day = (abs(timezone.now() - i.last_date)).days
        i.remaining_days = remain_day
        i.save()
    
    # if subscription.objects.filter(uname = request.POST['uname']).exists(): 
    #     if .user_member.remaining_days == 0:
    #         j.active == False
    #         j.save()
    

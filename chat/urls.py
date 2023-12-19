from django.contrib import admin
from django.urls import path
from apscheduler.schedulers.background import BackgroundScheduler
import threading
from .views import *
from app.consumers import *
scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 3})
scheduler.start()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',cop)
]

scheduler.add_job( func=job1, trigger='interval', seconds=3)
scheduler.add_job( func=job2, trigger='interval', seconds=3)


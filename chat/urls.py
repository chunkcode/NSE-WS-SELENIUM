from django.contrib import admin
from django.urls import path
from apscheduler.schedulers.background import BackgroundScheduler
import threading
from .views import *
from app.consumers import *
scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 2})
# scheduler.start()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',cop)
]

# scheduler.add_job( func=cop, trigger='interval', seconds=1)

# scheduler.BaseEventLoop.run_forever()
# scheduler.start(job)

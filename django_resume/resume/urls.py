# Resume App URLs file
from django.conf.urls.defaults import *


urlpatterns = patterns('django_resume.resume.views',
    url(r'^$', 'index', name='resume_home'),
)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/user/(?P<user_id>[0-9]+)/$', views.getUser, name='getUser'),
<<<<<<< HEAD
    url(r'^api/user/n/$', views.createUser, name='createUser'),
    url(r'^api/user/all/$', views.getAllUsers, name='getAllUsers'),
    url(r'^api/job/(?P<job_id>[0-9]+)/$', views.getJob, name='getJob'),
    url(r'^api/job/n/$', views.createJob, name='createJob'),
    url(r'^api/job/all/$', view.getAllJobs, name='getAllJobs'),


=======
    url(r'^api/user/', views.getAllUsers, name='getAllUsers'),
    url(r'^api/job/', views.getAllJobs, name='getAllJobs'),
    url(r'^api/job/(?P<job_id>[0-9]+)/$', views.getJob, name='getJob'),
>>>>>>> master
]
from django.conf.urls import url
from student import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^majors/$', views.majors_list, name='majors_list'),
	url(r'^add_major/$', views.add_major, name='add_major'),
	url(r'^register_profile/$', views.register_profile, name='register_profile'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
	url(r'^profiles/$', views.profiles_list, name='profiles_list'),
	url(r'^print/report/$', views.report_document, name='report_document'),
	url(r'^print/grade/$', views.grade_document, name='grade_document'),
]
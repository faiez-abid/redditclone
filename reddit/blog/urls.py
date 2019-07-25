"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
url(r'^$', views.post_list, name='post_list'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.post_detail.as_view(), name='post_detail'),
    path('post/new/', views.PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit.as_view(), name='post_edit'),
    path('feedback/new/', views.FeedbackNew.as_view(), name='feedback_new'),
]

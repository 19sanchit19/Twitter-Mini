# created by me in the tweets folder

"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin							commented this 
# from django.urls import path								commented this
# from django.conf import settings							commented this
# from django.conf.urls.static import static				commented this
from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
        RetweetView,
		TweetCreateView,
		TweetDeleteView,
		TweetDetailView, 
		TweetListView,
		TweetUpdateView,
	) 
app_name='tweet'
urlpatterns = [
    # url(r'^admin/', admin.site.urls),						commented this
     url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]

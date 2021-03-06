# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from siteuser.users import views
from siteuser.settings import USING_SOCIAL_LOGIN

urlpatterns = patterns('',
    url(r'^account/login/$', views.SiteUserLoginView.as_view(), name='siteuser_login'),
    url(r'^account/register/$', views.SiteUserRegisterView.as_view(), name='siteuser_register'),
    url(r'^account/resetpw/step1/$', views.SiteUserResetPwStepOneView.as_view(), name='siteuser_reset_step1'),
    url(r'^account/resetpw/step1/done/$', views.SiteUserResetPwStepOneDoneView.as_view(), name='siteuser_reset_step1_done'),
    url(r'^account/resetpw/step2/done/$', views.SiteUserResetPwStepTwoDoneView.as_view(), name='siteuser_reset_step2_done'),
    url(r'^account/resetpw/step2/(?P<token>.+)/$', views.SiteUserResetPwStepTwoView.as_view(), name='siteuser_reset_step2'),
    url(r'^account/changepw/$', views.SiteUserChangePwView.as_view(), name='siteuser_changepw'),
    url(r'^account/changepw/done/$', views.SiteUserChangePwDoneView.as_view(), name='siteuser_changepw_done'),
    url(r'^account/logout/$', views.logout, name='siteuser_logout'),
)

if USING_SOCIAL_LOGIN:
    urlpatterns += patterns('',
        url(r'^account/oauth/(?P<sitename>\w+)/?$', views.social_login_callback),
    )
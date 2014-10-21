from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .views import *

urlpatterns = patterns('',
    url(r'^introductions?/(?P<slug>[\w-]+)/?$',
        login_required(EagleIntroductionDetailView.as_view()),
        name='eagle_introduction_detail'),
    url(r'^my/introduction/?$',
        login_required(EagleIntroductionCreateView.as_view()),
        name="eagle_add_intro"),
    url(r'^terms$',
        TemplateView.as_view(template_name="eagle_design/terms.html"),
        name="eagle_terms"),
    url(r'^about',
        TemplateView.as_view(template_name="eagle_design/about.html"),
        name="eagle_about"),
    url(r'^privacy',
        TemplateView.as_view(template_name="eagle_design/privacy.html"),
        name="eagle_privacy"),
    url(r'^[fF][aA][qQ]/?$',
        TemplateView.as_view(template_name="eagle_design/FAQ.html"),
        name="eagle_faq"),
    url(r'^resources',
        TemplateView.as_view(template_name="eagle_design/resources.html"),
        name="eagle_resources"),

    #
    # Django contrib.auth views
    #

    # login/logout
    url(r'^login/?$',
        'django.contrib.auth.views.login',
        {'template_name': 'eagle_design/login.html'},
        name='eagle_login'),
    url(r'^logout/?$',
        'django.contrib.auth.views.logout_then_login',
        name='eagle_logout'),

    # Password reset views
    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {
            'template_name': 'eagle_design/password_reset.html',
            'post_reset_redirect' : reverse_lazy('eagle_password_reset_done'),
        },
        name='password_reset'),
    url(r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'eagle_design/password_reset_done.html'},
        name='eagle_password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {
            'template_name': 'eagle_design/password_reset_confirm.html',
            'post_reset_redirect' : reverse_lazy('eagle_password_reset_complete'),
         },
        name='eagle_password_reset_confirm'),
    url(r'^reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'eagle_design/password_reset_complete.html'},
        name='eagle_password_reset_complete'),

    # Password Change
    url(r'^password_change/$',
        'django.contrib.auth.views.password_change',
        {
            'template_name': 'eagle_design/password_change.html',
            'post_reset_redirect' : reverse_lazy('eagle_password_change_done'),
         },
        name='eagle_password_change'),
    url(r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'eagle_design/password_change_done.html'},
        name='eagle_password_change_done'),


    url(r'^beta/gmail/install/?$', lambda x:HttpResponseRedirect('https://chrome.google.com/webstore/detail/introsto-introduction-hel/faboblafjncajbmcbdilliaigadmkijb')),
    url(r'^chrome$', lambda x:HttpResponseRedirect('https://chrome.google.com/webstore/detail/introsto-introduction-hel/faboblafjncajbmcbdilliaigadmkijb')),
    )

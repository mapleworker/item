from django.urls import include, re_path, path
from django.contrib import admin
from django.conf.urls import url
urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^users/', include(('users.urls','users'), namespace='users')),
    path(r'', include(('learning_logs.urls','learning_logs'), namespace='learning_logs')), 
    path(r'^captcha/', include(('captcha.urls','captcha'),namespace='captcha')),
    path(r'^captcha/', include(('captcha.urls','captcha'),namespace='captcha')),
    url(r'^captcha/', include('captcha.urls')),
    path(r'captcha/',include('captcha.urls')),
]


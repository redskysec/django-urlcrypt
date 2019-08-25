from django.urls import re_path, path, include
from apps.libraries.urlcrypt.conf import RUNNING_TESTS
from .views import login_redirect

app_name = 'app.libraries.urlcrypt'


urlpatterns = []
if RUNNING_TESTS:
    urlpatterns += [
        path(r'^test/view/$', 'test_view', name='urlcrypt_test_view'),  
        path(r'^test/view/(?P<username>.+)/$', 'test_view', name='urlcrypt_test_view_username'),  
    ]

urlpatterns += [
        path('<str:token>/', login_redirect, name='urlcrypt_redirect'),

]

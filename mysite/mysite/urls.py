from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello',hello_world),
    url(r'^form',form),
    url(r'^$',home),
    url(r'^post',post),
    url(r'^host/(?P<id>\d+)/$',post_detail, name='post_detail'),
    # 代表：抓出一個以上阿拉伯數字，並把抓出來的東西取名為 id。
)

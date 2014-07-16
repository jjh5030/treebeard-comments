from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treebeardcomments.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.home', name='home'),
	url(r'^post/(?P<post_id>\w+)/$', 'blog.views.single_post', name="single_post"),
)

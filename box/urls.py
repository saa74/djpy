from django.conf.urls import url
from box import views

urlpatterns = [
    url(r'^(?P<id_article>\d+)/$', views.article_singl, name='singl_article'),
    url(r'^tags/(?P<id_tag>\d+)/$', views.articles_tag, name='tag_articles'),
    url(r'^tags/', views.tags_list, name='list_tags'),
    url(r'^contacts/', views.contacts, name='contacts'),
]

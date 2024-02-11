from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .views import post_share, post_detail, post_list, post_comment
from .sitemaps import PostSitemap


app_name = 'blog'
sitemaps = {
    'posts': PostSitemap,
}



urlpatterns = [
# post views
#     path('', PostListView.as_view(), name='post_list'),
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
         post_list, name='post_list_by_tag'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail,
         name='post_detail'),
    path('<int:post_id>/share/',
         post_share, name='post_share'),
    path('<int:post_id>/comment/',
         post_comment, name='post_comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
           name='django.contrib.sitemaps.views.sitemap')
 ]


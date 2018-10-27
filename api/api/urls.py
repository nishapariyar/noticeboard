from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,DetailsView


urlpatterns = {

    url(r'^notice/$', CreateView.as_view(), name="create"),
    url(r'^notice/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

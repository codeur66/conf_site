from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView

from account.views import SignupView
try:
    import debug_toolbar
except ImportError:
    pass
import symposion.views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailimages.views.serve import ServeView as WagtailImageView

from cms.views import csrf_failure, LoginEmailView
from conf_site.reviews.views import (
    ReviewKeywordDetailView,
    ReviewKeywordListView)
from speakers.views import SpeakerListView, ExportAcceptedSpeakerEmailView


WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"

if settings.DEBUG:
    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)), ]
else:
    urlpatterns = []
urlpatterns += [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", LoginEmailView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),
    url(r"^api/", include("conf_site.api.urls")),
    url(r"^cms/", include(wagtailadmin_urls)),
    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(
        r"^images/([^/]*)/(\d*)/([^/]*)/[^/]*$",
        WagtailImageView.as_view(action="redirect"),
        name="wagtailimages_serve",
    ),
    url(r"^speaker/export/$",
        staff_member_required(ExportAcceptedSpeakerEmailView.as_view()),
        name="speaker_email_export"),
    url(r"^speaker/list/$", SpeakerListView.as_view(), name="speaker_list"),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^teams/", include("symposion.teams.urls")),
    url(r"^reviews/keyword/$",
        ReviewKeywordListView.as_view(),
        name="review_keyword_list"),
    url(r"^reviews/keyword/(?P<keyword_slug>[\w-]+)/$",
        ReviewKeywordDetailView.as_view(),
        name="review_keyword_detail"),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^403-csrf/", csrf_failure, name="403-csrf"),
    url(r"^413/", TemplateView.as_view(template_name="413.html")),
    url(r"", include(wagtail_urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

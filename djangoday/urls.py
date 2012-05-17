from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),

    url(r"^info/$", direct_to_template, {
        "template": "info.html",
    }, name="info"),

    url(r"^mapa/$", direct_to_template, {
        "template": "mapa.html",
    }, name="mapa"),

    url(r"^sponsors/$", direct_to_template, {
        "template": "sponsors.html",
    }, name="sponsors"),

    url(r"^agenda/$", direct_to_template, {
        "template": "agenda.html",
    }, name="agenda"),

    url(r"^organizadores/$", direct_to_template, {
        "template": "organizadores.html",
    }, name="organizadores"),

    url(r"^admin/invite_user/$",
        "pinax.apps.signup_codes.views.admin_invite_user",
        name="admin_invite_user"),

    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),

    url(r"^account/", include("pinax.apps.account.urls")),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )

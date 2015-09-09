from django.conf.urls import patterns, include, url

from koupons.views import IndexView, CouponDetailView, MyView, landing

urlpatterns = patterns('',
    
    #index con cupones
    #/
    url(r'^$', IndexView.as_view(), name='index'),
    #/coupons/servicios
    url(r'^servicios/$', IndexView.as_view(), name='servicios'),
    #/coupons/productos
    url(r'^productos/$', IndexView.as_view(), name='productos'),
    
    url(r'^(?P<slug>[-\w]+)/$', CouponDetailView.as_view()),
    url(r'^(?P<slug>[-\w]+)/hello.pdf', MyView.as_view()),

    #url(r'^accounts/register/$', RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    #url(r'^servicios/$', IndexView.as_view(), name='index'),
    #url(r'^productos/$', IndexView.as_view(), name='index'),
    

    #detalle de cupones

)

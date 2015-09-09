from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
#from django.contrib.auth.models import CustomUser
from koupons.models import CustomUser

import hashlib
import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import cache
from django.http import HttpResponse

#from tracdb import stats as trac_stats

from koupons.models import Coupon


from django.views.decorators.http import require_POST
from django.contrib.auth import views as auth_views


# Create your views here.
class IndexView(ListView):
   """docstring for IndexView"""
   template_name = 'index.html'
   model = Coupon

class CouponDetailView(DetailView):
   template_name = 'coupon_detail.html'
   model = Coupon

def landing(request):
   return render(request, "landing.html",)
	

@require_POST
@login_required(login_url='/accounts/login/')
def favorite_coupon(request, coupon_id):
    coupon = get_object_or_404(Coupon, pk=coupon_id)
    if request.user.favorites.filter(pk=coupon_id).exists():
        # user has already liked this company
        # remove like/user
        request.user.favorites.remove(coupon)
        message = 'You disliked this'
    else:
        # add a new like for a company
        request.user.favorites.add(coupon)
        message = 'You liked this'
    ctx = {'message': message}
    return redirect('user_profile', request.user.id)

@login_required
def user_profile(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, "user_profile.html", {
        'user_obj': user,
    })


from easy_pdf.views import PDFTemplateView

class MyView(PDFTemplateView):
    template_name = "coupon_detail_pdf.html"    
    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        coupon = get_object_or_404(Coupon, slug=slug)
        # add the data in the context 
        context = {'coupon':coupon,}
        return self.render_to_response(context)

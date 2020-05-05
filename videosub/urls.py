from django.urls import path
from videosub import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from videosub.views import (
    homeview,loginregview,startview,membershipview,catagory_list,movies_catagory_movie,movies_detail,movies_show,
    contact,register,logout,handlerequest,profile,editprofile,delete_account,all_movies,webseries_detail,
    webseries_season_episode_detail,watchlist,edit_review,delete_watchlist,edit_webseries_review,
    web_watchlist,delete_web_watchlist,all_webseries,language_media,PasswordChange,renewmembership,
    renewpage,renewhandlerequest,passwordreset_1ststep,passwordreset_2ndstep,passwordreset_3rdstep,
    request_movie,searchview,
)

from . import views

app_name = 'videosub'

urlpatterns = [
    path('',startview.as_view(),name='startpage'),
    path('home',homeview.as_view(),name='home'),
    path('login',loginregview.as_view(),name='loginreg'),
    path('membership',membershipview.as_view(),name='membership'),
    path('renewmembership/<member_id>',renewmembership.as_view(),name='renewmembership'),
    path('renewpage/<memid>/<member_id>',renewpage.as_view(),name='renewpage'),
    path('register/<memid>',register.as_view(),name='register'),
    path('handlerequest/',views.handlerequest,name='handlerequest'),
    path('renewhandlerequest/',views.renewhandlerequest,name='renewhandlerequest'),
    path('logout',logout.as_view(),name='logout'),
    path('profile',profile.as_view(),name='profile'),
    path('editprofile',editprofile.as_view(),name='editprofile'),
    path('delete_account',delete_account.as_view(),name='delete_account'),
    path('catagorylist/<sub_id>',catagory_list.as_view(),name='catagory_list'),
    path('moviescatagorylist/<type_id>',movies_catagory_movie.as_view(),name='movies_catagory_movie'),
    path('movies_detail/<movie_id>',movies_detail.as_view(),name='movies-detail'),
    path('edit_review/<movie_id>',edit_review.as_view(),name='edit_review'),
    path('webseries_detail/<webseries_id>',webseries_detail.as_view(),name='webseries-detail'),
    path('edit_webseries_review/<webseries_id>',edit_webseries_review.as_view(),name='edit_webseries_review'),
    path('webseries_season_episode_detail/<season_episode_id>',webseries_season_episode_detail.as_view(),name='webseries_season_episode_detail'),
    path('movies-show/<movie_show_id>/<movie_lang_id>',movies_show.as_view(),name='movies-show'),
    path('watchlist/<movie_id>',watchlist.as_view(),name='watchlist'),
    path('web_watchlist/<webseries_id>',web_watchlist.as_view(),name='web_watchlist'),
    path('delete_watchlist/<movies_watchlist_id>',delete_watchlist.as_view(),name='delete_watchlist'),
    path('delete_web_watchlist/<webseries_watchlist_id>',delete_web_watchlist.as_view(),name='delete_web_watchlist'),
    path('language_wise/<language_id>',language_media.as_view(),name='language_media'),
    path('all-movies',all_movies.as_view(),name='all_movies'),
    path('all_webseries',all_webseries.as_view(),name='all_webseries'),
    path('contact',contact.as_view(),name='contact'),
    path('request',request_movie.as_view(),name='request_movie'),
    path('search/',searchview.as_view(),name='search'),
    #Password Change
    path('changepassword',PasswordChange.as_view(),name='changepassword'),    
    #Password Reset
    path('password-reset--1st-step/',passwordreset_1ststep.as_view(),name='passwordreset_1ststep'),
    path('password-reset-2nd-step/<member_id>',passwordreset_2ndstep.as_view(),name='passwordreset_2ndstep'),
    path('password-reset-3rd-step/<member_id>',passwordreset_3rdstep.as_view(),name='passwordreset_3rdstep'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

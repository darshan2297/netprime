from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy

from NP_admin.views import (loginreg,index,admin_profile,admin_logout,add_catagory,add_sub_catagory,
                            add_type_catagory,upload_movie_form,upload_movie_csv,media_records,
                            )

app_name = 'NP_admin'


urlpatterns = [
    path('',loginreg.as_view(),name="loginreg"),
    path('index',index.as_view(),name="index"),
    path('admin_profile',admin_profile.as_view(),name="admin_profile"),
    path('admin_logout',admin_logout.as_view(),name="admin_logout"),
    path('addcatagory',add_catagory.as_view(),name="add_catagory"),
    path('addsubcatagory',add_sub_catagory.as_view(),name="add_sub_catagory"),
    path('addtypecatagory',add_type_catagory.as_view(),name="add_type_catagory"),
    path('uploadmediaform',upload_movie_form.as_view(),name="upload_movie_form"),
    path('uploadmediacsv',upload_movie_csv.as_view(),name="upload_movie_csv"),
    path('mediarecords',media_records.as_view(),name="media_records"),
    
    
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
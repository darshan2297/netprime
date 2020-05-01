from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from NP_admin.models import register_admin,main_catagory,sub_catagory,type_catagory,movie_content,movies_csv_content
from django.contrib import messages 
from django.contrib.sessions.models import Session
from hashutils import make_pw_hash, check_pw_hash
from django.contrib import messages
import datetime
import csv,io

# Create your views here.
class loginreg(View):
    def get(self,request,*args, **kwargs):
        if request.session.has_key('username'):
            return redirect('NP_admin:index')
        return render(request,'NP_admin/loginreg.html')
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            if request.FILES:
                unm = request.POST['username']
                pwd = request.POST['password']
                emil = request.POST['email']
                profile =  request.FILES['adminpic']
                
                enc_password = make_pw_hash(pwd)
                
                data = register_admin.objects.create(username=unm,password=enc_password,email=emil,profile_pic=profile)
                data.save()
                return redirect('NP_admin:loginreg')
            else:
                unm = request.POST['username']
                pwd = request.POST['password']
                
                all_data = register_admin.objects.all()
                admin = all_data.get(username = unm)

                if admin and check_pw_hash(pwd, admin.password) :
                    request.session['username'] = unm
                    return redirect('NP_admin:index')
                
class index(View):
    def get(self,request,*args, **kwargs):
        
        return render(request,'NP_admin/index.html')
    
class admin_profile(View):
    def get(self,request,*args, **kwargs):
        all_data = register_admin.objects.all()
        get_data = all_data.filter(username = request.session['username'])
        
        return render(request,'NP_admin/admin_profile.html',{'get_data':get_data})
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            up_data = register_admin.objects.get(username = request.session['username'] )
            
            unm = request.POST['username']
            emil = request.POST['email']
            fnm = request.POST['fname']
            lnm = request.POST['lname']
            mob = request.POST['mobileno']
            
            up_data.username = unm
            up_data.email = emil
            up_data.first_name = fnm
            up_data.last_name = lnm
            up_data.mobile_no = mob
            up_data.save()
            
            request.session['username'] = unm
            
            return redirect('NP_admin:admin_profile')

            
class add_catagory(View):
    def get(self,request,*args, **kwargs):
        main_cat = main_catagory.objects.all()
        sub_cat = sub_catagory.objects.all()
        type_cat = type_catagory.objects.all()
        return render(request,'NP_admin/add_catagory.html',{'main_cat':main_cat,'sub_cat':sub_cat,'type_cat':type_cat})

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            main_cat = request.POST['main_catagory']
            main_thumb = request.FILES['main_thumb']
            add_main_cat = main_catagory.objects.create(main_catagory = main_cat,main_cat_image=main_thumb)
            add_main_cat.save()
            messages.info(request,'Add Main Catagory Successfully')
            return redirect('NP_admin:add_catagory')
        
class add_sub_catagory(View):
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            sub_main_cat = request.POST['select']
            sub_cat = request.POST['sub_catagory']
            sub_thumb = request.FILES['sub_thumb']
            get_main_cat = main_catagory.objects.get(main_catagory = sub_main_cat)
            
            add_sub_cat = sub_catagory.objects.create(main_catagory = get_main_cat,sub_catagory = sub_cat,sub_cat_image=sub_thumb)
            add_sub_cat.save()
            messages.info(request,'Add Sub Catagory Successfully')
            return redirect('NP_admin:add_catagory')
            
class add_type_catagory(View):
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            type_main_cat = request.POST['select_main_cat']
            type_sub_cat = request.POST['select_sub_cat']
            type_cat = request.POST['type_catagory']
            type_thumb = request.FILES['type_thumb']
            
            get_main_cat = main_catagory.objects.get(main_catagory = type_main_cat)
            get_sub_cat = sub_catagory.objects.filter(sub_catagory = type_sub_cat)[0]
            
            add_type_cat = type_catagory.objects.create(main_catagory = get_main_cat,sub_catagory = get_sub_cat,type_catagory = type_cat,type_cat_image=type_thumb)
            add_type_cat.save()
            messages.info(request,'Add Type Catagory Successfully')
            return redirect('NP_admin:add_catagory')
        
               
        
            
class admin_logout(View):
    def get(self,request,*args, **kwargs):
        try:
            del request.session['username']
        except:
            pass
        return redirect('NP_admin:loginreg')
    

class upload_movie_form(View):
    def get(self,request,*args, **kwargs):
        main_cat = main_catagory.objects.all()
        sub_cat = sub_catagory.objects.all()
        type_cat = type_catagory.objects.all()
        return render(request,'NP_admin/upload_media_form.html',{'main_cat':main_cat,'sub_cat':sub_cat,'type_cat':type_cat})

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            mname = request.POST['media_name']
            dhour = request.POST['duration_hours']
            dmin = request.POST['duration_minutes']
            rdate = request.POST['rel_date']
            lng = request.POST['language']
            desc = request.POST['description']
            main_cat = request.POST['select_main_cat']
            sub_cat = request.POST['select_sub_cat']
            type_cat1 = request.POST['select_type_cat1']
            tthumb = request.FILES['t_thumbnail']
            m_potser = request.FILES['movie_poster']
            trailer_576p = request.FILES['movie_trailer_576p']
            trailer_720p = request.FILES['movie_trailer_720p']
            trailer_1080p = request.FILES['movie_trailer_1080p']
            mthumb = request.FILES['m_thumbnail']
            media_576p = request.FILES['media_576p']
            media_720p= request.FILES['media_720p']
            media_1080p = request.FILES['media_1080p']
            mbg = request.FILES['m_bg']
            

            get_main_cat = main_catagory.objects.get(main_catagory = main_cat)
            get_sub_cat = sub_catagory.objects.filter(sub_catagory = sub_cat)[0]
            get_type_cat1 = type_catagory.objects.filter(type_catagory = type_cat1)[0]
           
                

            movie_content_data = movie_content.objects.create(movie_name = mname,duration_hours=dhour,duration_minutes=dmin,
                                                        release_date=rdate,language=lng,description=desc,main_catagory=get_main_cat,
                                                        sub_catagory=get_sub_cat,type_catagory1=get_type_cat1,movie_poster=m_potser,movie_trailer_thumbnail=tthumb,
                                                        movie_trailer_576p=trailer_576p,movie_trailer_720p=trailer_720p,movie_trailer_1080p=trailer_1080p,movie_thumbnail=mthumb,
                                                        movie_576p=media_576p,movie_720p=media_720p,movie_1080p=media_1080p,
                                                        movie_bgimage=mbg
                                                        )
            movie_content_data.save()
            messages.info(request,'Upload Media Successfully')
            return redirect('NP_admin:upload_movie_form')
        
class upload_movie_csv(View):
    def get(self,request,*args, **kwargs):
        # main_cat = main_catagory.objects.all()
        # sub_cat = sub_catagory.objects.all()
        # type_cat = type_catagory.objects.all()
        prompt = {'download':'Please Download Movie Content CSV File Formate And Example '}
        return render(request,'NP_admin/upload_media_csv.html',prompt)
    
    def post(self,request,*args, **kwargs):
        if request.method =='POST':
            movie_csv_f = request.FILES['movie_csv']
            
            if not movie_csv_f.name.endswith('.csv'):
                messages.error(request,'Please select .csv file')
                
            # movie_csv_file_data = movies_csv_content.objects.create(movie_csv_file = movie_csv_f)
            # movie_csv_file_data.save()

            data_set = movie_csv_f.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    get_main_cat = main_catagory.objects.get(main_catagory = column[6])
                    get_sub_cat = sub_catagory.objects.get(sub_catagory = column[7])
                    get_type_cat1 = type_catagory.objects.filter(type_catagory = column[8])[0]
                    get_type_cat2 = type_catagory.objects.filter(type_catagory = column[9])[0]
                    get_type_cat3 = type_catagory.objects.filter(type_catagory = column[10])[0]
                    get_type_cat4 = type_catagory.objects.filter(type_catagory = column[11])[0]
                    get_type_cat5 = type_catagory.objects.filter(type_catagory = column[12])[0]
            
                    

                    movie_content_data = movie_content.objects.create(movie_name = column[0],duration_hours=column[1],duration_minutes=column[2],
                                                            release_date=column[3],language=column[4],description=column[5],main_catagory=get_main_cat,
                                                            sub_catagory=get_sub_cat,type_catagory1=get_type_cat1,type_catagory2=get_type_cat2,
                                                            type_catagory3=get_type_cat3,type_catagory4=get_type_cat4,type_catagory5=get_type_cat5,
                                                            movie_trailer_thumbnail=column[13],movie_trailer=column[14],movie_thumbnail=column[15],
                                                            movie_576p=column[16],movie_720p=column[17],movie_1080p=column[18],
                                                            movie_bgimage=column[19]
                                                            )
                    movie_content_data.save()
            messages.info(request,'Upload Movie Media CSV Successfully')
            return redirect('NP_admin:upload_movie_csv')


        
class media_records(View):
    def get(self,request,*args, **kwargs):
        media_data = movie_content.objects.all()
        return render(request,'NP_admin/media_records.html',{'media_data':media_data})



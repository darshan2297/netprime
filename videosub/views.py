from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from videosub.models import member_record,membership,subscription
from NP_admin.models import (
                register_admin,main_catagory,sub_catagory,type_catagory,
                movie_content,movies_csv_content,webseries_content,webseries_season,
                webseries_season_episode,cast,crew,movies_watchlist,movie_review,
                webseries_review,webseries_watchlist,Transaction,renewmember,multiple_audio_movies,
                language
)
from django.db.models import Avg
from django.contrib import messages
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from Paytm import checksum
from datetime import timedelta,datetime
from videosub.tasks import check_membership
from hashutils import make_pw_hash, check_pw_hash
from django.db.models import OuterRef,Subquery
from datetime import date
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


MERCHANT_KEY = settings.MERCHANT_KEY


class startview(TemplateView):
    def get(self,request,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        check_membership()
        return render(request,'startpage.html')

class membershipview(View):
    def get(self,request,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        membership1 = membership.objects.all()
        return render(request,'membership.html',{'membership1':membership1})
    
    def post(self,request,*args, **kwargs):
       pass
   
class renewmembership(View):
    def get(self,request,member_id,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        membership1 = membership.objects.all()
        return render(request,'membership.html',{'membership1':membership1,'member_id':member_id})

    def post(self,request,*args, **kwargs):
       pass

class renewpage(View):
    def get(self,request,memid,member_id,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        memid1 = membership.objects.get(id=memid)
        get_member = member_record.objects.get(mid = member_id)
        return render(request,'renewpage.html',{'memid1':memid1,'get_member':get_member})
    
    def post(self,request,memid,member_id,*args, **kwargs):
        memid1 = membership.objects.get(id=memid)
        get_member = member_record.objects.get(mid = member_id)
        
        get_member.membership = memid1
        get_member.amount = memid1.price
        get_member.save()
        
        transaction = Transaction.objects.create(made_by=get_member, amount=memid1.price)
        transaction.save()
        

        param_dict = {
            'MID': settings.MERCHANT_ID,
            'ORDER_ID': str(transaction.order_id),
            'TXN_AMOUNT': str(transaction.amount),
            'CUST_ID': str(transaction.made_by.email),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://netprime.pythonanywhere.com/renewhandlerequest/',
        }
        paytm_params = dict(param_dict)
        Checksum = checksum.generate_checksum(paytm_params, MERCHANT_KEY)
        
        transaction.checksum = Checksum
        transaction.save()
        
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request,'paytm.html', {'param_dict':param_dict,})
    
@csrf_exempt
def renewhandlerequest(request):
    if request.session.has_key('member_id'):
        return redirect('videosub:home')
     # paytm will send you post request here
    form = request.POST
    
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            Checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
    # member_record
    if verify:
        if response_dict['RESPCODE'] == '01':
            oid = request.POST['ORDERID']
            price = request.POST['TXNAMOUNT'][0:3]
            # member_record
            all_transaction = Transaction.objects.all()
            get_data = all_transaction.get(order_id=oid)
            get_mem = get_data.made_by.mid
            
            get_data.payment_status = True
            get_data.save()
            
            get_all_data = member_record.objects.all()
            get_mem_rec =  get_all_data.get(mid=get_mem)

            
            get_mem_rec.join_date = datetime.today()
            get_mem_rec.last_date = datetime.today() + timedelta(days=30)
            get_mem_rec.save()
            
            
            get_mem_rec.remaining_days = abs((get_mem_rec.join_date - get_mem_rec.last_date)).days
            get_mem_rec.save()
            
            # subscription_data
            if subscription.objects.filter(user_member=get_mem_rec).exists():
                get_sub = subscription.objects.get(user_member=get_mem_rec)
                get_sub.active=True
                get_sub.save()
            else:
                subscription_data = subscription(user_member=get_mem_rec,active=True)
                subscription_data.save()
            
            # renewsubscription
            renew = renewmember.objects.create(user = get_mem_rec,amount = price)
            renew.save()
        else:   
            oid = response_dict['ORDERID']
            # member_record 
            all_transaction = Transaction.objects.all()
            get_data = all_transaction.get(order_id=oid)
            get_mem = get_data.made_by.mid
            
            get_data.payment_status = False
            get_data.save()
            
            
            get_all_data = member_record.objects.all()
            get_mem_rec =  get_all_data.get(mid=get_mem)
            
            get_mem_rec.remaining_days = 0
            get_mem_rec.save()
            
            
    return render(request, 'paymentstatus.html', {'response': response_dict,'get_mem_rec':get_mem_rec})

class loginregview(View):
    def get(self,request,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        check_membership()
        return render(request,'loginregister.html')
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            if member_record.objects.filter(uname= request.POST['uname']).exists():
                unm = request.POST['uname']
                passwd = request.POST['pwd']
                
                data = member_record.objects.all()
                user =data.get(uname = unm)
                a = user.mid
                remain_days = int(user.remaining_days)
                log = member_record.objects.filter(uname=unm,password=passwd).count()
                
                all_subscription = subscription.objects.all()
                if all_subscription.get(user_member = user.mid):
                    get_sub = all_subscription.get(user_member = user.mid)
                
                    if remain_days == 0:
                        get_sub.active = False
                        get_sub.save()
                        
                    get_sub1 = all_subscription.get(user_member = user.mid)
                    
                    if remain_days != 0 and get_sub1.active:
                        if user and check_pw_hash(passwd, user.password):
                            request.session['member_id'] = unm
                            return redirect('videosub:home')
                        else:
                            messages.info(request,'Please enter correct password')
                            return redirect('videosub:loginreg')
                    else:
                        
                        messages.info(request,'Please renew the membership')
                        return redirect('/renewmembership/%s' % user.mid)
                else:
                    messages.info(request,'Please renew the membership')
                    return redirect('/renewmembership/%s' % user.mid)
            else:
                messages.info(request,'Please enter correct username')
                return redirect('videosub:loginreg')
                
class logout(View):
    def get(self,request,*args, **kwargs):
        try:
            del request.session['member_id']
        except:
            pass
        return redirect('videosub:startpage')
        
        
class register(View):
    def get(self,request,memid,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        memid1 = membership.objects.get(id=memid)
        return render(request,'register.html',{'memid1':memid1})
    
    def post(self,request,memid,*args, **kwargs):
        memid1 = membership.objects.get(id=memid)
        if request.method == 'POST':
            unm = request.POST['uname']
            emil = request.POST['email']
            pwd = request.POST['password']
            rpwd = request.POST['repeatpassword']
            amount = request.POST['price']
            profile_image = request.FILES['pimage']
            fmovie = (request.POST['fmovie']).lower()
            fwebseries = request.POST['fwebseries'].lower()
            if pwd == rpwd:
                if member_record.objects.filter(uname=unm).exists():
                    messages.info(request,'Username Already Taken')
                    return redirect('/register/%s' % memid)
                
                elif member_record.objects.filter(email=emil).exists():
                    messages.info(request,'Email Already Taken')
                    return redirect('/register/%s' % memid )

                else:
                    enc_password = make_pw_hash(pwd)
                    enc_rpassword = make_pw_hash(rpwd)
                    
                    reg_data = member_record.objects.create(uname=unm,email=emil,password=enc_password,repeat_password=enc_rpassword,
                                                            membership=memid1,amount=memid1.price,
                                                            profile_pic=profile_image,favourite_movie=fmovie,
                                                            favourite_webseries=fwebseries)
                    reg_data.save()
                    
                    all = member_record.objects.all()
                    get_member = all.get(uname = unm)
                    # print(get_member.mid)
                    
                    transaction = Transaction.objects.create(made_by=get_member, amount=memid1.price)
                    transaction.save()
                    

                    param_dict = {
                        'MID': settings.MERCHANT_ID,
                        'ORDER_ID': str(transaction.order_id),
                        'TXN_AMOUNT': str(transaction.amount),
                        'CUST_ID': str(transaction.made_by.email),
                        'INDUSTRY_TYPE_ID': 'Retail',
                        'WEBSITE': 'WEBSTAGING',
                        'CHANNEL_ID': 'WEB',
                        'CALLBACK_URL':'http://netprime.pythonanywhere.com/handlerequest/',
                    }
                    paytm_params = dict(param_dict)
                    Checksum = checksum.generate_checksum(paytm_params, MERCHANT_KEY)
                    
                    transaction.checksum = Checksum
                    transaction.save()
                    
                    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
                    
                    
                    return render(request,'paytm.html', {'param_dict':param_dict,})
            else:
                messages.info(request,'Both Password Not Matching')
                return redirect('videosub:membership')
            
@csrf_exempt
def handlerequest(request):
    if request.session.has_key('member_id'):
        return redirect('videosub:home')
     # paytm will send you post request here
    form = request.POST
    
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            Checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
    # member_record
    if verify:
        if response_dict['RESPCODE'] == '01':
            oid = request.POST['ORDERID']
            # member_record
            all_transaction = Transaction.objects.all()
            get_data = all_transaction.get(order_id=oid)
            get_mem = get_data.made_by.mid
            
            get_data.payment_status = True
            get_data.save()
            
            get_all_data = member_record.objects.all()
            get_mem_rec =  get_all_data.get(mid=get_mem)
            

            get_mem_rec.remaining_days = abs((get_mem_rec.join_date - get_mem_rec.last_date)).days
            get_mem_rec.save()
            
            # subscription_data
            subscription_data = subscription(user_member=get_mem_rec,active=True)
            subscription_data.save()
        else:   
            oid = response_dict['ORDERID']
            # member_record 
            all_transaction = Transaction.objects.all()
            get_data = all_transaction.get(order_id=oid)
            get_mem = get_data.made_by.mid
            
            get_data.payment_status = False
            get_data.save()
            
            
            get_all_data = member_record.objects.all()
            get_mem_rec =  get_all_data.get(mid=get_mem)

            get_mem_rec.remaining_days = 0
            get_mem_rec.save()
            
    return render(request, 'paymentstatus.html', {'response': response_dict,'get_mem_rec':get_mem_rec})
            
            
class passwordreset_1ststep(View):
    def get(self,request,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        return render(request, 'password-reset/password_reset.html')
    
    def post(self,request,*args, **kwargs):
        if request.method=='POST':
            if member_record.objects.filter(uname= request.POST['uname']).exists() and member_record.objects.filter(email= request.POST['email']).exists():
                unm = request.POST['uname']
                emil = request.POST['email']
                
                member = member_record.objects.get(uname = unm)
                
                if member.uname == unm and member.email == emil:
                   return redirect('/password-reset-2nd-step/%s' % member.mid)
            else:
                messages.info(request,'Please enter correct username and email')
                return redirect('videosub:passwordreset_1ststep')

class passwordreset_2ndstep(View):
    def get(self,request,member_id,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        
        return render(request, 'password-reset/password_reset_2ndstep.html')

    def post(self,request,member_id,*args, **kwargs):
        if request.method=='POST':
            if member_record.objects.filter(mid=member_id).exists():
                fmovie = request.POST['fmovie']
                fwebseries = request.POST['fwebseries']
                
                member = member_record.objects.get(mid = member_id)
                
                if member.favourite_movie == fmovie and member.favourite_webseries == fwebseries:
                  return redirect('/password-reset-3rd-step/%s' % member.mid)
                else:
                    messages.info(request,'Please enter correct answer')
                    return redirect('/password-reset-2nd-step/%s' % member.mid)
            else:
                return redirect('videosub:passwordreset_1ststep')

class passwordreset_3rdstep(View):
    def get(self,request,member_id,*args, **kwargs):
        if request.session.has_key('member_id'):
            return redirect('videosub:home')
        
        return render(request, 'password-reset/password_reset_3rdstep.html')

    def post(self,request,member_id,*args, **kwargs):
        if request.method=='POST':
            if member_record.objects.filter(mid=member_id).exists():
                newpwd = request.POST['newpwd']
                confpwd = request.POST['confpwd']
                
                member = member_record.objects.get(mid = member_id)
                
                enc_newpassword = make_pw_hash(newpwd)
                enc_confpassword = make_pw_hash(confpwd)
                
                if enc_newpassword == enc_confpassword:
                    member.password = enc_newpassword
                    member.repeat_password = enc_confpassword
                    member.save()
                    messages.info(request,'Password reset successfully')
                return redirect('videosub:loginreg')
            else:
                return redirect('videosub:passwordreset_1ststep')

class homeview(TemplateView):
    def get(self,request,*args, **kwargs):
        if request.session.has_key('member_id'):
            check_membership()
            data = member_record.objects.all()
            user_data = data.get(uname = request.session['member_id'])
            all_subscription = subscription.objects.all()
            get_sub = all_subscription.get(user_member = user_data.mid)
            
            if user_data.remaining_days == 0:
                get_sub.active = False
                get_sub.save()
            
            get_sub1 = all_subscription.get(user_member = user_data.mid)
            
            if user_data.remaining_days !=0 and get_sub1.active:
                m_cate = main_catagory.objects.all()
                s_cate = sub_catagory.objects.all()
                sdate  = date.today()
                edate = date.today() + timedelta(days=30)
                latest_movie_list = movie_content.objects.all().order_by('-release_date')
                latest_webseries_list = webseries_content.objects.all().order_by('-release_date')
                page = request.GET.get('page', 1)
                
                paginator = Paginator(latest_movie_list,16)
                try:
                    latest_movie_order = paginator.page(page)
                except PageNotAnInteger:
                    latest_movie_order = paginator.page(1)
                except EmptyPage:
                    latest_movie_order = paginator.page(paginator.num_pages)
                
                paginator1 = Paginator(latest_webseries_list,16)
                try:
                    latest_webseries_order = paginator1.page(page)
                except PageNotAnInteger:
                    latest_webseries_order = paginator1.page(1)
                except EmptyPage:
                    latest_webseries_order = paginator1.page(paginator1.num_pages)
                
                get_movie_review = movie_review.objects.filter(member = user_data)
                get_webseries_review = webseries_review.objects.filter(member = user_data)
                return render(request,'index.html',{'m_cate':m_cate,'s_cate':s_cate,
                                                    'latest_movie_order':latest_movie_order,
                                                    'latest_webseries_order':latest_webseries_order,
                                                    'get_movie_review':get_movie_review,
                                                    'get_webseries_review':get_webseries_review
                                                    })
            else:
                try:
                    del request.session['member_id']
                except:
                    pass
                messages.info(request,'Please renew the membership')
                return redirect('/renewmembership/%s' % user_data.mid)
        return redirect('videosub:loginreg')
 
class profile(View):
    def get(self,request,*args, **kwargs):
        data = member_record.objects.all()
        user_data = data.get(uname = request.session['member_id'])
        get_movie_review = movie_review.objects.filter(member = user_data)
        get_webseries_review = webseries_review.objects.filter(member = user_data)
        get_movie_review_count = movie_review.objects.filter(member = user_data).count()
        get_webseries_review_count = webseries_review.objects.filter(member = user_data).count()
        count_review = get_movie_review_count + get_webseries_review_count
        get_movie_watchlist = movies_watchlist.objects.filter(member = user_data)
        get_webseries_watchlist = webseries_watchlist.objects.filter(member = user_data)
        get_webseries_watchlist_count = webseries_watchlist.objects.filter(member = user_data).count()
        get_movie_watchlist_count = movies_watchlist.objects.filter(member = user_data).count()
        count_watchlist = get_webseries_watchlist_count + get_movie_watchlist_count
        
        return render(request,'profile.html',{'user_data':user_data,'get_movie_review':get_movie_review,
                                              'get_movie_review_count':get_movie_review_count,
                                              'get_movie_watchlist':get_movie_watchlist,
                                              'get_webseries_watchlist':get_webseries_watchlist,
                                              'get_movie_watchlist_count':get_movie_watchlist_count,
                                              'count_watchlist':count_watchlist,'count_review':count_review,
                                              'get_webseries_review':get_webseries_review
                                              })

           
class editprofile(View):
    def get(self,request,*args, **kwargs):
        all_member = member_record.objects.all()
        log_member = all_member.get(uname = request.session['member_id'])
        return render(request,'editprofile.html',{'log_member':log_member})
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST' and request.FILES['imageUpload']:
            all_member = member_record.objects.all()
            up_data = all_member.get(uname = request.session['member_id'])
            
            unm = request.POST['uname']
            emil = request.POST['email']
            fnm = request.POST['fname']
            lnm = request.POST['lname']
            mob = request.POST['mobileno']
            profile_image = request.FILES['imageUpload']
            cntry = request.POST['country']
            fb = request.POST['facebook']
            tw = request.POST['twitter']
            lk = request.POST['linkedin']
            insta = request.POST['instagram']
            
            
            up_data.uname = unm
            up_data.email = emil
            up_data.first_name = fnm
            up_data.last_name = lnm
            up_data.mobile_no = mob
            up_data.profile_pic = profile_image
            up_data.country=cntry
            up_data.facebook=fb
            up_data.twitter=tw
            up_data.linkedin=lk
            up_data.instagram=insta
            
            up_data.save()
            username = up_data.uname
            
            request.session['member_id'] = username
            
            return redirect('videosub:editprofile')

class delete_account(View):
    def post(self,request,*args, **kwargs):
        data = member_record.objects.all()
        user_data = data.filter(uname = request.session['member_id'])
        if request.method == 'POST':
            user_data.delete()
            del request.session['member_id']
            return redirect('videosub:startpage')

class catagory_list(View):
    def get(self,request,sub_id,*args,**kwargs):
        get_sub_cat = sub_catagory.objects.filter(sub_id = sub_id)
        get_main_cat = get_sub_cat.values_list('main_catagory',flat=True).first()
        get_type_data = type_catagory.objects.filter(sub_catagory = sub_id)
        get_movie = movie_content.objects.filter(sub_catagory=sub_id).order_by('-release_date')
        page = request.GET.get('page', 1)
                
        paginator = Paginator(get_movie,12)
        try:
            get_movie_list = paginator.page(page)
        except PageNotAnInteger:
            get_movie_list = paginator.page(1)
        except EmptyPage:
            get_movie_list = paginator.page(paginator.num_pages)
        
        get_webseries = webseries_content.objects.filter(sub_catagory=sub_id).order_by('-release_date')
        
        paginator1 = Paginator(get_webseries,12)
        try:
            get_webseries_list = paginator1.page(page)
        except PageNotAnInteger:
            get_webseries_list = paginator1.page(1)
        except EmptyPage:
            get_webseries_list = paginator1.page(paginator1.num_pages)
            
        return render(request,'catagory_list.html',{'get_type_data':get_type_data,'get_sub_cat':get_sub_cat,'get_movie_list':get_movie_list,'get_webseries_list':get_webseries_list,'get_main_cat':get_main_cat})
    
    def post(self,request,*args, **kwargs):
        pass
    
class movies_catagory_movie(View):
    def get(self,request,type_id,*args,**kwargs):
        all_type = type_catagory.objects.filter(type_id = type_id)
        get_main_cat = all_type.values_list('main_catagory',flat=True).first()
        get_movie = movie_content.objects.filter(type_catagory1 = type_id).order_by('-release_date')
        page = request.GET.get('page', 1)
                
        paginator = Paginator(get_movie,16)
        try:
            get_movie_list = paginator.page(page)
        except PageNotAnInteger:
            get_movie_list = paginator.page(1)
        except EmptyPage:
            get_movie_list = paginator.page(paginator.num_pages)
        
        
        get_webseries = webseries_content.objects.filter(type_catagory=type_id).order_by('-release_date')
        
        paginator1 = Paginator(get_webseries,16)
        try:
            get_webseries_list = paginator1.page(page)
        except PageNotAnInteger:
            get_webseries_list = paginator1.page(1)
        except EmptyPage:
            get_webseries_list = paginator1.page(paginator1.num_pages)
        return render(request,'movie_list.html',{'get_movie_list':get_movie_list,'get_webseries_list':get_webseries_list,'get_main_cat':get_main_cat,'all_type':all_type})
    
    def post(self,request,*args, **kwargs):
        pass
    
class movies_detail(View):
    def get(self,request,movie_id,*args, **kwargs):
        data = member_record.objects.all()
        user = data.get(uname = request.session['member_id'])
        get_movie_detail = movie_content.objects.get(movie_id = movie_id)
        get_review1 = movie_review.objects.filter(movie=get_movie_detail).order_by('-created_date')
        get_review = movie_review.objects.filter(movie=get_movie_detail).order_by('-created_date')
        page = request.GET.get('page', 1)
        
        paginator = Paginator(get_review,20)
        try:
            get_review_detail = paginator.page(page)
        except PageNotAnInteger:
            get_review_detail = paginator.page(1)
        except EmptyPage:
            get_review_detail = paginator.page(paginator.num_pages)
        
        all_review = movie_review.objects.filter(movie = movie_id).aggregate(Avg('rating'))
        get_member = movie_review.objects.filter(member = user) & movie_review.objects.filter(movie = get_movie_detail)
        get_member_watchlist = movies_watchlist.objects.filter(member = user) & movies_watchlist.objects.filter(movie = get_movie_detail)
        get_multiple_movie = multiple_audio_movies.objects.filter(movie=movie_id)
        return render(request,'movie-detail.html',{'get_movie_detail':get_movie_detail,
                                                   'get_review_detail':get_review_detail,
                                                   'all_review':all_review,'get_member':get_member,
                                                   'get_member_watchlist':get_member_watchlist,
                                                   'get_multiple_movie':get_multiple_movie,
                                                   'get_review1':get_review1
                                                   })
    
    def post(self,request,movie_id,*args, **kwargs):
        get_movie_detail = movie_content.objects.get(movie_id = movie_id)
        # get_watchlist = movies_watchlist.o
        data = member_record.objects.all()
        user = data.get(uname = request.session['member_id'])
        
        if request.method == 'POST':
            comment = request.POST['review']
            star = request.POST['rating']
            
            data = movie_review.objects.create(member=user,movie=get_movie_detail,comment=comment,rating=star)
            data.save()
            
            all_review = movie_review.objects.filter(movie = movie_id).aggregate(Avg('rating'))
 
            for key,value in all_review.items():
                get_movie_detail.rating = value
                get_movie_detail.save()
            
            return redirect('/movies_detail/%s' % movie_id)
        
class edit_review(View):
    def post(self,request,movie_id,*args, **kwargs):
        if request.method == 'POST':
            up_review = movie_review.objects.get(movie_review_id = request.POST['review_id'])
            get_movie_detail = movie_content.objects.get(movie_id = movie_id)
            get_movie_watchlist_detail = movies_watchlist.objects.get(movie = movie_id)
            # print(get_movie_watchlist_detail)
            data = member_record.objects.all()
            user = data.get(uname = request.session['member_id'])
            
            comment = request.POST['review']
            rating = request.POST['rating']
            
            up_review.member = user
            up_review.movie = get_movie_detail
            up_review.comment = comment
            up_review.rating = rating
            
            up_review.save()
            
            all_review = movie_review.objects.filter(movie = movie_id).aggregate(Avg('rating'))
 
            for key,value in all_review.items():
                get_movie_detail.rating = value
                get_movie_detail.save()
            
            
            messages.info(request,'Update Review Successfully')
            return redirect('/movies_detail/%s' % movie_id)

        
class webseries_detail(View):
    def get(self,request,webseries_id,*args, **kwargs):
        data = member_record.objects.all()
        user = data.get(uname = request.session['member_id'])
        get_webseries_detail = webseries_content.objects.filter(webseries_id = webseries_id)
        get_webseries = webseries_content.objects.get(webseries_id = webseries_id)
        get_webseries_season = webseries_season.objects.filter(webseries_id = webseries_id)
        get_webseries_season_episode = webseries_season_episode.objects.filter(webseries_id = webseries_id).order_by('webseries_season_id')
        get = get_webseries_season_episode.values('webseries_season_id')
        avg_review = webseries_review.objects.filter(webseries = webseries_id).aggregate(Avg('rating'))
        get_member_review = webseries_review.objects.filter(member = user) & webseries_review.objects.filter(webseries = get_webseries)
        get_member_watchlist = webseries_watchlist.objects.filter(member = user) & webseries_watchlist.objects.filter(webseries = get_webseries)
        get_review1 = webseries_review.objects.filter(webseries=get_webseries).order_by('-created_date')
        get_review = webseries_review.objects.filter(webseries=get_webseries).order_by('-created_date')
        
        page = request.GET.get('page', 1)
        
        paginator = Paginator(get_review,20)
        try:
            get_review_detail = paginator.page(page)
        except PageNotAnInteger:
            get_review_detail = paginator.page(1)
        except EmptyPage:
            get_review_detail = paginator.page(paginator.num_pages)
        
        return render(request,'webseries_detail.html',{'get_webseries_detail':get_webseries_detail,'get_webseries_season':get_webseries_season,
                                                       'get_webseries_season_episode':get_webseries_season_episode,
                                                       'get_member_review':get_member_review,'avg_review':avg_review,
                                                       'get_member_watchlist':get_member_watchlist,
                                                       'get_review_detail':get_review_detail,'get_review1':get_review1
                                                       })
    
    def post(self,request,webseries_id,*args, **kwargs):
        get_webseries_detail = webseries_content.objects.get(webseries_id = webseries_id)
  
        data = member_record.objects.all()
        user = data.get(uname = request.session['member_id'])
        
        if request.method == 'POST':
            comment = request.POST['review']
            star = request.POST['rating']
            
            data = webseries_review.objects.create(member=user,webseries=get_webseries_detail,comment=comment,rating=star)
            data.save()
            
            avg_review = webseries_review.objects.filter(webseries = webseries_id).aggregate(Avg('rating'))
 
            for key,value in avg_review.items():
                get_webseries_detail.rating = value
                get_webseries_detail.save()
            
            return redirect('/webseries_detail/%s' % webseries_id)
        
        
class edit_webseries_review(View):
    def post(self,request,webseries_id,*args, **kwargs):
        if request.method == 'POST':
            up_review = webseries_review.objects.get(webseries_review_id = request.POST['review_id'])
            get_webseries_detail = webseries_content.objects.get(webseries_id = webseries_id)
            data = member_record.objects.all()
            user = data.get(uname = request.session['member_id'])
            
            comment = request.POST['review']
            rating = request.POST['rating']
            
            up_review.member = user
            up_review.webseries = get_webseries_detail
            up_review.comment = comment
            up_review.rating = rating
            
            up_review.save()
            
            avg_review = webseries_review.objects.filter(webseries = webseries_id).aggregate(Avg('rating'))
            
 
            for key,value in avg_review.items():
                get_webseries_detail.rating = value
                get_webseries_detail.save()
            
            
            messages.info(request,'Update Review Successfully')
            return redirect('/webseries_detail/%s' % webseries_id)

class webseries_season_episode_detail(View):
    def get(self,request,season_episode_id,*args, **kwargs):
        get_webseries_season_episode = webseries_season_episode.objects.filter(webseries_season_episode_id = season_episode_id)
        return render(request,'webseries_season_episode_detail.html',{'get_webseries_season_episode':get_webseries_season_episode})
    
    def post(self,request,*args, **kwargs):
        pass

class movies_show(View):
    def get(self,request,movie_show_id,movie_lang_id,*args, **kwargs):
        get_movie_show = multiple_audio_movies.objects.filter(movie = movie_show_id)& multiple_audio_movies.objects.filter(language = movie_lang_id)
        return render(request,'movie-show.html',{'get_movie_show':get_movie_show})
    
    def post(self,request,*args, **kwargs):
        pass
    
class language_media(View):
    def get(self,request,language_id,*args, **kwargs):
        get_lang= language.objects.get(language_id=language_id)
        get_movie = multiple_audio_movies.objects.filter(language=language_id).order_by('movie__release_date').reverse()
        page = request.GET.get('page', 1)
        
        paginator = Paginator(get_movie,16)
        try:
            get_movie_lang = paginator.page(page)
        except PageNotAnInteger:
            get_movie_lang = paginator.page(1)
        except EmptyPage:
            get_movie_lang = paginator.page(paginator.num_pages)
            
        get_webseries = webseries_season_episode.objects.filter(language=language_id).order_by('webseries_season_id__release_date').reverse()
        page = request.GET.get('page', 1)
        
        paginator = Paginator(get_webseries,16)
        try:
            get_webseries_lang = paginator.page(page)
        except PageNotAnInteger:
            get_webseries_lang = paginator.page(1)
        except EmptyPage:
            get_webseries_lang = paginator.page(paginator.num_pages)    
        return render(request,'language_wise.html',{'get_lang':get_lang,'get_movie_lang':get_movie_lang,
                                                    'get_webseries_lang':get_webseries_lang})
 
class all_movies(View):
    def get(self,request,*args, **kwargs):
        all_movies = movie_content.objects.all().order_by('-release_date')
        page = request.GET.get('page', 1)
        
        paginator = Paginator(all_movies,16)
        try:
            get_all_movies = paginator.page(page)
        except PageNotAnInteger:
            get_all_movies = paginator.page(1)
        except EmptyPage:
            get_all_movies = paginator.page(paginator.num_pages)
        return render(request,'all_movies.html',{'get_all_movies':get_all_movies})
        
    
class all_webseries(View):
    def get(self,request,*args, **kwargs):
        all_webseries = webseries_content.objects.all().order_by('-release_date')
        page = request.GET.get('page', 1)
        
        paginator = Paginator(all_webseries,16)
        try:
            get_all_webseries = paginator.page(page)
        except PageNotAnInteger:
            get_all_webseries = paginator.page(1)
        except EmptyPage:
            get_all_webseries = paginator.page(paginator.num_pages)
        
        return render(request,'all_webseries.html',{'get_all_webseries':get_all_webseries})
    
    
class watchlist(View):
    def post(self,request,movie_id,*args, **kwargs):
        get_movie_detail = movie_content.objects.get(movie_id = movie_id)
        data = member_record.objects.all()
        user = data.get(uname = request.session['member_id'])
        get_member_watchlist = movies_watchlist.objects.filter(member = user) & movies_watchlist.objects.filter(movie = get_movie_detail)


        if request.method == 'POST':
            if get_member_watchlist:
                messages.info(request,'This Movie Already Exist In WatchList')
                return redirect('/movies_detail/%s' % movie_id )
            else:
                watchlist = movies_watchlist.objects.create(member=user,movie=get_movie_detail)
                watchlist.save()
                return redirect('/movies_detail/%s' % movie_id)
            
            
class web_watchlist(View):
    def post(self,request,webseries_id,*args, **kwargs):
        get_webseries_detail = webseries_content.objects.get(webseries_id = webseries_id)
        data = member_record.objects.all()
        user = data.get(uname = request.session['member_id'])
        get_member_watchlist = webseries_watchlist.objects.filter(member = user) & webseries_watchlist.objects.filter(webseries = get_webseries_detail)

        if request.method == 'POST':
            if get_member_watchlist:
                messages.info(request,'This Movie Already Exist In WatchList')
                return redirect('/webseries_detail/%s' % webseries_id)
            else:
                watchlist = webseries_watchlist.objects.create(member=user,webseries=get_webseries_detail)
                watchlist.save()
                return redirect('/webseries_detail/%s' % webseries_id)
                
                
class delete_watchlist(View):
    def post(self,request,movies_watchlist_id,*args, **kwargs):
        get_review_id = movies_watchlist.objects.get(movies_watchlist_id= movies_watchlist_id)
        if request.method == 'POST':
            get_review_id.delete()
            return redirect('videosub:profile')
        
class delete_web_watchlist(View):
    def post(self,request,webseries_watchlist_id,*args, **kwargs):
        get_review_id = webseries_watchlist.objects.get(webseries_watchlist_id= webseries_watchlist_id)
        if request.method == 'POST':
            get_review_id.delete()
            return redirect('videosub:profile')
    

class contact(View):
    def get(self,request,*args, **kwargs):
        return render(request,'contact.html')
    
    def post(self,request,*args, **kwargs):
        i  = False
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            sub = request.POST['subject']
            msg = request.POST['message']
            
            msg_html = render_to_string('email.html', {'name': name,'name': name,'email': email,'sub': sub,'msg': msg})

            send_mail(sub,msg,
                settings.EMAIL_HOST_USER,
                ['darshanvwla22@gmail.com'],
                html_message=msg_html,
            )
            
            i = True
            
            return render(request,'contact.html',{'i':i}) 
        
class request_movie(View):
    def get(self,request,*args, **kwargs):
        return render(request,'request_movie.html')
    
    def post(self,request,*args, **kwargs):
        i  = False
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            sub = request.POST['mrequest']
            msg = request.POST['message']
            
            msg_html = render_to_string('email_mrequest.html', {'name': name,'name': name,'email': email,'sub': sub,'msg': msg})

            send_mail(sub,msg,
                settings.EMAIL_HOST_USER,
                ['darshanvwla22@gmail.com'],
                html_message=msg_html,
            )
            
            i = True
            
            return render(request,'request_movie.html',{'i':i}) 

class PasswordChange(View):
    def get(self,request,*args, **kwargs):
        return render(request,'change-password.html')
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            data = member_record.objects.all()
            user = data.get(uname = request.session['member_id'])
            oldpwd = request.POST['oldpwd']
            newpwd = request.POST['newpwd']
            confpwd = request.POST['confpwd']
            
            enc_password = make_pw_hash(oldpwd)
            enc_newpassword = make_pw_hash(newpwd)
            enc_confpassword = make_pw_hash(confpwd)
            
            if user.password == enc_password:
                user.password = enc_newpassword
                user.repeat_password = enc_confpassword
                user.save()
                try:
                    del request.session['member_id']
                except:
                    pass
                return redirect('videosub:loginreg')
            else:
                messages.info(request,'Old Password is Incorrect')
                return render(request,'change-password.html')

class searchview(View):
    def get(self,request,*args, **kwargs):   
        if request.method == 'GET': # this will be GET now      
            search_text =  request.GET.get('search') 
            if movie_content.objects.filter(movie_name__icontains=search_text):
                get_result_movie = movie_content.objects.filter(movie_name__icontains=search_text)
                print(get_result_movie)
                return render(request,"search_template.html",{'get_result_movie':get_result_movie})
            else:
                if webseries_content.objects.filter(webseries_name__icontains=search_text):
                    get_result_webseries = webseries_content.objects.filter(webseries_name__icontains=search_text)
                    print(get_result_webseries)
                    return render(request,"search_template.html",{'get_result_webseries':get_result_webseries})
                else:
                    i=True
                    return render(request,"search_template.html",{'i':i})
        else:
            return render(request,"search_template.html",{})
                    
                
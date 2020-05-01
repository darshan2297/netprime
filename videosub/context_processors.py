from videosub.models import subscription,member_record,membership
from NP_admin.models import register_admin,main_catagory,sub_catagory,type_catagory,movie_content,movies_csv_content,language


def all_sub_catagory(request):
    return {
        'movie_sub_category': sub_catagory.objects.all()
    }
     
def all_language(request):
    return {
        'language_all': language.objects.all()
    }
     
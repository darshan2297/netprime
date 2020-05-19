from django.db import models
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from videosub.models import *

# Create your models here.
class register_admin(models.Model):
    aid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    password = models.CharField(max_length=256)
    mobile_no = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='AdminProfile')
    join_date = models.DateTimeField(auto_now_add=True)
    
    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
    
class main_catagory(models.Model):
    main_id = models.AutoField(primary_key=True)
    main_catagory = models.CharField(max_length = 150,null=True,blank=True)
    main_cat_image = models.ImageField(upload_to='main_cat_image',null = True,blank=True)
    
    def __str__(self):
        return self.main_catagory
    
class sub_catagory(models.Model):
    sub_id = models.AutoField(primary_key=True)
    main_catagory = models.ForeignKey(main_catagory,on_delete = models.CASCADE,null=True,blank=True)
    sub_catagory = models.CharField(max_length = 150,null=True,blank=True)
    sub_cat_image = models.ImageField(upload_to='sub_cat_image',null = True,blank=True)
    
    def __str__(self):
        return self.sub_catagory
    
    
class type_catagory(models.Model):
    type_id = models.AutoField(primary_key=True)
    main_catagory = models.ForeignKey(main_catagory,on_delete = models.CASCADE,null=True,blank=True)
    sub_catagory = models.ForeignKey(sub_catagory,on_delete = models.CASCADE,null=True,blank=True)
    type_catagory = models.CharField(max_length = 150,null=True,blank=True)
    type_cat_image = models.ImageField(upload_to='type_cat_image',null = True,blank=True)
    
    def __str__(self):
        return self.type_catagory

    
class cast(models.Model):
    cast_id = models.AutoField(primary_key=True)
    cast_name = models.CharField(max_length = 50)
    cast_profile = models.ImageField(upload_to='cast_profile',null = True,blank=True)
    more_info = models.URLField(max_length = 200)
    
    def __str__(self):
        return self.cast_name
    
class crew(models.Model):
    crew_id = models.AutoField(primary_key=True)
    crew_name = models.CharField(max_length = 50)
    crew_profile = models.ImageField(upload_to='crew_profile',null = True,blank=True)
    more_info = models.URLField(max_length = 200)
          
    def __str__(self):
        return self.crew_name    
    
class movie_content(models.Model):
    movie_id  = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length= 100)
    duration_hours = models.IntegerField()
    duration_minutes = models.IntegerField()
    release_date = models.DateField()
    language = models.CharField(max_length=50)
    description = models.TextField(max_length = 1500)
    main_catagory = models.ForeignKey(main_catagory,on_delete = models.CASCADE,null = True)
    sub_catagory = models.ForeignKey(sub_catagory,on_delete = models.CASCADE,null = True)
    type_catagory1 = models.ForeignKey(type_catagory,on_delete = models.CASCADE,null = True,blank = True,related_name="type_cat1")
    cast = models.ManyToManyField(cast,blank = True)
    crew = models.ManyToManyField(crew,blank = True)
    rating = models.FloatField(default=0)
    movie_trailer_thumbnail = models.ImageField(max_length=200,upload_to='movie_trailers_thumbnail',null = True,blank=True)
    movie_trailer_720p = models.FileField(max_length=200,upload_to ='movie_trailers_720p',null = True,blank=True)
    movie_poster = models.ImageField(upload_to='movie_poster',editable=True,blank=True,null = True)                    
    movie_bgimage = models.ImageField(upload_to='movie_background',null = True,blank=True)
    more_info = models.URLField(max_length = 200)
    created_date = models.DateField(default=datetime.today())
    
    def __str__(self):
        return self.movie_name
    
class language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.language
    
class multiple_audio_movies(models.Model):
    multiple_audio_movies_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(movie_content,on_delete = models.CASCADE,null = True)
    language = models.ForeignKey(language,on_delete = models.CASCADE,null = True)
    title = models.CharField(max_length= 150)
    movie_thumbnail = models.ImageField(upload_to='movie_thumbnail',null = True,blank=True)
    movie_720p = models.FileField(upload_to ='movie_720p',null = True,blank=True)
    
    def __str__(self):
        return '{} {}'.format(self.movie.movie_name, self.language.language)
    

class webseries_content(models.Model):
    webseries_id  = models.AutoField(primary_key=True)
    webseries_name = models.CharField(max_length= 100)
    release_date = models.DateField()
    language = models.CharField(max_length=50)
    description = models.TextField(max_length = 1500)
    main_catagory = models.ForeignKey(main_catagory,on_delete = models.CASCADE,null = True)
    sub_catagory = models.ForeignKey(sub_catagory,on_delete = models.CASCADE,null = True)
    type_catagory = models.ForeignKey(type_catagory,on_delete = models.CASCADE,null = True,blank = True)
    cast = models.ManyToManyField(cast,null = True,blank = True)
    crew = models.ManyToManyField(crew,null = True,blank = True)
    rating = models.FloatField(default=0)
    webseries_poster = models.ImageField(upload_to='webseries_poster',editable=True,blank=True,null = True)                        
    webseries_bgimage = models.ImageField(upload_to='webseries_background',null = True,blank=True)
    more_info = models.URLField(max_length = 200)
    created_date = models.DateField(default=datetime.today())
    
    def __str__(self):
        return self.webseries_name

class webseries_season(models.Model):
    webseries_season_id = models.AutoField(primary_key=True)
    webseries_id = models.ForeignKey(webseries_content,on_delete = models.CASCADE,null = True)
    duration_hours = models.IntegerField()
    duration_minutes = models.IntegerField()
    release_date = models.DateField()
    season = models.CharField(max_length = 20)
    webseries_trailer_thumbnail = models.ImageField(upload_to='webseries_trailers_thumbnail',null = True,blank=True)
    webseries_trailer_720p = models.FileField(upload_to ='webseries_trailers_720p',null = True,blank=True)
    created_date = models.DateField(default=datetime.today())

    def __str__(self):
        return '{} {}'.format(self.webseries_id.webseries_name, self.season)
    
class webseries_season_episode(models.Model):
    webseries_season_episode_id = models.AutoField(primary_key=True)
    webseries_id = models.ForeignKey(webseries_content,on_delete = models.CASCADE,null = True)
    webseries_season_id = models.ForeignKey(webseries_season,on_delete = models.CASCADE,null = True)
    episode_name = models.CharField(max_length= 100)
    duration_hours = models.IntegerField()
    duration_minutes = models.IntegerField()
    release_date = models.DateField()
    language = models.ForeignKey(language,on_delete = models.CASCADE,null = True)
    episode = models.CharField(max_length = 20)
    webseries_thumbnail = models.ImageField(upload_to='webseries_thumbnail',null = True,blank=True)
    webseries_720p = models.FileField(upload_to ='webseries_720p',null = True,blank=True)
    created_date = models.DateField(default=datetime.today())
    
    def __str__(self):
        return '{} {} {} {}'.format(self.webseries_id.webseries_name, self.webseries_season_id.season,
                                 self.episode_name,self.language.language)

   
class movie_download_link(models.Model):
    movie_download_link_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length= 100)
    release_date = models.DateField(null = True,blank=True)
    description = models.TextField(max_length = 1500)
    movie_poster =  models.ImageField(upload_to='movie_poster',null = True,blank=True)

    def __str__(self):
        return self.movie_name

class movie_link_detail(models.Model):
    movie_download_link_id = models.ForeignKey(movie_download_link,on_delete = models.CASCADE,null = True)
    title = models.CharField(max_length= 100,null = True,blank=True)
    link = models.URLField(null = True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.movie_download_link_id.movie_name, self.title)
    
class webseries_download_link(models.Model):
    webseries_download_link_id = models.AutoField(primary_key=True)
    webseries_name = models.CharField(max_length= 100)
    season_release_date = models.DateField(null = True,blank=True)
    season = models.CharField(max_length= 100,null = True,blank=True)
    description = models.TextField(max_length = 1500)
    webseries_poster =  models.ImageField(upload_to='webseries_poster',null = True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.webseries_name,self.season)

class webseries_link_details(models.Model):
    webseries_download_link_id = models.ForeignKey(webseries_download_link,on_delete = models.CASCADE,null = True)
    episode = models.CharField(max_length= 100)
    link = models.URLField(null = True,blank=True)
    
    def __str__(self):
        return '{} {} {}'.format(self.webseries_download_link_id.webseries_name,self.webseries_download_link_id.season,self.episode)
    
class movie_review(models.Model):
    movie_review_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(member_record,on_delete = models.CASCADE,null = True,)
    movie = models.ForeignKey(movie_content,on_delete = models.CASCADE,null = True,blank=True)
    comment = models.TextField(max_length= 1000)
    rating = models.FloatField(default=0)
    created_date = models.DateField(default=datetime.today())
    
    def __str__(self):
        return self.member.uname
    
    
class movies_watchlist(models.Model):
    movies_watchlist_id =  models.AutoField(primary_key=True)
    member = models.ForeignKey(member_record,on_delete = models.CASCADE,null = True)
    movie = models.ForeignKey(movie_content,on_delete = models.CASCADE,null = True,blank=True)
    
    
class webseries_review(models.Model):
    webseries_review_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(member_record,on_delete = models.CASCADE,null = True,)
    webseries = models.ForeignKey(webseries_content,on_delete = models.CASCADE,null = True,blank=True)
    comment = models.TextField(max_length= 1000)
    rating = models.FloatField(default=0)
    created_date = models.DateField(default=datetime.today())
    
    def __str__(self):
        return self.member.uname
    
    
class webseries_watchlist(models.Model):
    webseries_watchlist_id =  models.AutoField(primary_key=True)
    member = models.ForeignKey(member_record,on_delete = models.CASCADE,null = True)
    webseries = models.ForeignKey(webseries_content,on_delete = models.CASCADE,null = True,blank=True)
              
class movies_csv_content(models.Model):
    movie_csv_file = models.FileField(upload_to='movie_csv_file')
    
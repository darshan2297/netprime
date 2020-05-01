from django.db import models
from datetime import timedelta,datetime
# Create your models here.


MEMBERSHIP_CHOICES = (
    ('Premirer', 'pre'),
    ('Popular', 'pop'),
    ('Basic', 'basic')
)    

class membership(models.Model):
    id = models.AutoField(primary_key=True)
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Free',
        max_length=30)
    feature1 = models.CharField(max_length=200)
    feature2 = models.CharField(max_length=200)
    feature3 = models.CharField(max_length=200)
    price = models.IntegerField(default=15)
    
    def __str__(self):
        return self.membership_type
    
class member_record(models.Model):
    mid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    membership = models.ForeignKey(membership, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(null=True)
    profile_pic = models.ImageField(upload_to='Profileimage', null=True,blank=True)
    facebook = models.URLField(max_length = 200)
    twitter = models.URLField(max_length = 200)
    linkedin = models.URLField(max_length = 200)
    instagram = models.URLField(max_length = 200)
    member_date = models.DateTimeField(default=datetime.today())
    join_date = models.DateTimeField(default=datetime.today())
    last_date = models.DateTimeField(default=datetime.today() + timedelta(days=30),null=True)
    remaining_days = models.IntegerField(null=True)
    favourite_movie = models.CharField(max_length=100,null=True)
    favourite_webseries = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.uname
    
class renewmember(models.Model):
    user = models.ForeignKey(member_record, 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    
    def __str__(self):
        return self.user.uname

class Transaction(models.Model):
    made_by = models.ForeignKey(member_record, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.made_by.uname

    def save(self, *args, **kwargs):    
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


    
class subscription(models.Model):
    sid = models.AutoField(primary_key=True)
    user_member = models.ForeignKey(member_record,on_delete=models.CASCADE,null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user_member.uname

    

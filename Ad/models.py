from django.db import models
from polymorphic.models import PolymorphicModel
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
#from varieties.models import SubCategory

 

class Ad (PolymorphicModel) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=105)
    ad_description = models.TextField(max_length=1000)
    price = models.FloatField()
    category = models.ForeignKey('varieties.SubCategory', on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    # country = models.ForeignKey()
    # city = models.ForeignKey()
    # curreny = models.ForeignKey()
    # payment_method = models.ForeignKey()

    def __str__(self) : 
        return f"{self.ad_title}"
    

class AdImage (models.Model) : 
    image = models.ImageField(upload_to='Ads-images/')
    Ad = models.ForeignKey(Ad,on_delete=models.CASCADE)
    




class Notification (models.Model) : 
    to_user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self) :
        return f'{self.content}'
    




from .bridge import Bridge
@receiver(post_save,sender=Ad)
def Send_Message_To_Ad_Owner_Followers (created, instance, **kwrags) : 
    if created :
        user_id = instance.user.id
        try :
            Bridge(user_id=user_id)
        except Exception as error : 
            print(f"An error accoured : {error}")

            

from django.db import models
from users.models import User
from Ad.models import Ad


 


class ReportAd(models.Model):
    content = models.TextField()
    ad = models.ForeignKey('Ad.Ad', on_delete=models.CASCADE, related_name='report_ads')
    reported_at = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_ads')
    discard = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.ad)

  
class ReportProblem(models.Model):
    content = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_problems')
    discard = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.content)


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_ads')
    ad = models.ForeignKey('Ad.Ad', on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.ad)

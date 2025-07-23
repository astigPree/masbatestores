from django.db import models
from datetime import datetime
# Create your models here.

class MerchantData(models.Model):
    base_pk = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=320)
    latitude = models.FloatField(null=True, blank=True)   
    longitude = models.FloatField( null=True, blank=True)
    hours = models.JSONField(default=dict)
    profile = models.ImageField(null=True, blank=True , upload_to='merchant/')
    background = models.ImageField(null=True, blank=True , upload_to='merchant_background/')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def coordinates(self):
        return (self.latitude, self.longitude)
    
    def is_open_now(self):
        now = datetime.now()
        day = now.strftime('%A').lower()
        today = self.hours.get(day)

        if not today:  # Closed
            return False

        if today.get("always"):
            return True

        time_range = today.get("time")
        if not time_range or len(time_range) != 2:
            return False

        fmt = "%I:%M:%S %p"  # Matches "09:00:00 am"
        try:
            open_time = datetime.strptime(time_range[0], fmt).time()
            close_time = datetime.strptime(time_range[1], fmt).time()
        except ValueError:
            return False  # Invalid time format

        return open_time <= now.time() <= close_time
    

    #TODO: Store hours in this format later
    #{
    #    "monday":    { "always": false, "time": ["09:00:00 am", "05:00:00 pm"] },
    #    "tuesday":   { "always": true,  "time": [] },
    #    "wednesday": { "always": false, "time": ["10:00:00 am", "04:00:00 pm"] },
    #    "thursday":  null,
    #    "friday":    { "always": false, "time": ["09:00:00 am", "05:00:00 pm"] },
    #    "saturday":  null,
    #    "sunday":    null
    #}


class Paninda(models.Model):
    merchant_pk = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    availability = models.CharField(
        max_length=100,
        choices=[
            ("Laging Available", "Laging Available"),
            ("Available sa Umaga", "Available sa Umaga"),
            ("Available sa Hapon", "Available sa Hapon"),
            ("Available sa Gabi", "Available sa Gabi"),
            ("Hindi Available", "Hindi Available")
        ]
    )
    uri = models.CharField(
        max_length=100,
        choices=[
            ("Produkto", "Produkto"),
            ("Serbisyo", "Serbisyo")
        ]
    )
    image = models.ImageField(null=True, blank=True , upload_to='paninda/')
    created_at = models.DateTimeField(auto_now_add=True)




class MerchantReviews(models.Model):
    user_pk = models.BigIntegerField(null=True, blank=True)
    merchant_pk = models.BigIntegerField(null=True, blank=True)
    review = models.CharField(max_length=1000)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_item = models.CharField(max_length=100)
    
class MerchantReviewReplies(models.Model):
    user_pk = models.BigIntegerField(null=True, blank=True)
    merchant_pk = models.BigIntegerField(null=True, blank=True)
    review_pk = models.BigIntegerField(null=True, blank=True)
    reply = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)    



# TODO: FUCOS ON WORKING ON IN USER SCREEN TO CREATE USER MODEL


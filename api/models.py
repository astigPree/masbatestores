from django.db import models
from datetime import datetime
# Create your models here.

class MerchantData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=320)
    latitude = models.FloatField()   
    longitude = models.FloatField()
    hours = models.JSONField()


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



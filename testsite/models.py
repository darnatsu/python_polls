from django.db import models

# Create your models here.

class Page(models.Model):
    heading_text = models.CharField(max_length=265)
    subheading_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.heading_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
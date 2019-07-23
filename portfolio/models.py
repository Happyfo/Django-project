from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio')
    description = models.TextField()

    # summary of the description in the model( 100 characters)
    def minimized(self):
        return self.description[:100]

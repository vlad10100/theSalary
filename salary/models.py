from django.db import models



class Industry(models.Model):
    industry                    = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name            = 'Industy'
        verbose_name_plural     = 'Industries'

    def __repr__(self):
        return self.industry
    
    def __str__(self):
        return self.__repr__()


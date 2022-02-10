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


class JobBoard(models.Model):
    job_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    pay = models.PositiveIntegerField()
    
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    class Meta:
        verbose_name            = 'Job Board'
        verbose_name_plural     = 'Job Board'

    def __repr__(self):
        return self.job_name
    
    def __str__(self):
        return self.__repr__()



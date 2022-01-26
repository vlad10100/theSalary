from django.db import models

from account.models import CustomUser



class Industry(models.Model):
    industry                    = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name            = 'Industy'
        verbose_name_plural     = 'Industries'

    def __repr__(self):
        return self.industry
    
    def __str__(self):
        return self.__repr__()

class Job(models.Model):
    job                         = models.CharField(max_length=30, unique=True)

    industry                    = models.ForeignKey('Industry', on_delete=models.CASCADE)

    class Meta:
        verbose_name            = 'Job'
        verbose_name_plural     = 'Jobs'

    

    def __repr__(self):
        return self.job
    
    def __str__(self):
        return self.__repr__()

class SalaryBlog(models.Model):
    position                    = models.CharField(max_length=50, null=False, blank=False)
    role                        = models.CharField(max_length=50, null=False, blank=False)
    yoe                         = models.PositiveSmallIntegerField(null=False, blank=False)
    tool_1                      = models.CharField(max_length=20, null=False, blank=False)
    tool_2                      = models.CharField(max_length=20, null=True, blank=True)
    tool_3                      = models.CharField(max_length=20, null=True, blank=True)
    salary                      = models.PositiveIntegerField(null=False, blank=False)
    location                    = models.CharField(max_length=50, null=False, blank=False)

    user                        = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    job                         = models.ForeignKey('Job', on_delete=models.CASCADE)

    # created                     = models.DateTimeField(auto_now_add=True)
    # updated                     = models.DateTimeField(auto_now=True)


    class Meta:
        
        verbose_name            = 'Salary Info'
        verbose_name_plural     = 'Salary Info'



    def __repr__(self):
        output = f"{self.user.username} || {self.position} || {self.role} || {self.salary} || {self.location}"
        return output
    
    def __str__(self):
        return self.__repr__()

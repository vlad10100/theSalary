from django.db import models

from account.models import CustomUser
from salary.models import Industry

class IndustryBlog(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        output = f"{self.title} -by {self.created_by}"
        return output

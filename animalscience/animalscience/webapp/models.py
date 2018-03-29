from django.db import models

class ProjectsData(models.Model):
    project_title = models.CharField(max_length=30, default='none')
    project_author_name = models.CharField(max_length=30, default='none')
    project_year = models.DateField(null=True)
    project_keywords = models.CharField(max_length=30, default='none')
    def __str__(self):              # __unicode__ on Python 2
        return self.project_title
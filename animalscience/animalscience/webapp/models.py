from django.db import models

class ProjectsData(models.Model):
    project_title = models.CharField(max_length=30, default='none')
    project_author_name = models.CharField(max_length=30, default='none')
    project_year = models.DateField(null=True)
    project_keywords = models.CharField(max_length=30, default='none')
    def __str__(self):              # __unicode__ on Python 2
        return self.project_title

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)
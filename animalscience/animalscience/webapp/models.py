from django.db import models
import uuid
    
class author_entity(models.Model):
    """
    Model representing an author.
    """
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100, default='none')
    last_name = models.CharField(max_length=100, default='none')

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.author_id)])
    
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)

class key_entity(models.Model):
    key_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    keyword = models.CharField(max_length=100, default="")
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.keyword
        
    
class article_entity(models.Model):
    # article_id = models.AutoField(primary_key=True)
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    article_title = models.CharField(max_length=200, default=None)
    # filename = models.CharField(max_length=200, default=None)
    link = models.CharField(max_length=200, default=None)
    article_year = models.CharField(max_length=4, default=None)

    authors = models.ManyToManyField(author_entity, default=None)
    keywords = models.ManyToManyField(key_entity, default=None)
    
    # class Meta:
    #     ordering = [""]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('article_entity', args=[str(self.id)])
    
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.article_title
    def display_authors(self):
        # Create a string of authors to display on admin
        return ', '.join([ authors.last_name for authors in self.authors.all()[:3] ])
        display_authors.short_description = 'Authors'

    def display_keywords(self):
        # Create astring of  keywords to dislay on admin
        return ', '.join([ keywords.keyword for keywords in self.keywords.all()[:3] ])
        display_keywords.short_description = 'Keywords'
    
# class article_author_rel (models.Model):
#     article_id_fk = models.ForeignKey(article_entity, on_delete=models.CASCADE, null=True)
#     author_id_fk = models.ForeignKey(author_entity, on_delete=models.CASCADE, null=True)
    
# class article_key_rel(models.Model):
#     article_id_fk = models.ForeignKey(article_entity, on_delete=models.CASCADE, null=True)
#     key_id_fk = models.ForeignKey(key_entity, on_delete=models.CASCADE, null=True)
    
    
    
class researchdata(models.Model):
    article_id = models.IntegerField()
    article_title = models.CharField(max_length=30, default='none')
    article_author_name = models.CharField(max_length=30, default='none')
    article_year = models.DateField(null=True)
    article_keywords = models.CharField(max_length=30, default='none')
    def __str__(self):
        return self.article_title


class ProjectsData(models.Model):
    project_title = models.CharField(max_length=30, default='none')
    project_author_name = models.CharField(max_length=30, default='none')
    project_year = models.DateField(null=True)
    project_keywords = models.CharField(max_length=30, default='none')
    def __str__(self):              # __unicode__ on Python 2
        return self.project_title

class Post(models.Model):
    project_title = models.CharField(max_length=30, default='none')
    author = models.CharField(max_length=30, default='none')
    description = models.CharField(max_length=30, default='none')

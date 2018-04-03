from django.contrib import admin
from .models import ProjectsData, article_entity, key_entity, author_entity

# Register your models here.
admin.site.register(ProjectsData)
admin.site.register(article_entity)
admin.site.register(key_entity)
admin.site.register(author_entity)
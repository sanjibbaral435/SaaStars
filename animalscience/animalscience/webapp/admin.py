from django.contrib import admin
from .models import ProjectsData, article_entity, key_entity, author_entity

# Register your models here.
admin.site.register(ProjectsData)

admin.site.register(key_entity)

admin.site.register(author_entity)
class author_entityAdmin(admin.ModelAdmin):
	list_display=('last_name','first_name')

#admin.site.register(article_entity)
@admin.register(article_entity)
class article_entityAdmin(admin.ModelAdmin):
	list_display=('article_title','article_year','display_authors','display_keywords')
from django.contrib import admin
from .models import study

class studyadmin(admin.ModelAdmin):
    list_display =["study_title", "study_reshte" , "study_master"]
    list_display_links = ["study_title", "study_reshte" , "study_master"]
    list_filter = ["study_master" ,"study_unit"]
    search_fields = ["study_title", "study_reshte" , "study_unit" ,"study_code","study_group","study_master"]

    class Meta:
        model = study

admin.site.register(study ,studyadmin)

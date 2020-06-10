from django.contrib import admin
from .models import student


class studentadmin(admin.ModelAdmin):
    list_display =["student_name", "student_family" , "student_id" ,"meli_code"]
    list_display_links =["student_name", "student_family" , "student_id" ,"meli_code"]
    list_filter = ["enter_year" ,"reshte", "uni_name","maghta_tahsil"]
    search_fields = ["student_name", "student_family" , "student_id" ,"meli_code","father_name","student_phone","reshte","bank_id","address"]

    class Meta:
        model = student

admin.site.register(student ,studentadmin)
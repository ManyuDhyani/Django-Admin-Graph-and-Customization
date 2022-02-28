from django.contrib import admin
from .models import Student, Country, City
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field


admin.site.register(Country)
admin.site.register(City)

class StudentResource(resources.ModelResource):
    gender = Field()
    class Meta:
        model = Student
        fields = ('id', 'full_name', 'language', 'grades', 'gender')
        export_order = fields



class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    resources_class = StudentResource
    list_display = ('full_name', 'language', 'grades', 'gender')
    list_filter = ('language', 'gender', 'grades')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

admin.site.register(Student, StudentAdmin)
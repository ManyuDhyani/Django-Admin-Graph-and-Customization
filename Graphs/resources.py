from import_export import resources
from .models import Person
from import_export.fields import Field

class PersonResource(resources.ModelResource):
    birth_date = Field()
    class Meta:
        model = Person

    def dehydrate_birth_date(self, obj):
        return obj.birth_date.strftime('%d-%m-%Y')
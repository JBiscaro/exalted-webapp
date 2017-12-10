from django.contrib import admin

from calculator.models import Charm


# Register your models here.
class CharmAdmin(admin.ModelAdmin):
    model = Charm
    list_display = ('name', 'order')
    prepopulated_fields = {
        'slug': ('name',),
    }


admin.site.register(Charm, CharmAdmin)

# name: joe
# pass: PredCyrus101@

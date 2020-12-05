from django.contrib import admin

from .models import Country, Atraction


class AtractionInline(admin.StackedInline):
    model = Atraction
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['tags']}),
        (None, {'fields': ['open_for_f']}),
        (None, {'fields': ['open_for_t']}),
        (None,  {'fields': ['quarantine']})
        

    ]
    inlines = [AtractionInline]

admin.site.register(Country, CountryAdmin)
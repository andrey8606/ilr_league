from django.contrib import admin

from .models import Result


class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'overall_place',
        'place_in_group',
        'name',
        'distance',
        'result',
        'city',
        'gender',
        'rank',
        'year'
    )
    search_fields = ("name",)
    list_filter = ("year", "gender")
    empty_value_display = "-пусто-"


admin.site.register(Result, ResultAdmin)

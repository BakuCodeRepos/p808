from django.contrib import admin

from .models import About, AboutPoint


class InlineAboutPointAdmin(admin.TabularInline):
    model = AboutPoint
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (InlineAboutPointAdmin,)


# admin.site.register(AboutPoint)

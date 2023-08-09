from django.contrib import admin

from .models import Scenario, Prompt, PromptGroup, ScenarioPrompt

class ScenarioPromptInline(admin.TabularInline):
    model = ScenarioPrompt
    extra = 1 # how many rows to show

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = (ScenarioPromptInline,)

class PromptAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags')


class PromptGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag','is_active')

# Register your models here.

admin.site.register(Scenario, ScenarioAdmin)

admin.site.register(Prompt, PromptAdmin)

admin.site.register(PromptGroup, PromptGroupAdmin)
from DjangonLearning.polls.models import Poll, Choice

from django.contrib import admin

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['question']}),
        ('Info de Data', {'fields' : ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInLine]
    filter = ['pub_date']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)

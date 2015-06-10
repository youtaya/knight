from django.contrib import admin
from people.models import People


class PeopleAdmin(admin.ModelAdmin):
	fieldsets = [
		('user', {'fields':['user']}),
		('nickname', {'fields': ['nickname']}),
		('avatar', {'fields': ['avatar']}),
	]

admin.site.register(People, PeopleAdmin)

from django.contrib import admin
from models import BBS,Category,BBS_user
# Register your models here.

class BBS_admin(admin.ModelAdmin):
	list_display=('title','category','summary','author','signature','view_count','create_at')
	list_filter=('create_at',)
	search_fields=('title','author__user__username')
	def signature(self,obj):
		return obj.author.signature
	signature.short_description='signature'



admin.site.register(BBS,BBS_admin)
admin.site.register(Category)
admin.site.register(BBS_user)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account

class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'phone_number','identity_id','last_login', 'is_admin','is_staff')
	search_fields = ('email','username','identity_id')
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)

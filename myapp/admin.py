from django.contrib import admin
from .models import sinhvien,school,khoa,comment
class schooladmin(admin.ModelAdmin):
    list_display=('mat','tent')
    search_fields=['mat','tent']
    list_filter=('mat','tent')
class khoaadmin(admin.ModelAdmin):
    list_display=('mak','tenk')
    search_fields=['mak','tenk']
    list_filter=('mak','tenk')
class sinhvienadmin(admin.ModelAdmin):
    list_display=('masv','tensv','school','khoa','lop','image','gender')
    search_fields=['masv','tensv','school','khoa','lop','image','gender']
    list_filter=('masv','tensv','school','khoa','lop','image','gender')
class commentAdmin(admin.ModelAdmin):
    list_display=('user','text','create_time')
    search_fields=['user','text','create_time']
    list_filter=('user','text','create_time')
admin.site.register(school,schooladmin)
admin.site.register(khoa,khoaadmin)
admin.site.register(sinhvien,sinhvienadmin)
admin.site.register(comment,commentAdmin)
# Register your models here.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CustomUser, stkStatus
from import_export import resources

class stkResource(resources.ModelResource):
    class Meta:
        model = stkStatus
        exclude = ('id',)
        import_id_fields = ['createtime']


# 将资源注册到导入导出模块中
@admin.register(stkStatus)
class stkAdmin(ImportExportModelAdmin):
    resource_class = stkResource


# admin.site.register(stkStatus, stkAdmin)

# Register your models here.
admin.site.register(CustomUser)


from django.contrib import admin
from . import models

admin.site.register(models.Instructor)
admin.site.register(models.Course)
admin.site.register(models.Blog)
admin.site.register(models.Traffic_Law)
admin.site.register(models.Traffic_Rule)
admin.site.register(models.Warning_Signs)
admin.site.register(models.Priotity_Signs)
admin.site.register(models.Prohibition_Signs)
admin.site.register(models.Mandatory_Signs)
admin.site.register(models.Signs_Of_Special_Regulations)
admin.site.register(models.Information_Signs)
admin.site.register(models.Service_Marks)
admin.site.register(models.Signs_Of_Additional_Information)
admin.site.register(models.Advantages)
admin.site.register(models.Frequently_Asked_Questions)
admin.site.register(models.Aplly_For_Job)
admin.site.register(models.Aplly_For_Course)

class Comments_Admin(admin.ModelAdmin):
    readonly_fields = ['name', 'body', 'rating', 'created_date', 'updated_date']
admin.site.register(models.Comment, Comments_Admin)
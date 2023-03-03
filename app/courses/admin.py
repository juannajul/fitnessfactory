from django.contrib import admin

# Models
from .models.categories import Category
from .models.courses import Course


admin.site.register(Category)

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Course, CourseAdmin)

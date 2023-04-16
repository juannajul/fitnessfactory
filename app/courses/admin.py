from django.contrib import admin
from django.utils import timezone
from django.utils import timezone
timezone.activate("America/Caracas")
# Models
from .models.categories import Category
from .models.courses import Course
from .models.memberships import Membership


admin.site.register(Category)

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Course, CourseAdmin)

admin.site.register(Membership)


# class StudentAdmin(Admin.ModelAdmin):
#         list_display = [..., "created_at_etc", ...]
#         def add_view(self, request, form_url='', extra_context=None):
#             timezone.activate("US/Eastern")
#             return super(ActivityAdmin, self).add_view(
#                 request,
#                 form_url,
#                 extra_context
#             )

#         def change_view(self, request, object_id, form_url='', extra_context=None):
#             timezone.activate("US/Eastern")
#             return super(ActivityAdmin, self).change_view(
#                 request,
#                 object_id,
#                 form_url,
#                 extra_context
#           )

#         def get_time(self, time):
#             import pytz
#             fmt = '%Y-%m-%d %H:%M:%S %Z'
#             tz = pytz.timezone("US/Eastern")
#             dt = time.astimezone(tz)
#             return dt.strftime(fmt)

#         def created_at_etc(self, student):
#             return self.get_time(student.created_at)

#         created_at_etc.short_description = "Created At"
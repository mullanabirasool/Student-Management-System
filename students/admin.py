from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "mobile_no",
        "email_id",
        "course",
        "batch",
        "experience_fresher",
    )

    search_fields = (
        "name",
        "mobile_no",
        "email_id",
        "course",
    )

    list_filter = (
        "course",
        "experience_fresher",
    )

    ordering = (
        "-id",
    )
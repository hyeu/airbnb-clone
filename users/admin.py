from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# from . import models: 같은 파일에 있는 models.py를 불러오는것


class RoomInline(admin.StackedInline):
    model = models.User


# decorator는 class위에 있어야 함. ex. customUserAdmin으로 User control
# admin.site.register(models.User, CustomUserAdmin)과 같음
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

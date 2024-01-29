from django.contrib import admin

from .models import Course, Level, LevelSkill, Links, Modul, Pract, Skill, Theme, UserCourse, UserLevel

admin.site.register(UserLevel)
admin.site.register(LevelSkill)
admin.site.register(Level)
admin.site.register(Skill)
admin.site.register(UserCourse)
admin.site.register(Theme)
admin.site.register(Modul)
admin.site.register(Course)
admin.site.register(Pract)
admin.site.register(Links)

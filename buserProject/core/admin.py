from django.contrib import admin

from core.models import ActivityLog, Todo, Question, Answer, UserExtraInfo


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'text')


class UserExtraInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'avatar_email')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserExtraInfo, UserExtraInfoAdmin)
admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)

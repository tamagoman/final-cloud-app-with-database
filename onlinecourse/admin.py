from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Question)
admin.site.register(Choice)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['question_text']
#     lession = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     # question text
#     question_text = models.CharField(max_length=200)
#     # question grade/mark
#     grade = models.IntegerField(default=0)

# class ChoiseAdmin(admin.ModelAdmin):
#     list_display = ['title']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

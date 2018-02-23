# coding=utf-8
from django.contrib import admin

# Register your models here.

from .models import Question,Choice

# admin.StackedInline以堆叠的形式展示关联的choice
# class ChoiceInline(admin.StackedInline):
# admin.TabularInline以表格的形式展示关联的choice
class ChoiceInline(admin.TabularInline):
	model = Choice
	# 控制额外显示的输入框，默认就是3
	extra = 2

class QuestionAdmin(admin.ModelAdmin):
	# 控制表单输入框的顺序和标题
	# fields = ['pub_date','question_text']
	# 每个元组的第一个参数作为表单控件的标题，第二个参数作为表单的字段参数
	fieldsets = [
		('Question information',{'fields':['question_text']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']})
	]

	# 注册关联对象数据
	inlines = [ChoiceInline]

	# 控制表头的显示文本和列数
	list_display = ('question_text','pub_date','was_published_recently')
	# list_display = ('pub_date','question_text','was_published_recently')
	
	# 控制过滤查询的字段，以菜单列表的形式在右侧进行显示
	list_filter = ['question_text','pub_date']

	# 控制查询输入框支持的字段，在表格顶部显示
	search_fields = ['question_text']

# admin.site.register(Question)
admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)



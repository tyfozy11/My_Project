from django import template
from core.models import Dish


# @register.inclusion_tag('includes/course_card.html')
# def popular_courses(num: int = 5) -> dict:
#     students = Student.objects.all().select_related('group')
#     courses = {}
#     for student in students:
#         if courses.get(student.group.course_id):
#             my_list = courses[student.group.course_id] + 1
#             courses.update({student.group.course_id: my_list})
#         else:
#             courses.update({student.group.course_id: 1})
#     sorted_courses = dict(sorted(courses.items(), key=lambda item: item[1], reverse=True)[:num])
#     return {
#         'course_list': Course.objects.prefetch_related('teacher').filter(id__in=sorted_courses.keys())
#     }

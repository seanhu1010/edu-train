from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet,LessonTimeViewSet, CourseViewSet, FeeViewSet, EnrollmentViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register('lessontime', LessonTimeViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'attendances', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

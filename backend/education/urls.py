from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DictionaryViewSet, DictionaryDataViewSet, AvatarViewSet, ParentViewSet, DropoutViewSet, \
    TeacherViewSet, StudentViewSet, FeeViewSet, PeriodViewSet, LessonViewSet, CourseViewSet, FeeDetailViewSet, \
    PaymentRecordViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'dictionary', DictionaryViewSet)
router.register(r'dictionary-data', DictionaryDataViewSet)
router.register(r'avatar', AvatarViewSet)
router.register(r'parent', ParentViewSet)
router.register(r'dropout', DropoutViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)
router.register(r'fee', FeeViewSet)
router.register(r'period', PeriodViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'course', CourseViewSet)
router.register(r'fee-detail', FeeDetailViewSet)
router.register(r'payment-record', PaymentRecordViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import  path
from django.db import router

"""Routes"""
from rest_framework.routers import DefaultRouter

"""Views"""
from .views import AuthorViewSet, CategoryViewSet, ObraViewSet

router = DefaultRouter()
router.register(r'author',AuthorViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'obras',ObraViewSet)

urlpatterns = router.urls

urlpatterns += [

]
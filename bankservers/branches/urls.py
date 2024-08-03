from django.urls import path
from .views import BankList, BankDetail, BranchDetail

urlpatterns = [
    path('banks/', BankList.as_view(), name='bank-list'),
    path('banks/<int:pk>/', BankDetail.as_view(), name='bank-detail'),
    path('branches/<int:pk>/', BranchDetail.as_view(), name='branch-detail'),
]

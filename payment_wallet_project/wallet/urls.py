from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletViewSet, TransactionViewSet, wallet_view

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallets')
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', wallet_view, name='wallet-page'),
    path('wallets/<int:pk>/deposit/', WalletViewSet.as_view({'post': 'deposit'}), name='wallet-deposit'),
    path('wallets/<int:pk>/withdraw/', WalletViewSet.as_view({'post': 'withdraw'}), name='wallet-withdraw'),

]
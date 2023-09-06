from rest_framework import viewsets, status
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from decimal import Decimal
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from django.shortcuts import render
from django.http import JsonResponse

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=True, methods=['post'])
    def deposit(self, request, pk=None):
        wallet = self.get_object()
        amount = Decimal(request.data['amount'])
        print(f"Amount to deposit: {amount}")  # For debugging
        wallet.balance += amount
        wallet.save()        
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
        

    @action(detail=True, methods=['post'])
    def withdraw(self, request, pk=None):
        wallet = self.get_object()
        amount = Decimal(request.data['amount'])
        if wallet.balance < amount:
            return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
        wallet.balance -= amount
        wallet.save()
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

def wallet_view(request):
    # Retrieve the wallet data you want to display
    wallet = Wallet.objects.first()  # You may need to adjust this query
    return render(request, 'wallt.html', {'wallet': wallet})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# def wallet_page(request):
#     # Retrieve the transaction history data (you can customize this query as needed)
#     transactions = Transaction.objects.all().order_by('-timestamp')

#     # Render the HTML template with the transaction history data
#     return render(request, 'wallet.html', {'transactions': transactions})


# class WalletViewSet(viewsets.ModelViewSet):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer


# class TransactionViewSet(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer

#     def create(self, request, *args, **kwargs):
#         # Determine if it's a deposit or withdrawal
#         is_deposit = request.data.get('is_deposit', False)
#         wallet_id = request.data.get('wallet')

#         # Validate that wallet_id is provided and is a valid integer
#         if not wallet_id:
#             return Response({"detail": "Wallet ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             wallet_id = int(wallet_id)
#         except ValueError:
#             return Response({"detail": "Invalid Wallet ID format."}, status=status.HTTP_400_BAD_REQUEST)

#         # Retrieve the wallet
#         try:
#             wallet = Wallet.objects.get(pk=wallet_id)
#         except Wallet.DoesNotExist:
#             return Response({"detail": "Wallet does not exist."}, status=status.HTTP_404_NOT_FOUND)

#         amount = request.data.get('amount', 0)

#         if is_deposit:
#             wallet.balance += amount
#         else:
#             if wallet.balance < amount:
#                 return Response({"detail": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)
#             wallet.balance -= amount

#         # Save the wallet and create a transaction record
#         wallet.save()
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class Deposit(generics.CreateAPIView):
#     serializer_class = TransactionSerializer

#     def perform_create(self, serializer):
#         user = self.request.user
#         amount = serializer.validated_data['amount']
        
#         # Update user balance
#         user.balance += amount
#         user.save()

#         # Create transaction record
#         Transaction.objects.create(user=user, amount=amount, is_deposit=True)

# class Withdraw(generics.CreateAPIView):
#     serializer_class = TransactionSerializer

#     def perform_create(self, serializer):
#         user = self.request.user
#         amount = serializer.validated_data['amount']

#         if user.balance < amount:
#             return Response({"detail": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Update user balance
#         user.balance -= amount
#         user.save()

#         # Create transaction record
#         Transaction.objects.create(user=user, amount=amount, is_deposit=False)

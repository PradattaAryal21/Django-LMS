from rest_framework import viewsets, status
from rest_framework.response import Response
from .service import TransactionService
from .serializer import TransactionSerializer
from rest_framework.permissions import AllowAny
from core.utils import handle_error
class TransactionViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = TransactionService()
    @handle_error
    def list(self, request):
        Transactions = self.service.get_all_Transactions()
        serializer = TransactionSerializer(Transactions, many=True)
        return Response(serializer.data)
    @handle_error
    def retrieve(self, request, pk=None):
        Transaction = self.service.get_Transaction_by_id(pk)
        if Transaction:
            serializer = TransactionSerializer(Transaction)
            return Response(serializer.data)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
    @handle_error
    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            Transaction = self.service.create_Transaction(serializer.validated_data)
            return Response(TransactionSerializer(Transaction).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @handle_error
    def update(self, request, pk=None):
        serializer = TransactionSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            Transaction = self.service.update_Transaction(pk, serializer.validated_data)
            if Transaction:
                return Response(TransactionSerializer(Transaction).data)
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @handle_error
    def destroy(self, request, pk=None):
        if self.service.delete_Transaction(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

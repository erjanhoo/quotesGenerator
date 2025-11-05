from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from random import random

from .models import Quote, Author
from .serializers import QuoteSerializer


class RandomQuoteView(APIView):
    def get(self, request):
        quotes_count = Quote.objects.count()
        if quotes_count == 0:
            return Response('No quotes available')
        
        random_quote = Quote.objects.get(id=(random(0,quotes_count)))

        return Response({
            'quote': random_quote.quote,
            'author': random_quote.author
        }, status=status.HTTP_200_OK)

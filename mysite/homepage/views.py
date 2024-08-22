from django.shortcuts import render, redirect
from .models import Purchase
import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PurchaseSerializer
from rest_framework import status

class PurchaseView(APIView):
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            store = serializer.validated_data.get("store")
            amount = serializer.validated_data.get("amount_spent")
            date = serializer.validated_data.get("purchase_date")
            products = serializer.validated_data.get("products")
            
            GOOGLE_API_KEY="AIzaSyBsAr6hC4XUqpRZ4CgvUP1J-rgPiPN7Id0"
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"I bought {products} from {store} worth ${amount} on {date}. Did I make an environmentally positive purchase or environmentally negative purchase? Say just one number on a scale from 1 to 10 where 1 is extremely megative and 10 is extremely positive. Don't include a full stop. Only return a number.")
            
            if int(response.text) > 5:
                return Response({"result":"good"}, status=status.HTTP_200_OK)
            elif int(response.text) <= 5:
                return Response({"result":"bad"}, status=status.HTTP_200_OK)

    
    
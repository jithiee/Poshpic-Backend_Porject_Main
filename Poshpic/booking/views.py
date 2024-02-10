from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from . serializer import BookingSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . models import BookingPhotographer


# Create your views here.

class BookingApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk, *args, **kwargs):
        photographer = User.objects.get(id =pk)
        data = {
        "photographer": photographer.id,
            "user": request.user.id,
            **request.data 
            
            # "booking_date": request.data.get("booking_date"),
            # "amount": request.data.get("amount")
            
            }
        
        print(data ,'ddddaaaaaaaatttteeeeeeeeeeeee')
                
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
def get(self, request, pk):
    try:
        if pk is not None:
            bookinguser = BookingPhotographer.objects.get(pk=pk)
            serializer = BookingSerializer(bookinguser)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            booking_users = BookingPhotographer.objects.all()
            serializer = BookingSerializer(booking_users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except BookingPhotographer.DoesNotExist:
        return Response({"detail": "Photographer not found"}, status=status.HTTP_404_NOT_FOUND)

 

    
                
  
            
        
  
                
                
    
    
    
        




        
        
        
        
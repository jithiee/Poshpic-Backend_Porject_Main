from rest_framework import generics
from .models import Message ,Room
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import MessageSerializer,UserGetSerializer , RoomSerializer 
from rest_framework.views import APIView
from account.models import User

# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     ordering = ('-timestamp',)
    



class ListUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_obj = User.objects.exclude(id=request.user.id)
            serializer = UserGetSerializer(user_obj, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            print("error", str(e))
            return Response({"error": "Error in getting user list"}, status=400)


class MessageList(APIView):
    def get(self, request, format=None):
        messages = Message.objects.all().order_by("-timestamp")
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, message_id, format=None):
        try:
            message = Message.objects.get(pk=message_id)
        except Message.DoesNotExist:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )

        message.delete()
        return Response(
            {"message": "Message deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class ChatHistoryView(APIView):
    def get(self, request, room_name):
        try:
            chat_history = Message.objects.filter(room__name=room_name).order_by(
                "timestamp"
            )
            serializer = MessageSerializer(chat_history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DeleteMessageView(APIView):
    def delete(self, request, message_id):
        try:
            message = Message.objects.get(pk=message_id)
            message.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Message.DoesNotExist:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ChatNotification(APIView):
    def get(self, request):
        rooms = Room.objects.filter(name__contains=request.user.username)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
   
   
    
# from .serializer import ChatMessageSerializer
# from . models import ChatMessage
# from rest_framework  import generics
# from django.db.models import Subquery ,OuterRef ,Q
# from account.models import User

# # Create your views here.




# class MyInbox(generics.ListAPIView):
#     serializer_class = ChatMessageSerializer
    
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         message = ChatMessage.objects.filter(id__in = Subquery(
            
#             User.objects.filter(
#                 Q(sender__reciver = user_id)|
#                 Q(reciver__sender  = user_id)
#             ).distinct().annotate(
#                 last_msg = Subquery(
#                     ChatMessage.objects.filter(
#                      Q(sender = OuterRef('id'), receiver= user_id)|
#                      Q(receiver = OuterRef('id'),sender =  user_id )
#                     ).order_by("-id")[:1].values_list("id", flat=True)
#                 )
#             ).values_list("last_msg", flat=True ).order_by("-id")
#           )
                                             
#         ).order_by("-id")
        
#         return message    
    

# class Getmessage(generics.ListAPIView):
#     serializer_class = ChatMessage
    
#     def get_queryset(self):
#         sender_id = self.kwargs['user_id']
#         receiver_id = self.kwargs["user_id"]
        
#         message= ChatMessage.objects.filter(
#             sender__in = [sender_id , receiver_id],
#             receiver__in = [sender_id , receiver_id]
            
#         )
#         return message
    

# class SenntMessage(generics.CreateAPIView):
#     serializer_class = ChatMessageSerializer    
    
    
    
    
    
    
    
    
    
    
    

















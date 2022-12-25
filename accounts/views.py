from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import (
    Profile
)
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    RegisterSerializer
)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data, many=False)

            if(serializer.is_valid()):
                serialized_user = serializer.save()
                user = serialized_user

                is_student = True if data['is_student'] else False
                is_teacher = True if data['is_teacher'] else False
                is_staff = True if data['is_staff'] else False
                is_hod = True if data['is_hod'] else False


                profile = Profile(
                    user = user,
                    is_student=is_student,
                    is_teacher=is_teacher,
                    is_staff=is_staff,
                    is_hod=is_hod
                )
                profile.save()

                profile_serializer = ProfileSerializer(profile, many=False)
                
                return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'Created',
                    'data': profile_serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'Created',
                    'error': serializer.errors},
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response({
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Something went wrong',
                'error': e},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserView(APIView):
    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

class GetUserView(APIView):
    permission_classes =  [IsAuthenticated]
    def post(self, request):
        user_id = request.data.get('id')
        try:
            user = User.objects.get(id=user_id)
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile, many=False)
            return Response({
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Created',
                'data': serializer.data},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Something went wrong',
                'error': e},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

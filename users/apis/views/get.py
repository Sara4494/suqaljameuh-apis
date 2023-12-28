from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import User
from users.apis.serializers import UserSerializer
from rest_framework import status, permissions
from rest_framework import status
from rest_framework import status
from django.db.models import Case, When, Value
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from memberships.models import FeaturedMember, UserMembership
from memberships.apis.serializers import MembershipSerializer
from globals.password_remover import RemovePasswordFromList


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_users(request):
    try:
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'data': serializer.data, 'message': 'Users retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_featured_membership(request):
    try:
        featured_membership = None
        try:
            featured_membership = FeaturedMember.objects.get(
                subscriber=request.user)
        except:
            featured_membership = None

        if featured_membership != None:
            serializer = MembershipSerializer(
                featured_membership.membership, many=False).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting user's membership"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_membership(request):
    try:
        membership = None
        serializer = None
        try:
            membership = UserMembership.objects.get(subscriber=request.user)
        except:
            membership = None

        if membership != None:
            serializer = MembershipSerializer(
                membership.membership, many=False).data

        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while getting user's membership"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_featured_users(request):
    try:

        users = User.objects.exclude(is_superuser=True, user_rank="Normal").order_by(
            Case(
                When(user_rank="Premium", then=Value(0)),
                When(user_rank="Featured", then=Value(1)),
            )
        )
        page = request.query_params.get("page")
        paginator = Paginator(users, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        has_previous = users.has_previous()
        has_next = users.has_next()
        pages = paginator.num_pages

        serializer = UserSerializer(users, many=True)

        return Response({
            "data": RemovePasswordFromList(serializer.data),
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

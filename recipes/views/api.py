from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, TagSerializer
from rest_framework import status
from rest_framework.views import APIView
from tag.models import Tag
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from unicodedata import category
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from ..permissions import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework import status

class RecipeAPIv2ListPagination(PageNumberPagination):
    page_size = 5


class RecipeAPIv2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2ListPagination
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get("category_id", "")
        if category_id != "" and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)
        return qs

    def get_object(self):
        pk = self.kwargs.get("pk",'')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk,
        )
        self.check_object_permissions(self.request, obj)
        return obj
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsOwner(), ]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        print('REQUEST', request.user)
        print(request.user.is_authenticated)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def partial_update(self, request, *args, **kwargs):
        recipe = self.get_object()

        serializer = RecipeSerializer(
            recipe,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)



@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(Tag.objects.all(), pk=pk)
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={"request": request},
    )
    return Response(serializer.data)


# class RecipeAPIv2List(ListCreateAPIView):
#     queryset = Recipe.objects.get_published()
#     serializer_class = RecipeSerializer
#     pagination_class = RecipeAPIv2ListPagination

# class RecipeAPIv2Detail(RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.get_published()
#     serializer_class = RecipeSerializer
#     pagination_class = RecipeAPIv2ListPagination

#     def patch(self, request, *args, **kwargs):
#         # Delegate to DRF's built-in partial update flow
#         return self.partial_update(request, *args, **kwargs)


# class RecipeAPIv2List(APIView):
#     def get(self, request):
#         recipes = Recipe.objects.get_published()[:10]
#         serializer = RecipeSerializer(
#             instance=recipes,
#             many=True,
#             context={"request": request},
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = RecipeSerializer(
#             data=request.data,
#             context={"request": request},
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class RecipeAPIv2Detail(APIView):
#     def get_recipe(self, pk):
#         recipe = get_object_or_404(Recipe.objects.get_published(), pk=pk)
#         return recipe

#     def get(self, request, pk):
#         recipe = self.get_recipe(pk)
#         serializer = RecipeSerializer(
#             instance=recipe,
#             many=True,
#             context={"request": request},
#         )
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         recipe = self.get_recipe(pk)
#         serializer = RecipeSerializer(
#             instance=recipe,
#             data=request.data,
#             many=False,
#             context={"request": request},
#             partial=True,
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             serializer.data,
#         )

#     def delete(self, request, pk):
#         recipe = self.get_recipe(pk)
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(http_method_names=["get", "post"])
# def recipe_api_list(request):
#     if request.method == "GET":
#         recipes = Recipe.objects.get_published()[:10]
#         serializer = RecipeSerializer(
#             instance=recipes,
#             many=True,
#             context={"request": request},
#         )
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = RecipeSerializer(
#             data=request.data,
#             context={"request": request},
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(http_method_names=["get", "patch", "delete"])
# def recipe_api_detail(request, pk):
#     recipe = get_object_or_404(Recipe.objects.get_published(), pk=pk)
#     if request.method == "GET":
#         serializer = RecipeSerializer(
#             instance=recipe,
#             many=False,
#             context={"request": request},
#         )
#         return Response(serializer.data)
#     elif request.method == "PATCH":
#         serializer = RecipeSerializer(
#             instance=recipe,
#             data=request.data,
#             many=False,
#             context={"request": request},
#             partial=True,
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             serializer.data,
#         )
#     elif request.method == "DELETE":
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def tag_api_detail(request, pk):
#     tag = get_object_or_404(Tag.objects.all(), pk=pk)
#     serializer = TagSerializer(instance=tag, many=False, context={"request": request})
#     return Response(serializer.data)

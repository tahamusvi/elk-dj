from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if "page" in request.query_params:
            if "page_size" in request.query_params:
                self.page_size = request.query_params["page_size"]
            return super().paginate_queryset(queryset, request, view)
        else:
            return None

    def get_paginated_response(self, data):
        if self.page is not None:
            response = super().get_paginated_response(data)
            ordered_response_data = OrderedDict(
                {
                    "total_pages": self.page.paginator.num_pages,
                    "has_next": self.page.has_next(),
                    "has_previous": self.page.has_previous(),
                    "total_items": response.data["count"],
                    "items": response.data["results"],
                }
            )
            return Response(ordered_response_data)
        return Response(data)


class PaginatedActionMixin:
    def paginated_action(self, queryset, serializer_class):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


class PaginatedActionAPIViewMixin:
    def paginated_action(self, queryset, serializer_class):
        paginator = self.pagination_class
        # queryset = queryset.order_by('-id')
        page = paginator.paginate_queryset(queryset, self.request)
        if page is not None:
            serializer = serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


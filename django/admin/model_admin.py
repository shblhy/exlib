from django.contrib.admin import ModelAdmin as ModelAdmin_
from django.db import models, router, transaction
from django.contrib.admin.utils import unquote

from django.contrib.admin.options import csrf_protect_m, TO_FIELD_VAR
from django.core.exceptions import (
    FieldDoesNotExist,
    FieldError,
    PermissionDenied,
    ValidationError,
)


class ModelAdmin(ModelAdmin_):
    @csrf_protect_m
    def detail_view(self, request, object_id, extra_context=None):
        return self._detail_view(request, object_id, extra_context)

    def _detail_view(self, request, object_id, extra_context):
        to_field = request.GET.get(TO_FIELD_VAR)
        obj = self.get_object(request, unquote(object_id), to_field)
        model = self.model
        opts = model._meta
        if not self.has_view_permission(request, obj):
            raise PermissionDenied

        if obj is None:
            return self._get_obj_does_not_exist_redirect(request, opts, object_id)

        return self.render_change_form(
            request, context, add=add, change=not add, obj=obj, form_url=form_url
        )


from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.contrib.admin.templatetags.admin_list import register, result_headers, result_hidden_fields, results


def result_list_opertions(cl):
    """
    Display the headers and data list together.
    """
    headers = list(result_headers(cl))
    num_sorted_fields = 0
    for h in headers:
        if h["sortable"] and h["sorted"]:
            num_sorted_fields += 1
    return {
        "cl": cl,
        "result_hidden_fields": list(result_hidden_fields(cl)),
        "result_headers": headers,
        "num_sorted_fields": num_sorted_fields,
        "results": list(results(cl)),
    }


@register.tag(name="result_list_opertions")
def result_list_tag(parser, token):
    return InclusionAdminNode(
        parser,
        token,
        func=result_list_opertions,
        template_name="change_list_results_operations.html",
        takes_context=False,
    )
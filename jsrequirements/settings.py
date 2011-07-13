from django.conf import settings

VARNAME = getattr(settings, 'JS_REQUIREMENTS_VARNAME', 'JS_REQUIREMENTS_CONTENT_HOLDER')
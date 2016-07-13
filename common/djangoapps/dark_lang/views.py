"""
Views file for the Darklang Django App
"""
from openedx.core.lib.api.view_utils import view_auth_classes
from django.views.generic.base import View

from edxmako.shortcuts import render_to_response

from .darklang import Darklang

SET_LANGUAGE_CODE = 'set_language_code'

@view_auth_classes()
class DarkLangView(View):
    """
    View used when a user is attempting to change the preview language using Darklang.

    Expected Behavior:
    GET - returns a form for setting/resetting the user's dark language
    POST - updates the setting to the given dark language
    DELETE - removes the dark language settings and resets to default behavior

    Note: This class and View are meant to replace DarkLang as a middleware, which was determined to be a
    security risk.
    """
    template_name = 'darklang/preview_lang.html'

    def get(self, request, error=None):
        """
        Displays the Form for setting/resetting a User's dark language setting
        :param request: The Django Request Object
        :return: View containing the form for setting the preview lang
        """
        context = {
            'disable_courseware_js': True,
            'uses_pattern_library': True
        }
        return render_to_response(self.template_name, context)

    def post(self, request):
        context = {
            'disable_courseware_js': True,
            'uses_pattern_library': True
        }
        darklang = Darklang()
        result = darklang.process_darklang_request(request)
        if result is not None:
            context.update({SET_LANGUAGE_CODE: result})
        return render_to_response(self.template_name, context)



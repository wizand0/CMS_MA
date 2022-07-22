from django.conf import settings as conf_settings

def header(request):

    app_version = conf_settings.APP_VERSION

    context = {

        'app_version': app_version,
    }
    return render(request, context)
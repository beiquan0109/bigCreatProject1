from import_export import resources
from .models import stkStatus

class stkResource(resources.ModelResource):

    class Meta:
        model = stkStatus
        exclude = ['id']
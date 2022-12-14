from rest_framework.permissions import DjangoModelPermissions

# ! django model permission default olarak GET metodlarına bir permission belirlemiyor. Bu sebeple kendi 'GET' metodumuzu belirlemek için permissions'ı overwrite ediyoruz
class CustomModelPermission(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
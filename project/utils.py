from django.db.models import Model


def query_all(obj:Model) -> Model:
    return obj.objects.all()

def filter_query(obj:Model, *args, **kwargs) -> Model:
    return obj.objects.filter(*args, **kwargs)

def get_object(obj:Model,*args, **kwargs) -> Model:
    return obj.objects.get(*args, **kwargs)

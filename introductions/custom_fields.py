from django.db import models

class NullableCharField(models.CharField):
    description = "CharField that obeys null=True"

    def get_db_prep_value(self, value, *args, **kwargs):
        my_value = super(NullableCharField, self).get_db_prep_value(value, *args, **kwargs)
        return my_value or None


    def to_python(self, value):
        if isinstance(value, models.CharField):
            return value
        return value or ""

    def get_internal_type(self):
        return "CharField"

    def south_field_triple(self):
        "Returns a suitable description of this field for South"
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

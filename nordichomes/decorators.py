from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify


def autoslug(fieldname):
    def decorator(model):
        # some sanity checks first
        assert hasattr(model, fieldname), f"Model has no field {fieldname!r}"
        assert hasattr(model, "slug"), "Model is missing a slug field"

        @receiver(models.signals.pre_save, sender=model, weak=False)
        def generate_slug(sender, instance, *args, raw=False, **kwargs):
            if not raw:
                source = getattr(instance, fieldname)
                slug = slugify(source)
                if slug:  # not all strings result in a slug value
                    instance.slug = slug
        return model
    return decorator
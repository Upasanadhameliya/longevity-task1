import random

def random_bool_fields(model,field="BooleanField"):
    return {
                f.name: random.choice([True, False])
                for f in model._meta.get_fields()
                if f.get_internal_type() == field
            }

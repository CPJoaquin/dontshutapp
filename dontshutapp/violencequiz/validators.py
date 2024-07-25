from django.core.exceptions import ValidationError

def clean_question(value):
        if not value.islower():
            raise ValidationError("Los nombres de usuario deben estar en minúsculas")
        if any(char in value for char in ['@', '-', '|']):
            raise ValidationError("Los nombres de usuario no deben contener caracteres especiales.")
        return value
def clean_phone(value):
        if not value:
            raise ValidationError("El campo no puede estar vacío.")
        if not any(char in value for char in ['1','2','3','4','5','6','7','8','9','0']):
            raise ValidationError("El telefono debe ser numerico")
        return value
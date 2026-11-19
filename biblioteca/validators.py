
from django import forms


def validate_file_size(file):
    limit_mb = 2
    if file.size > limit_mb * 1024 * 1024: 
        raise forms.ValidationError(f"O arquivo deve ter no máximo {limit_mb} MB.")
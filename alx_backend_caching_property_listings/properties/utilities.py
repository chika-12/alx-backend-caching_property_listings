import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
load_dotenv()

def verify_os_variables(var_name):
  variable = os.getenv(var_name)
  if variable is None:
    raise ImproperlyConfigured(f"{var_name} cant be found")
  return variable
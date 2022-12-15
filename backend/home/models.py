from django.conf import settings
from django.db import models
class Test(models.Model):
    'Generated Model'
    title = models.CharField(max_length=256,)
    def test_method(self):
        response = requests.get('https://hello.com')
        return response

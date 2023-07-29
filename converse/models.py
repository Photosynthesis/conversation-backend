from django.db import models
# from django_better_admin_arrayfield.models.fields import ArrayField
    

class Scenario(models.Model):
    name = models.CharField("Name", max_length=240)
    description = models.TextField()
  

    def __str__(self):
        return self.name



class Prompt(models.Model):
    name = models.CharField("Name", max_length=240)
    prompt_type = models.CharField("Type", max_length=240)
    tags = models.CharField("Tags", max_length=240)
    audio_file = models.FileField("Audio file", upload_to='prompt_audio')

    def __str__(self):
        return self.name
    
class PromptGroup(models.Model):
    name = models.CharField("Name", max_length=240)
    tag = models.CharField("Matches tag", max_length=240)
    icon = models.FileField("Icon file", upload_to='prompt_group_icons', blank=True)
    position = models.FloatField("List position")
    is_active = models.BooleanField("Active")

    def __str__(self):
        return self.name   

from django.db import models
# from sortedm2m.fields import SortedManyToManyField
# from django_better_admin_arrayfield.models.fields import ArrayField
    


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


class Scenario(models.Model):
    name = models.CharField("Name", max_length=240)
    description = models.TextField("Description")
    intro_audio_file = models.FileField("Intro audio file", upload_to='prompt_audio', blank=True)
    #prompts = models.ManyToManyField(Prompt)
    #scenario = models.TextField("Scenario JSON", blank=True)
    #scenario_json = models.JSONField("Scenario JSON test", blank=True)
    prompts = models.ManyToManyField(Prompt, through="ScenarioPrompt")
  

    def __str__(self):
        return self.name

class ScenarioPrompt(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    position = models.FloatField("List position")
    trigger = models.CharField("Trigger type", max_length=240)
    delay = models.IntegerField("Delay (seconds)")
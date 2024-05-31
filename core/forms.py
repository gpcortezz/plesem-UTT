from django import forms

from core import models

class NewGrantGoalForm(forms.ModelForm):
    class Meta:
        model = models.GrantGoal
        fields = [
            "ggname",
            "user",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "ggname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }


class UpdateGrantGoalForm(forms.ModelForm):
    class Meta:
        model = models.GrantGoal
        fields = [
            "ggname",
            "user",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "ggname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }

### SUBGRANTGOALS FORMS ###

class NewSubGrantGoalForm(forms.ModelForm):
    class Meta:
        model = models.SubGrantGoal
        fields = [
            "sggname",
            "user",
            "area",
            "grantgoal",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "ggname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "area": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "grantgoal": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }
class UpdateSubGrantGoalForm(forms.ModelForm):
    class Meta:
        model = models.SubGrantGoal
        fields = [
            "sggname",
            "user",
            "area",
            "grantgoal",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "ggname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "area": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "grantgoal": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }


        #### GOALS FORMS ###
class NewGoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = [
            "goalname",
            "user",
            "area",
            "subgrantgoal",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "goalname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el goal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el goal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "area": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "subgrantgoal": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el goal slug!"}),
        }
class UpdateGoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = [
            "goalname",
            "user",
            "area",
            "subgrantgoal",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "goalname": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "area": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "subgrantgoal": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}),
        }
### ISSUES FORMS ###
class NewIssueForm(forms.ModelForm):
    class Meta:
        model = models.Issue
        fields = [
            "issuename",
            "user",
            "area",
            "goal",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "issuename": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el goal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el goal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "area": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "goal": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el goal slug!"}),
        }

class UpdateIssueForm(forms.ModelForm):
    class Meta:
        model = models.Issue
        fields = [
            "issuename",
            "user",
            "area",
            "goal",
            "description",
            "days_duration",
            "state",
            "priority",
            "slug"
        ]
        widgets = {
            "issuename": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el issue name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el issue description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "area": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "goal": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "priority": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "state": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el issue slug!"}),
        }
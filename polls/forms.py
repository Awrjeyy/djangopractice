from dataclasses import Field
from django import forms
from django.http import Http404, HttpResponseRedirect
from .models import Choice, Question
from . import views
from django.urls import reverse
from django.shortcuts import get_object_or_404,render



def form(id):
    
    class DetailForm(forms.ModelForm):
        # qchoices = forms.ChoiceField(choices=Choice, widget=forms.RadioSelect)
        
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['choice'] = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)
            self.fields['choice'].queryset = Choice.objects.filter(question_id=id)

        class Meta:
            model = Choice
            fields = {'id'}
            widgets = {Field : forms.RadioSelect, }

    return DetailForm

# class DetailForm(forms.ModelForm):
    

#     def get(request, question_id):
#         field1 = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)
#         question = get_object_or_404(Question, pk=question_id)
#         print(str(question_id))
#         field1.queryset = Choice.objects.filter(question_id=question_id)
#         if Choice.DoesNotExist:
#             return render(request, 'polls/detail.html', {
#                 'question' : question,
#                 'error_message' : "You didn't select a choice",
#             })
#         else:
#             return HttpResponseRedirect(reverse('polls:reuslts', args=(question_id,)))
  
#     class Meta:
#         model = Choice
#         fields = {'id'}
#         widgets = {Field : forms.RadioSelect,}

# def get_question(all_choices):
#         #Specify the field needed for the form
#         #use query(?)
#         #Look for question.id
#         #Check if its valid(maybe) or compare if query and question.id are same
#         #Make a for loop
#         #Use def vote(???)
#         model = Question
#         Choices = all_choices
        

    # def post(self, request, pk):
    #     form = DetailForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/polls/')
    #     else:
    #         form = NameForm()
    #     return render(request, 'polls/detail.html', {'detail': detail})
#     from django import forms
# from django.http import Http404
# from .models import Choice, Question
# from django.shortcuts import get_object_or_404,render
# from .models import Choice, Question

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
#     your_age = forms.IntegerField(max_value=100)

# class DetailForm(forms.Form):
    
    
#     Choices = [('M','Male'), ('F','Female')

#     ]
#     like = forms.ChoiceField(label="Your Gender",choices=Choices, widget=forms.RadioSelect)


#     # def post(self, request, pk):
#     #     form = DetailForm(request.POST)
#     #     if form.is_valid():
#     #         return HttpResponseRedirect('/polls/')
#     #     else:
#     #         form = NameForm()
#     #     return render(request, 'polls/detail.html', {'detail': detail})
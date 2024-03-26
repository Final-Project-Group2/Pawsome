from typing import Any, Sequence
from django import forms
from .models import Pet, CustomerUser
from django.core.validators import RegexValidator
from backend.models import Species 
from .more_settings import  GROUPS, TWO_VALUES_OPT
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
import asyncio





class Selector(forms.Select):
      def __init__(self, attrs, choices) -> None:
            self.attrs = attrs
            self.choices = choices
            self.loadopt()
            super().__init__(attrs, choices)


      def loadopt(self,in_data=GROUPS, name=None,attrs=None):
            data=dict()
            if issubclass(dict,in_data.__class__):
                  if ("name", "value") in in_data.keys():
                        key, iterable = in_data["name"], in_data["value"]
                        data[key] = [(self.create_option(*val) for val in iterable)]
                        self.subwidgets(key,data[key],{'class':'p-2'}) 
                  else:
                        for name,values in in_data.items() :
                              data[name] = self.loadopt(values)
                              self.subwidgets(name,data[name],{'class':'p-2'})      
            elif issubclass(list, in_data.__class__) and issubclass(tuple, in_data[0].__class__):
                  data=[(self.create_option(*val) for val in in_data)]      
                  self.subwidgets(in_data.__class__.__name__, data, {'class':'p-2'})
                  
class MultiSelectWidget(forms.MultiWidget):
      
      def __init__(self,widgets=None,attrs=None ):
            data = TWO_VALUES_OPT
            s={"class":"p-2"}
            self.widgets = [
                  Selector(s,choices=data["SPECIES"]),
                  Selector(s, choices=data["GENDER"]),
                  Selector(s,choices=data["SIZE"]),
                  Selector(s, choices=data["STATUS"]),
                  Selector(s, choices=data["BREED"]),
            ]
            super(MultiSelectWidget, self).__init__(self.widgets, attrs)
            
      def decompress(self, value):
            if value:
                  return {"species":value["species"], "size":value["size"]}
            return [None, None]

      def format_output(self, rendered_widgets):
            return ''.join(rendered_widgets)

class MultiSelectField(forms.MultiValueField):
      def __init__(self,widget=None,*a,**kw):
            self.localize = True
            self.label='Shelters'
            self.data=TWO_VALUES_OPT
            fields = [
                  forms.ChoiceField(choices=self.data["SPECIES"]),
                  forms.ChoiceField(choices=self.data["GENDER"]),
                  forms.ChoiceField(choices=self.data["SIZE"]),
                  forms.ChoiceField(choices=self.data["STATUS"]),
                  forms.ChoiceField(choices=self.data["BREED"]),
            
            ]
            super(MultiSelectField,self).__init__(fields, widget=MultiSelectWidget,*a,**kw)
            
      def compress(self, data_list):
            return {
                  'species': data_list[0],
                  'gender':data_list[1],
                  'size': data_list[2],
                  'status':data_list[3],
                  'breed':data_list[4],
            }
      
      
class PetForm(forms.ModelForm):

      class Meta:

            model=Pet
            fields=["name"]
            widgets={
                  "name":forms.TextInput({"class":"form-control shadow fs-3 m-auto"}),
                  #"size": forms.Select(attrs={"class":"shadow fs-3 m-auto","style":"width:100%;","id":"size",},choices=sizes_options),
                  #"species": MultiSelectField(datadict=V,widgets=MultiSelectWidget(V)),
            
            }
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            runtime_field=MultiSelectField()
            runtime_field.widget=MultiSelectWidget()
            self.fields["species"] = runtime_field



class CustomerUserForm(forms.ModelForm):
      class Meta:
            model= CustomerUser
            fields ="__all__" 




class AdminForm(UserChangeForm):
      class Meta:
            model = CustomerUser
            fields=UserChangeForm.Meta.fields 
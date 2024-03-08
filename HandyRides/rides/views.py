from django.shortcuts import render
from django.shortcuts import redirect

from .forms import RideForm, NewRideForm

from .models import Person

# relative import of forms
from .forms import RideForm

# Create your views here.


def index(request):
  context = {}

  possible_entries = ['origination_city', 'origination_state', 'destination_city', 'destination_state', 'date', 'time', 'seats']
  if request.method == 'GET' and any(field in request.GET for field in possible_entries):
      origination_city = request.GET.get('origination_city', '')
      origination_state = request.GET.get('origination_state', '')
      destination_city = request.GET.get('destination_city', '')
      destination_state = request.GET.get('destination_state', '')
      date = request.GET.get('date', '')
      time = request.GET.get('time', '')
      seats = request.GET.get('seats', '')

      context['people'] = Person.objects.filter(
            origination_city__icontains=origination_city,
            origination_state__icontains=origination_state,
            destination_city__icontains=destination_city,
            destination_state__icontains=destination_state,
            date__icontains=date,
            time__icontains=time,
            seats_available__icontains=seats
        )
      return render(request, 'search_results.html', context)

  context['form'] = RideForm()
  return render(request, 'index_view.html', context)

def create(request):
  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()
  return redirect("/rides")

def create_rides(request):
  context = {}
  context["new_ride_form"] = NewRideForm()
  return render(request, "create_rides.html",context)


def display_rides(request):
  return render(request, "search_results.html")


# AI_INTERACTION
""""
import os
from transformers import pipeline
from .models import Person

def ai_interaction(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        rides_data = Person.objects.all()

        system_message = f"You are trying to help folks get rides based on the data you have in your database: {rides_data}"
        

        # Combine system message and user input
        prompt = f"{system_message} {user_input} AI:"
        
        # Load the text generation pipeline with the desired model
        generator = pipeline("text-generation", model="openai-community/gpt2")
        
        # Generate text based on combined prompt
        ai_text = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        final_ai_text = ai_text.split("AI:")[-1].split()

        return render(request, 'index_view.html', {'ai_text': final_ai_text})
    
    return render(request, 'index_view.html')
"""

# OPEN AI VERSION
# PRINCETON: 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
# PERSONAL: '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'
import os
from langchain_openai import OpenAI

def ai_interaction(request):
  context = {}
  context['form'] = RideForm()
  os.environ["OPENAI_API_KEY"] = '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'

  if request.method == 'POST':
        input_text = request.POST.get('user_input')
        rides_data = Person.objects.all()

        # Format rides_data into a string
        rides_data_str = '\n'.join([f"(First Name: {person.first_name}, Last Name: {person.last_name}, Email: {person.email}, Phone Number: {person.phone_number}, Origination City: {person.origination_city}, Origination State: {person.origination_state}, Destination City: {person.destination_city}, Destination State: {person.destination_state}, Vehicle Type: {person.vehicle_type}, Vehicle Model: {person.vehicle_model}, Date: {person.date}, Time: {person.time}, Taking Passengers: {person.taking_passengers}, Seats Available: {person.seats_available})" for person in rides_data])

        prompt = f"{input_text}. If applicable you can also use data from:{rides_data_str} where each individual person trip plan is seperated by '()' "
        
        llm = OpenAI(temperature=0.8)

        if input_text:
            ai_text = llm(prompt)
            return render(request, 'AI_page.html', {'user_input': prompt, 'ai_text': ai_text}) #{'user_input': prompt, 'ai_text': ai_text}

  return render(request, 'index_view.html',context)




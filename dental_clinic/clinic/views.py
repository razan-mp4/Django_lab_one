from django.shortcuts import render

# Fixed data for the application
patients = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'dob': '1980-01-01', 'address': '123 Main St', 'phone': '123-456-7890'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'dob': '1985-05-05', 'address': '456 Oak Ave', 'phone': '987-654-3210'},
]

dentists = [
    {'id': 1, 'first_name': 'Alice', 'last_name': 'Brown', 'specialty': 'Orthodontist'},
    {'id': 2, 'first_name': 'Bob', 'last_name': 'Green', 'specialty': 'General Dentist'},
]

appointments = [
    {'id': 1, 'patient': patients[0], 'dentist': dentists[0], 'date': '2024-06-05 10:00', 'notes': 'Regular check-up'},
    {'id': 2, 'patient': patients[1], 'dentist': dentists[1], 'date': '2024-06-06 11:00', 'notes': 'Teeth cleaning'},
]

treatments = [
    {'id': 1, 'name': 'Filling', 'cost': 100},
    {'id': 2, 'name': 'Root Canal', 'cost': 300},
]

invoices = [
    {'id': 1, 'patient': patients[0], 'amount': 150, 'date': '2024-06-05'},
    {'id': 2, 'patient': patients[1], 'amount': 350, 'date': '2024-06-06'},
]

feedbacks = [
    {'id': 1, 'patient': patients[0], 'dentist': dentists[0], 'rating': 5, 'comments': 'Great service!'},
    {'id': 2, 'patient': patients[1], 'dentist': dentists[1], 'rating': 4, 'comments': 'Very professional.'},
]

def home(request):
    return render(request, 'clinic/home.html')

def appointments_view(request):
    return render(request, 'clinic/appointments.html', {'appointments': appointments})

def treatments_view(request):
    return render(request, 'clinic/treatments.html', {'treatments': treatments})

def invoices_view(request):
    return render(request, 'clinic/invoices.html', {'invoices': invoices})

def feedbacks_view(request):
    return render(request, 'clinic/feedbacks.html', {'feedbacks': feedbacks})

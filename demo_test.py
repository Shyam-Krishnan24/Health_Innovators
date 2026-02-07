#!/usr/bin/env python
"""
Quick demo script to test IVR without needing microphone input.
This simulates a non-emergency call with voice disabled.
"""
import sys
import os

# Add Frontend folder to path
frontend_dir = os.path.join(os.path.dirname(__file__), "Front-End (IVR system)")
sys.path.insert(0, frontend_dir)

# Switch to frontend directory so relative paths work
os.chdir(frontend_dir)

# Import IVR components
from db import create_table, populate_sample_data
from languages import LANGUAGES
from symptoms import SYMPTOMS
from ai_engine import calculate_urgency, assign_priority
from scheduler import generate_token
from db import save_call

def demo_non_emergency_call():
    """Demonstrate a non-emergency flow and show results."""
    print("\n" + "="*80)
    print("HEALTH IVR SYSTEM - DEMO TEST".center(80))
    print("="*80)
    
    # Initialize database
    create_table()
    try:
        populate_sample_data()
    except:
        pass
    
    # Simulate a non-emergency call
    print("\n[TEST] Simulating a Non-Emergency Call")
    print("-" * 80)
    
    language = "English"
    symptom = "Fever"
    age = 45
    gender = "Female"
    status = "Normal"
    past_surgery = False
    medications = "None"
    patient_name = "Demo Patient"
    patient_phone = "+918765432109"
    
    # Calculate urgency using AI engine
    data = {
        "symptom": symptom,
        "age": age,
        "status": status,
        "past_surgery": past_surgery,
        "medications": medications
    }
    
    score = calculate_urgency(data)
    priority = assign_priority(score)
    token = generate_token(priority)
    
    print(f"Language             : {language}")
    print(f"Patient Name         : {patient_name}")
    print(f"Patient Phone        : {patient_phone}")
    print(f"Symptom              : {symptom}")
    print(f"Age                  : {age}")
    print(f"Gender               : {gender}")
    print(f"Status               : {status}")
    print(f"Past Surgery         : {'Yes' if past_surgery else 'No'}")
    print(f"Medications          : {medications}")
    print(f"\nAI Analysis:")
    print(f"  Urgency Score      : {score}/100")
    print(f"  Priority Level     : {priority}")
    print(f"  Token Generated    : {token}")
    
    if priority in ["A", "B"]:
        print(f"\n[RESULT] ESCALATED TO EMERGENCY - Appointment offered")
        call_type = "Non-Emergency (Escalated)"
    else:
        print(f"\n[RESULT] Normal consultation flow")
        call_type = "Non-Emergency"
    
    # Save to database
    save_call({
        "patient_name": patient_name,
        "patient_phone": patient_phone,
        "language": language,
        "call_type": call_type,
        "symptom": symptom,
        "age": age,
        "gender": gender,
        "status": status,
        "past_surgery": past_surgery,
        "medications": medications,
        "urgency_score": score,
        "priority": priority,
        "token": token
    })
    
    print(f"\n[SUCCESS] Record saved to database!")
    print("="*80)
    print("\nTo view all records, run:")
    print("  python view_data.py")
    print("\nTo run the full interactive IVR, run:")
    print("  python main.py")
    print("="*80 + "\n")

if __name__ == "__main__":
    demo_non_emergency_call()

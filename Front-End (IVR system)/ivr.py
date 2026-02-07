from languages import LANGUAGES
from symptoms import SYMPTOMS
from ai_engine import calculate_urgency, assign_priority
from scheduler import generate_token
from db import save_call


def start_call():
    print("\nSelect Language:")
    for k, v in LANGUAGES.items():
        print(f"{k}. {v['name']}")

    lang = input("Choice: ")
    language = LANGUAGES.get(lang, LANGUAGES["1"])["name"]
    print(LANGUAGES.get(lang, LANGUAGES["1"])["welcome"])

    print("\nPress 1 for Emergency")
    print("Press 2 for Non-Emergency")
    call_type = input("Choice: ")

    if call_type == "1":
        handle_emergency(language)
    else:
        handle_non_emergency(language)


def handle_non_emergency(language):
    print("\nSelect Symptom:")
    for k, v in SYMPTOMS.items():
        print(f"{k}. {v}")

    s = input("Choice: ")
    symptom = SYMPTOMS.get(s, "Unknown")

    if s == "0":
        symptom = input("Describe your symptoms: ")

    age = int(input("Enter age: "))

    print("Gender:")
    print("1. Male")
    print("2. Female")
    print("3. Non-binary")
    gender_map = {"1": "Male", "2": "Female", "3": "Non-binary"}
    gender = gender_map.get(input("Choice: "), "Unknown")

    print("Status:")
    print("1. Normal")
    print("2. Child")
    print("3. Pregnant")
    status_map = {"1": "Normal", "2": "Child", "3": "Pregnant"}
    status = status_map.get(input("Choice: "), "Normal")

    past_surgery = input("Past surgery? (yes/no): ").lower() == "yes"
    medications = input("Current medications (leave blank if none): ")

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

    print(f"\nAI Urgency Score: {score}")
    print(f"Priority Level: {priority}")
    print(f"Your token number is: {token}")

    if priority in ["A", "B"]:
        print("Please proceed immediately to the emergency desk.")
    else:
        print("You may wait for routine consultation.")

    # ✅ Save to database
    save_call({
        "language": language,
        "call_type": "Non-Emergency",
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

    print("\nYour details have been recorded successfully.")


def handle_emergency(language):
    token = generate_token("A")

    print("\nEmergency case registered.")
    print(f"Your priority token is {token}")
    print("Please proceed immediately.")

    # ✅ Save emergency call to database
    save_call({
        "language": language,
        "call_type": "Emergency",
        "symptom": "Emergency Call",
        "age": None,
        "gender": None,
        "status": None,
        "past_surgery": False,
        "medications": None,
        "urgency_score": 100,
        "priority": "A",
        "token": token
    })

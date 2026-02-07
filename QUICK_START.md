# Quick Start Guide - Health IVR System

## ONE-COMMAND START

### From Root Directory
```bash
python main.py
```

### Direct Frontend
```bash
cd "Front-End (IVR system)"
python main.py
```

---

## THREE ESSENTIAL COMMANDS

### 1. Run IVR (Interactive Voice Response)
```bash
python main.py
```
- Greets the caller in selected language
- Collects symptoms, patient details, medical history
- AI engine analyzes and prioritizes
- Generates token and saves to database

### 2. View All Patient Records
```bash
python view_data.py
```
- Shows all recorded calls
- Displays patient details, symptoms, AI scores, priority levels, tokens
- Displays in formatted table

### 3. Run Automated Demo
```bash
python demo_test.py
```
- Tests system without microphone
- Shows AI analysis with sample data
- Verifies database integration

---

## WHAT HAPPENS IN EACH CALL TYPE

### EMERGENCY (Option 1)
```
Ask for issue
Ask for patient name
Ask for phone number
↓
Assign Priority A (Highest)
Generate token: A-ER-001
Save to database
Announce token
End call
```

### NON-EMERGENCY (Option 2)
```
Ask for symptom (1-9 or voice)
Ask for age
Ask for gender (1=Male, 2=Female, 3=Non-binary)
Ask for status (1=Normal, 2=Child, 3=Pregnant)
Ask for past surgery (yes/no)
Ask for medications
↓
AI ANALYSIS (calculate urgency score)
↓
IF Score ≥ 90 or risky symptoms → ESCALATE TO EMERGENCY
   - Ask: Book appointment? (1=Yes, 2=No)
   - If yes → Collect name/phone → Save as Priority A/B
   - If no → Save record → End
↓
ELSE → Normal consultation
   - Generate token (C or D priority)
   - Save to database
   - End call
```

---

## DATABASE RECORDS SHOWN

Each record displays:
- **ID** - Record number
- **Patient Name** - Full name
- **Phone** - Contact number
- **Language** - Selected language
- **Call Type** - Emergency/Non-Emergency/Escalated
- **Symptom** - Medical issue
- **Age** - Patient age
- **Gender** - Male/Female/Non-binary
- **Status** - Normal/Child/Pregnant
- **Past Surgery** - Yes/No
- **Medications** - Current meds
- **Urgency Score** - AI calculated (0-100)
- **Priority** - A/B/C/D level
- **Token** - Generated token (A-ER-001 format)
- **Timestamp** - Call date/time

---

## PRIORITY LEVELS

| Priority | Score | Description | Action |
|----------|-------|-------------|--------|
| **A** | ≥90 | EMERGENCY | Urgent desk immediately |
| **B** | ≥70 | HIGH | Priority appointment |
| **C** | ≥40 | MEDIUM | Routine appointment |
| **D** | <40 | LOW | Normal consultation |

---

## AI URGENCY SCORING

```
SYMPTOM RISK
- Chest Pain, Breathing Difficulty, Injury/Bleeding: +50
- Other symptoms: +20

AGE RISK
- Age > 60: +15

SPECIAL STATUS RISK
- Child: +20
- Pregnant: +20

MEDICAL HISTORY RISK
- Past Surgery: +10
- Current Medications: +5

TOTAL = Min(sum, 100)
```

---

## SYMPTOM OPTIONS (List 1-9)

When asked to select symptom:
```
1 - Fever
2 - Headache
3 - Chest Pain ⚠️ HIGH RISK
4 - Breathing Difficulty ⚠️ HIGH RISK
5 - Abdominal Pain
6 - Vomiting / Nausea
7 - Dizziness / Fainting
8 - Injury / Bleeding ⚠️ HIGH RISK
9 - Fatigue / Weakness
0 - Voice Description (speak freely)
```

---

## EXAMPLE: Full Call Flow

```
SYSTEM: Welcome to Smart Health IVR

Select Language:
1. English
USER: 1

Press 1 for Emergency. Press 2 for Non-Emergency.
USER: 2

Select Symptom (1-9):
USER: 3 (Chest Pain)

Enter age:
USER: 65

Gender: 1. Male  2. Female  3. Non-binary
USER: 1

Status: 1. Normal  2. Child  3. Pregnant
USER: 1

Past surgery? (yes/no):
USER: yes

Medications:
USER: Aspirin

[AI ANALYSIS]
Urgency Score: 80
Priority: B

SYSTEM: This case is classified as emergency.
Press 1 to Book Appointment. Press 2 to Leave.
USER: 1

Full name:
USER: John Smith

Phone number:
USER: 9876543210

SYSTEM: Appointment confirmed. Token: B-ER-001
Please proceed to emergency desk.

[RECORD SAVED TO DATABASE]
Name: John Smith
Phone: 9876543210
Symptom: Chest Pain
Age: 65
Score: 80
Priority: B
Token: B-ER-001
```

---

## TROUBLESHOOTING QUICK FIXES

| Issue | Fix |
|-------|-----|
| "Can't find main.py" | Ensure you're in Health_Innovators root folder |
| "health.sqlite not found" | Run `python main.py` first to create database |
| "No microphone" | That's OK! Type your responses instead |
| "Import error" | Run `python -m pip install pyttsx3 SpeechRecognition` |
| "Python not found" | Install Python 3.8+ from python.org |
| "Permission denied" | Right-click terminal > Run as Administrator (Windows) |

---

## FILES YOU INTERACT WITH

### TO RUN
- **main.py** - Main entry point (run this!)
- **demo_test.py** - Test without microphone

### TO VIEW DATA
- **view_data.py** - Display all records

### AUTO CREATED
- **health.sqlite** - Database (created automatically)

### REFERENCE
- **PROTOTYPE_GUIDE.md** - Full documentation
- **README.md** - Project overview

---

## INSTALLATION (One-Time Only)

```bash
python -m pip install -r "Front-End (IVR system)/requirements.txt"
```

---

## TESTING CHECKLIST

✅ Start system: `python main.py`
✅ Select language: Press 1 (English)
✅ Emergency test: Press 1 → Name John → Phone 9876543210
✅ Non-emergency test: Press 2 → Symptom 1 → Age 25 → Gender 2 → Status 1 → No surgery → No meds
✅ View records: `python view_data.py`
✅ Check tokens generated and saved

---

## VOICE vs KEYBOARD

The system works BOTH ways:

✅ **VOICE** (if microphone available)
- Speak symptoms, age, name
- Natural conversation flow

✅ **KEYBOARD** (always available)
- Type responses
- No microphone needed
- Perfect for testing

The system automatically switches between them!

---

**Status:** ✅ Ready for Hackathon Demo  
**Database:** SQLite (local, no server needed)  
**Voice:** Optional (keyboard fallback)  
**Setup Time:** 30 seconds  

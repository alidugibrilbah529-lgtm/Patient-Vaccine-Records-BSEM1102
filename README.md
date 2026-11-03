# Vaccination Tracker System 💉

A Python OOP-based **Vaccination Tracker** solving a real-world **Health** domain problem.
Built to meet **Digital Public Goods (DPG)** standards.

---

## 📌 Domain
**Health** — Patient Record / Vaccination Tracker

---

## 🧩 How It Aligns with DPG Standards

| DPG Principle         | Implementation                                                                 |
|-----------------------|--------------------------------------------------------------------------------|
| **Open-source**       | All source code is publicly available on GitHub under an open license          |
| **Privacy-respecting**| Patients are stored with anonymous IDs only — no real names or sensitive data  |
| **Inclusive & Accessible** | Plain-text output readable by any terminal; no proprietary software needed |
| **Modular & Reusable**| Classes (`Vaccine`, `Patient`) and helper functions are fully independent       |

---

## 🗂️ OOP Concepts Covered

### Classes & Objects
- **`Vaccine`** — represents a vaccine product with `name`, `manufacturer`, `year`
- **`Patient`** — represents a patient with an anonymous `patient_id` and `age`

### Methods
| Type | Method | Class |
|------|--------|-------|
| Instance | `display_info()` | `Vaccine`, `Patient` |
| Instance | `update_record()` | `Vaccine`, `Patient` |
| Instance | `receive_vaccine()` | `Patient` |
| **Class** (`@classmethod`) | `add_vaccine()` | `Vaccine` |
| **Class** (`@classmethod`) | `display_all_vaccines()` | `Vaccine` |
| **Class** (`@classmethod`) | `enroll_patient()` | `Patient` |
| **Class** (`@classmethod`) | `display_all_patients()` | `Patient` |
| Static | `vaccine_count()` | `Vaccine` |

### Data Structure — Dictionary
- `Vaccine.total_vaccines` — catalogue of all vaccines (`{name: Vaccine}`)
- `Patient.registry` — registry of all patients (`{patient_id: Patient}`)
- Helper functions `add_record()` and `display_records()` work on any dictionary

### Bonus — Tuple
An immutable `dose_schedule` tuple is demonstrated in `main()`.

---

## ▶️ Sample Input / Output

```
==================================================
   VACCINATION TRACKER SYSTEM
   Domain: Health | DPG Compliant
==================================================

>>> Adding vaccines to catalogue...
[ADD] Vaccine 'COVID-19 mRNA' added to catalogue.
[ADD] Vaccine 'Polio OPV' added to catalogue.
[ADD] Vaccine 'Measles MMR' added to catalogue.

===== VACCINE CATALOGUE =====

  [1] COVID-19 mRNA
  Vaccine : COVID-19 mRNA
  Made by : BioNTech
  Year    : 2020

  [2] Polio OPV
  Vaccine : Polio OPV
  Made by : WHO-Supply
  Year    : 1961

  [3] Measles MMR
  Vaccine : Measles MMR
  Made by : Merck
  Year    : 1971
==============================

>>> Updating Polio OPV record...
[UPDATE] Vaccine 'Polio OPV' record updated.

>>> Enrolling patients...
[ENROLL] Patient 'P-001' enrolled.
[ENROLL] Patient 'P-002' enrolled.
[ENROLL] Patient 'P-003' enrolled.

>>> Administering vaccines...
[VACCINATE] Patient P-001 received 'COVID-19 mRNA'.
[VACCINATE] Patient P-001 received 'Measles MMR'.
[VACCINATE] Patient P-002 received 'Polio OPV'.
[VACCINATE] Patient P-003 received 'COVID-19 mRNA'.
[VACCINATE] Patient P-003 received 'Polio OPV'.
[VACCINATE] Patient P-003 received 'Measles MMR'.

===== PATIENT REGISTRY =====

  Patient ID : P-001
  Age        : 34
  Vaccines received (2):
    - COVID-19 mRNA (BioNTech, 2020)
    - Measles MMR (Merck, 1971)

  Patient ID : P-002
  Age        : 12
  Vaccines received (1):
    - Polio OPV (UNICEF Supply Division, 2022)

  Patient ID : P-003
  Age        : 67
  Vaccines received (3):
    - COVID-19 mRNA (BioNTech, 2020)
    - Polio OPV (UNICEF Supply Division, 2022)
    - Measles MMR (Merck, 1971)
==============================

[SUMMARY] Total vaccines in catalogue : 3
[SUMMARY] Total patients enrolled     : 3

>>> (BONUS) Tuple – immutable dose schedule:
  Dose 1: Day 0
  Dose 2: Day 21
  Dose 3: Day 180

[DONE] Vaccination Tracker completed successfully.
```

---

## 🚀 How to Run

```bash
python Main.py
```

> Requirements: Python 3.7+ (no external libraries needed)

---

## 📁 Files
| File | Description |
|------|-------------|
| `Main.py` | Main program — all classes, methods, and demo |
| `README.md` | This documentation file |

---

## 👤 Author
Osman Kaimapo Momoh  
Assignment — Python OOP | Health Domain | DPG Compliant

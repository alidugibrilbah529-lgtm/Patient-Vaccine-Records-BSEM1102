
# CLASS 1 – Vaccine
# Represents a single vaccine product (no personal data stored → privacy-safe)
# ──────────────────────────────────────────────────────────────────────────────
class Vaccine:
    """Stores details about a vaccine product."""

    # Class-level attribute shared across ALL Vaccine instances
    total_vaccines = {}   # Task 2: dictionary data structure  {name: Vaccine}

    def __init__(self, name: str, manufacturer: str, year: int):
        """Instance method – initialise a Vaccine object."""
        self.name         = name          # e.g. "COVID-19 mRNA"
        self.manufacturer = manufacturer  # e.g. "BioNTech"
        self.year         = year          # e.g. 2020

    # ── Instance method ──────────────────────────────────────────────────────
    def display_info(self):
        """Print vaccine details."""
        print(f"  Vaccine : {self.name}")
        print(f"  Made by : {self.manufacturer}")
        print(f"  Year    : {self.year}")

    # ── Instance method ──────────────────────────────────────────────────────
    def update_record(self, manufacturer: str = None, year: int = None):
        """Update manufacturer and/or year."""
        if manufacturer:
            self.manufacturer = manufacturer
        if year:
            self.year = year
        print(f"[UPDATE] Vaccine '{self.name}' record updated.")

    # ── Class method (Task 3) ────────────────────────────────────────────────
    @classmethod
    def add_vaccine(cls, name: str, manufacturer: str, year: int):
        """Add a new Vaccine to the shared catalogue (class-level dictionary)."""
        vaccine = cls(name, manufacturer, year)
        cls.total_vaccines[name] = vaccine
        print(f"[ADD] Vaccine '{name}' added to catalogue.")
        return vaccine

    # ── Class method ─────────────────────────────────────────────────────────
    @classmethod
    def display_all_vaccines(cls):
        """Display every vaccine in the catalogue."""
        print("\n===== VACCINE CATALOGUE =====")
        if not cls.total_vaccines:
            print("  (no vaccines registered)")
        else:
            for idx, (key, v) in enumerate(cls.total_vaccines.items(), start=1):
                print(f"\n  [{idx}] {key}")
                v.display_info()
        print("=" * 30)

    # ── Static helper ─────────────────────────────────────────────────────────
    @staticmethod
    def vaccine_count():
        """Return total number of vaccines in the catalogue."""
        return len(Vaccine.total_vaccines)


# ──────────────────────────────────────────────────────────────────────────────
# CLASS 2 – Patient
# Represents a patient using an anonymous ID (privacy-respecting)
# ──────────────────────────────────────────────────────────────────────────────
class Patient:
    """Tracks vaccination records for a patient."""

    # Class-level dictionary: patient_id -> Patient  (Task 2 data structure)
    registry = {}

    def __init__(self, patient_id: str, age: int):
        """Instance method – initialise a Patient object."""
        self.patient_id       = patient_id   # Anonymous ID (no real name stored)
        self.age              = age
        self.vaccinations     = []           # list of Vaccine objects received

    # ── Instance method ──────────────────────────────────────────────────────
    def receive_vaccine(self, vaccine: Vaccine):
        """Record that this patient received a vaccine."""
        self.vaccinations.append(vaccine)
        print(f"[VACCINATE] Patient {self.patient_id} received '{vaccine.name}'.")

    # ── Instance method ──────────────────────────────────────────────────────
    def display_info(self):
        """Display patient vaccination history."""
        print(f"\n  Patient ID : {self.patient_id}")
        print(f"  Age        : {self.age}")
        print(f"  Vaccines received ({len(self.vaccinations)}):")
        if not self.vaccinations:
            print("    None yet.")
        else:
            for v in self.vaccinations:
                print(f"    - {v.name} ({v.manufacturer}, {v.year})")

    # ── Instance method ──────────────────────────────────────────────────────
    def update_record(self, age: int):
        """Update patient age."""
        self.age = age
        print(f"[UPDATE] Patient {self.patient_id} age updated to {age}.")

    # ── Class method (Task 3) ────────────────────────────────────────────────
    @classmethod
    def enroll_patient(cls, patient_id: str, age: int):
        """Enroll a new patient and add them to the registry."""
        patient = cls(patient_id, age)
        cls.registry[patient_id] = patient
        print(f"[ENROLL] Patient '{patient_id}' enrolled.")
        return patient

    # ── Class method ─────────────────────────────────────────────────────────
    @classmethod
    def display_all_patients(cls):
        """Display all enrolled patients and their vaccination status."""
        print("\n===== PATIENT REGISTRY =====")
        if not cls.registry:
            print("  (no patients enrolled)")
        else:
            for patient in cls.registry.values():
                patient.display_info()
        print("=" * 30)


# ──────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS  (Task 2 – simple functions to add/display records)
# ──────────────────────────────────────────────────────────────────────────────
def add_record(data_structure: dict, key: str, value):
    """Generic function to add a record to a dictionary."""
    data_structure[key] = value
    print(f"[RECORD] '{key}' added to data store.")


def display_records(data_structure: dict, label: str = "Records"):
    """Generic function to display all records in a dictionary."""
    print(f"\n----- {label} -----")
    for key, val in data_structure.items():
        print(f"  {key}: {val}")
    print("-" * (len(label) + 12))


# ──────────────────────────────────────────────────────────────────────────────
# MAIN PROGRAM  –  demonstrates object creation and interaction
# ──────────────────────────────────────────────────────────────────────────────
def main():
    print("=" * 50)
    print("   VACCINATION TRACKER SYSTEM")
    print("   Domain: Health | DPG Compliant")
    print("=" * 50)

    # ── Task 1 & 2: Create Vaccine objects via class method (stored in dict) ──
    print("\n>>> Adding vaccines to catalogue...")
    v1 = Vaccine.add_vaccine("COVID-19 mRNA", "BioNTech",   2020)
    v2 = Vaccine.add_vaccine("Polio OPV",     "WHO-Supply",  1961)
    v3 = Vaccine.add_vaccine("Measles MMR",   "Merck",       1971)

    # ── Task 3: Class method – display all vaccines ───────────────────────────
    Vaccine.display_all_vaccines()

    # ── Task 1: Update a vaccine record (instance method) ────────────────────
    print("\n>>> Updating Polio OPV record...")
    v2.update_record(manufacturer="UNICEF Supply Division", year=2022)

    # ── Task 1 & 2: Enroll patients (stored in dictionary registry) ──────────
    print("\n>>> Enrolling patients...")
    p1 = Patient.enroll_patient("P-001", 34)
    p2 = Patient.enroll_patient("P-002", 12)
    p3 = Patient.enroll_patient("P-003", 67)

    # ── Task 1: Object interaction – patient receives vaccine ─────────────────
    print("\n>>> Administering vaccines...")
    p1.receive_vaccine(v1)
    p1.receive_vaccine(v3)
    p2.receive_vaccine(v2)
    p3.receive_vaccine(v1)
    p3.receive_vaccine(v2)
    p3.receive_vaccine(v3)

    # ── Task 3: Class method – display all patients ───────────────────────────
    Patient.display_all_patients()

    # ── Task 1: Update a patient record (instance method) ────────────────────
    print("\n>>> Updating patient P-002 age...")
    p2.update_record(age=13)

    # ── Task 2: Demonstrate generic add/display helper functions ──────────────
    print("\n>>> Using generic add_record / display_records helpers...")
    notes = {}
    add_record(notes, "P-001", "Allergic to latex – handle with care")
    add_record(notes, "P-003", "Requires follow-up in 6 months")
    display_records(notes, "Clinical Notes")

    # ── Summary stats ─────────────────────────────────────────────────────────
    print(f"\n[SUMMARY] Total vaccines in catalogue : {Vaccine.vaccine_count()}")
    print(f"[SUMMARY] Total patients enrolled     : {len(Patient.registry)}")

    # ── BONUS – Tuple usage (optional extra marks) ────────────────────────────
    print("\n>>> (BONUS) Tuple – immutable dose schedule:")
    dose_schedule = ("Dose 1: Day 0", "Dose 2: Day 21", "Dose 3: Day 180")
    for dose in dose_schedule:
        print(f"  {dose}")

    print("\n[DONE] Vaccination Tracker completed successfully.")


if __name__ == "__main__":
    main()
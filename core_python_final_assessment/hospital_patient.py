class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease


def search_disease(patients, disease):
    result = [patient.name for patient in patients if patient.disease.lower() == disease.lower()]
    return result

patients = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu")
]

disease = "Flu"
matching_patients = search_disease(patients, disease)
print(f"Patients with {disease}: {matching_patients}")

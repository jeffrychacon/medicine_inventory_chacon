from patient import Patient
from medicine import Medicine

my_medicine = Medicine("Vymada","Compuesto","Merk", 28,1,5000,"Paciente Feliz")
my_medicine2 = Medicine("Concor","Compuesto","Merk", 28,1,5000,"Paciente Feliz")

my_patient = Patient("Simon Chacon", 301110468,120,60)
my_patient.medicine.append(my_medicine)
my_patient.medicine.append(my_medicine2)

def status(my_patient):
    print(f" Nombre: {my_patient.name}")
    print(f"**** Tratamiento ****")
    for meds in my_patient.medicine:
        print(f" {meds.name} \t {meds.brand}")

status(my_patient)

from sqlalchemy.orm import Session
from sqlalchemy_project.db_management import prideti_darbuotoja, gauti_visus_darbuotojus, atnaujinti_darbuotoja, istrinti_darbuotoja, SessionLocal

def spausdinti_meniu():
    print("1. Pridėti naują darbuotoją")
    print("2. Peržiūrėti visus darbuotojus")
    print("3. Atnaujinti darbuotoją")
    print("4. Ištrinti darbuotoją")
    print("5. Išeiti")

def prideti_darbuotoja_interaktyviai(db: Session):
    vardas = input("Įveskite vardą: ")
    pavarde = input("Įveskite pavardę: ")
    gimimo_data = input("Įveskite gimimo datą (YYYY-MM-DD): ")
    pareigos = input("Įveskite pareigas: ")
    atlyginimas = float(input("Įveskite atlyginimą: "))
    naujas_darbuotojas = prideti_darbuotoja(db, vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    print(f"Pridėtas darbuotojas: {naujas_darbuotojas.vardas} {naujas_darbuotojas.pavarde}")

def perziureti_visus_darbuotojus(db: Session):
    visi_darbuotojai = gauti_visus_darbuotojus(db)
    if visi_darbuotojai:
        for darbuotojas in visi_darbuotojai:
            print(f"{darbuotojas.id}. {darbuotojas.vardas} {darbuotojas.pavarde} - {darbuotojas.pareigos} - {darbuotojas.atlyginimas} EUR - Dirba nuo {darbuotojas.nuo_kada_dirba}")
    else:
        print("Nėra darbuotojų duomenų.")

def atnaujinti_darbuotoja_interaktyviai(db: Session):
    darbuotojas_id = int(input("Įveskite darbuotojo ID, kurį norite atnaujinti: "))
    vardas = input("Įveskite naują vardą: ")
    pavarde = input("Įveskite naują pavardę: ")
    gimimo_data = input("Įveskite naują gimimo datą (YYYY-MM-DD): ")
    pareigos = input("Įveskite naujas pareigas: ")
    atlyginimas = float(input("Įveskite naują atlyginimą: "))
    atnaujintas_darbuotojas = atnaujinti_darbuotoja(db, darbuotojas_id, vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    if atnaujintas_darbuotojas:
        print(f"Atnaujintas darbuotojas: {atnaujintas_darbuotojas.vardas} {atnaujintas_darbuotojas.pavarde}")
    else:
        print("Darbuotojas nerastas")

def istrinti_darbuotoja_interaktyviai(db: Session):
    darbuotojas_id = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
    istrintas_darbuotojas = istrinti_darbuotoja(db, darbuotojas_id)
    if istrintas_darbuotojas:
        print(f"Ištrintas darbuotojas: {istrintas_darbuotojas.vardas} {istrintas_darbuotojas.pavarde}")
    else:
        print("Darbuotojas nerastas")

def main():
    db = SessionLocal()
    try:
        while True:
            spausdinti_meniu()
            pasirinkimas = input("Pasirinkite veiksmą: ")
            if pasirinkimas == "1":
                prideti_darbuotoja_interaktyviai(db)
            elif pasirinkimas == "2":
                perziureti_visus_darbuotojus(db)
            elif pasirinkimas == "3":
                atnaujinti_darbuotoja_interaktyviai(db)
            elif pasirinkimas == "4":
                istrinti_darbuotoja_interaktyviai(db)
            elif pasirinkimas == "5":
                print("Viskas!")
                break
            else:
                print("Neteisingas pasirinkimas, bandykite dar kartą.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
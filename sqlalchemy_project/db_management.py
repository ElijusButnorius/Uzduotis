from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .constants import DATABASE_URL
from .tables import Base, Darbuotojas

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Sukuriame visas lenteles
Base.metadata.create_all(bind=engine)

def prideti_darbuotoja(db, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    naujas_darbuotojas = Darbuotojas(
        vardas=vardas,
        pavarde=pavarde,
        gimimo_data=datetime.strptime(gimimo_data, '%Y-%m-%d').date(),
        pareigos=pareigos,
        atlyginimas=atlyginimas,
        nuo_kada_dirba=datetime.now().date()
    )
    db.add(naujas_darbuotojas)
    db.commit()
    db.refresh(naujas_darbuotojas)
    return naujas_darbuotojas

def gauti_visus_darbuotojus(db):
    return db.query(Darbuotojas).all()

def atnaujinti_darbuotoja(db, darbuotojas_id, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    darbuotojas = db.query(Darbuotojas).filter(Darbuotojas.id == darbuotojas_id).first()
    if darbuotojas:
        darbuotojas.vardas = vardas
        darbuotojas.pavarde = pavarde
        darbuotojas.gimimo_data = datetime.strptime(gimimo_data, '%Y-%m-%d').date()
        darbuotojas.pareigos = pareigos
        darbuotojas.atlyginimas = atlyginimas
        db.commit()
        db.refresh(darbuotojas)
    return darbuotojas

def istrinti_darbuotoja(db, darbuotojas_id):
    darbuotojas = db.query(Darbuotojas).filter(Darbuotojas.id == darbuotojas_id).first()
    if darbuotojas:
        db.delete(darbuotojas)
        db.commit()
    return darbuotojas
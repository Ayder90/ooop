
import main


class Dinamik_koaksil(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    nom_moshnost = db.Column(db.Integer, nullable = False)
    max_moshnost = db.Column(db.Integer, nullable = False)
    Soprot = db.Column(db.Integer, nullable = False)
    Diapozon_chastot = db.Column(db.Integer, nullable = False)
    Chyvstvit = db.Column(db.Integer, nullable = False)
    Ves_magnita = db.Column(db.Integer, nullable = False)
    Type_Razmer = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"

class Dinamik_komponent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    nom_moshnost = db.Column(db.Integer, nullable = False)
    max_moshnost = db.Column(db.Integer, nullable = False)
    Soprot = db.Column(db.Integer, nullable = False)
    Diapozon_chastot = db.Column(db.Integer, nullable = False)
    Chyvstvit = db.Column(db.Integer, nullable = False)
    Type_Razmer = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"

class Type_Dinamik_komponent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type_razmer = db.Column(db.Integer, primary_key = True)

class Type_Dinamik_koaksil(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type_razmer = db.Column(db.Integer, primary_key = True)

class Type_Dinamik_Krossover(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type_razmer = db.Column(db.Integer, primary_key = True)

class Type_Magnitofon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type = db.Column(db.Integer, primary_key = True)

class Type_Dinamik_Twitter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type_razmer = db.Column(db.Integer, primary_key = True)

class Type_SAB(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Integer, primary_key = True)

class Type_Ysilitel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type = db.Column(db.Integer, primary_key = True)

class Magnitofon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    Color_magnitofon = db.Column(db.String(50), nullable = False)
    Bluetooth = db.Column(db.Boolean(50), nullable = False)
    Aux = db.Column(db.Boolean(50), nullable = False)
    USB = db.Column(db.Boolean(50), nullable = False)
    Max_moshnost_kanal = db.Column(db.Integer, nullable = False)
    Razmer = db.Column(db.Integer, nullable = False)
    Radio = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"

class Oval(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    nom_moshnost = db.Column(db.Integer, nullable = False)
    max_moshnost = db.Column(db.Integer, nullable = False)
    Soprot = db.Column(db.Integer, nullable = False)
    Diapozon_chastot = db.Column(db.Integer, nullable = False)
    Chyvstvit = db.Column(db.Integer, nullable = False)
    Type_Razmer = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"

class Ysiliteli(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    Oblast_primeneni_dlya_saba = db.Column(db.Boolean, nullable = False)
    Oblast_primeneni_shirokopolosna = db.Column(db.Boolean, nullable = False)
    Class = db.Column(db.String(50), nullable = False)
    Type_kanal = db.Column(db.Integer, primary_key = True)
    nom_moshnost = db.Column(db.Integer, nullable = False)
    max_moshnost = db.Column(db.Integer, nullable = False)
    min_soprot = db.Column(db.Integer, nullable = False)
    Diapozon_chastot = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    Otnoshenie_signal = db.Column(db.Integer, nullable = False)
    Demping_factor = db.Column(db.Integer, nullable = False)
    Distancion_regulator = db.Column(db.Boolean(50), nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"

class Sabik(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    Soprot_impedans = db.Column(db.Integer, nullable = False)
    Chyvstvit = db.Column(db.Integer, nullable = False)
    Diapozon_chastot = db.Column(db.Integer, nullable = False)
    nom_moshnost = db.Column(db.Integer, nullable = False)
    max_moshnost = db.Column(db.Integer, nullable = False)
    Rezonansna_chastota = db.Column(db.Integer, nullable = False)
    Elictrichesk_dobrotnost = db.Column(db.Integer, nullable = False)
    Mexanic_dobrotnost = db.Column(db.Integer, nullable = False)
    Full_dobrotnost = db.Column(db.Integer, nullable = False)
    Ekvivalent_OBom = db.Column(db.Integer, nullable = False)
    Massa_podvign_system = db.Column(db.Integer, nullable = False)
    Soprot_DC = db.Column(db.Integer, nullable = False)
    Effect_ploshad_diffysora = db.Column(db.Integer, nullable = False)
    Gibkost_podvign_system = db.Column(db.Integer, nullable = False)
    power_fact = db.Column(db.String(50), nullable = False)
    Mehanic_soprot = db.Column(db.Integer, nullable = False)
    Mat_difys = db.Column(db.String(50), nullable = False)
    Mat_podves = db.Column(db.String(50), nullable = False)
    Mat_zvyk_katyshki = db.Column(db.String(50), nullable = False)
    Mat_magnita = db.Column(db.String(50), nullable = False)
    Type_korsin = db.Column(db.String(50), nullable = False)
    Type_sab = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"

class Twitter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    nom_moshnost = db.Column(db.Integer, nullable = False)
    max_moshnost = db.Column(db.Integer, nullable = False)
    Soprot = db.Column(db.Integer, nullable = False)
    Diapozon_chastot = db.Column(db.Integer, nullable = False)
    Chyvstvit = db.Column(db.Integer, nullable = False)
    Type_Razmer = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"


class Krossover(db.Model):
    id = db.Column(db.Integer, primary_key = True)    
    Proizvod = db.Column(db.String(50), nullable = False)
    Model = db.Column(db.String(50), nullable = False)
    Nasnachenitie = db.Column(db.String(50), nullable = False)
    Bluetooth = db.Column(db.Boolean, nullable = False)
    Ves = db.Column(db.Integer, nullable = False)
    Kolvo_polos = db.Column(db.Integer, nullable = False)
    moshonst = db.Column(db.Integer, nullable = False)
    Soprot = db.Column(db.Integer, nullable = False)
    Chastota_razdela = db.Column(db.Integer, nullable = False)
    SCH = db.Column(db.Integer, nullable = False)
    VCH = db.Column(db.Integer, nullable = False)
    Krytizna_sreza = db.Column(db.Integer, nullable = False)
    Akysticheskie_terminala = db.Column(db.Integer, nullable = False)
    Type_Razmer = db.Column(db.Integer, nullable = False)
    Price = db.Column(db.Integer, nullable = False)
    # Image = image_attachment("image_tovar")
    # __tablename__ = "tovar"


class Zakaz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nomer_zakaza = db.Column(db.Integer, nullable = False)
    sost_zakaza = db.Column(db.String(70), nullable = True)
    Tovar_id = db.Column(db.String(100), nullable = False)
    data = db.Column(db.DateTime, default = datetime.utcnow)
    data_prib = db.Column(db.DateTime, default = datetime.utcnow)
    Users_id = db.Column(db.Integer, nullable = False)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Name_user = db.Column(db.String(50), nullable = False)
    Surname = db.Column(db.String(50), nullable = False)
    Otchestvo = db.Column(db.String(50), nullable = True)
    Email = db.Column(db.String(50), nullable = False)
    Nomer = db.Column(db.Integer, nullable = False)
    Login = db.Column(db.String(50), nullable = True)
    Password = db.Column(db.String(50), nullable = True)
    # Photo = db.Column(db.Image, nullable = False)
    Address = db.Column(db.String(50), nullable = True)

def __repr__(self):
        return "<Zakaz %r>" %self.id   
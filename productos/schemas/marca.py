from pydantic import BaseModel

# Esquema base para atributos comunes
class MarcaBase(BaseModel):
    nombre: str

# Esquema para creación (entrada de datos)
class MarcaCreate(MarcaBase):
    pass

# Esquema para respuesta con ID
class MarcaRead(MarcaBase):
    id_marca: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

# Esquema base para atributos comunes
class CategoriaBase(BaseModel):
    nombre: str

# Esquema para creación (entrada de datos)
class CategoriaCreate(CategoriaBase):
    pass

# Esquema para respuesta con ID
class CategoriaRead(CategoriaBase):
    id_categoria: int

    class Config:
        orm_mode = True

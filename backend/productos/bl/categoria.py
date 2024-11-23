from repository.categoria import (
    obtener_categorias,
    obtener_categoria_por_id,
    crear_categoria,
    actualizar_categoria,
    eliminar_categoria
)

def listar_categorias():
    return obtener_categorias()

def obtener_categoria(id_categoria: int):
    categoria = obtener_categoria_por_id(id_categoria)
    if not categoria:
        raise ValueError("La categoría no existe.")
    return categoria

def agregar_categoria(categoria_data):
    return crear_categoria(categoria_data)

def modificar_categoria(id_categoria: int, categoria_data):
    if not obtener_categoria_por_id(id_categoria):
        raise ValueError("La categoría no existe.")
    actualizar_categoria(id_categoria, categoria_data)

def borrar_categoria(id_categoria: int):
    if not obtener_categoria_por_id(id_categoria):
        raise ValueError("La categoría no existe.")
    eliminar_categoria(id_categoria)

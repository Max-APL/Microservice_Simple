import { categoriaApi} from "../../api/productos/categoriaApi";

export class CategoriaService {
    async listarCategorias() {
        try {
            const categorias = await categoriaApi.listarCategorias();
            return categorias;
        } catch (error) {
            throw new Error('Error al obtener la lista de categorías');
        }
    }

    async obtenerCategoria(idCategoria) {
        try {
            const categoria = await categoriaApi.obtenerCategoria(idCategoria);
            return categoria;
        } catch (error) {
            throw new Error(`Error al obtener la categoría con ID ${idCategoria}`);
        }
    }

    async agregarCategoria(categoria) {
        try {
            const nuevaCategoria = await categoriaApi.agregarCategoria(categoria);
            return nuevaCategoria;
        } catch (error) {
            throw new Error('Error al agregar una nueva categoría');
        }
    }

    async modificarCategoria(idCategoria, categoria) {
        try {
            const categoriaActualizada = await categoriaApi.modificarCategoria(
                idCategoria,
                categoria
            );
            return categoriaActualizada;
        } catch (error) {
            throw new Error(`Error al modificar la categoría con ID ${idCategoria}`);
        }
    }

    async borrarCategoria(idCategoria) {
        try {
            const resultado = await categoriaApi.borrarCategoria(idCategoria);
            return resultado;
        } catch (error) {
            throw new Error(`Error al borrar la categoría con ID ${idCategoria}`);
        }
    }
}

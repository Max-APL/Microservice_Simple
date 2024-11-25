import { marcaApi} from "../../api/productos/marcaApi";

export class MarcaService {
    async listarMarcas() {
        try {
            const marcas = await marcaApi.listarMarcas();
            return marcas;
        } catch (error) {
            throw new Error('Error al obtener la lista de marcas');
        }
    }

    async obtenerMarca(idMarca) {
        try {
            const marca = await marcaApi.obtenerMarca(idMarca);
            return marca;
        } catch (error) {
            throw new Error(`Error al obtener la marca con ID ${idMarca}`);
        }
    }

    async agregarMarca(marca) {
        try {
            const nuevaMarca = await marcaApi.agregarMarca(marca);
            return nuevaMarca;
        } catch (error) {
            throw new Error('Error al agregar una nueva marca');
        }
    }

    async modificarMarca(idMarca, marca) {
        try {
            const marcaActualizada = await marcaApi.modificarMarca(idMarca, marca);
            return marcaActualizada;
        } catch (error) {
            throw new Error(`Error al modificar la marca con ID ${idMarca}`);
        }
    }

    async borrarMarca(idMarca) {
        try {
            const resultado = await marcaApi.borrarMarca(idMarca);
            return resultado;
        } catch (error) {
            throw new Error(`Error al borrar la marca con ID ${idMarca}`);
        }
    }
}

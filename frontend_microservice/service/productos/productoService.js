import {productoApi} from "../../api/productos/productoApi";

export class ProductoService {
    async listarProductos() {
        try {
            const productos = await productoApi.listarProductos();
            return productos;
        } catch (error) {
            throw new Error('Error al obtener la lista de productos');
        }
    }

    async obtenerProducto(idProducto) {
        try {
            const producto = await productoApi.obtenerProducto(idProducto);
            return producto;
        } catch (error) {
            throw new Error(`Error al obtener el producto con ID ${idProducto}`);
        }
    }

    async agregarProducto(producto) {
        try {
            const nuevoProducto = await productoApi.agregarProducto(producto);
            return nuevoProducto;
        } catch (error) {
            throw new Error('Error al agregar un nuevo producto');
        }
    }

    async modificarProducto(idProducto, producto) {
        try {
            const productoActualizado = await productoApi.modificarProducto(
                idProducto,
                producto
            );
            return productoActualizado;
        } catch (error) {
            throw new Error(`Error al modificar el producto con ID ${idProducto}`);
        }
    }

    async borrarProducto(idProducto) {
        try {
            const resultado = await productoApi.borrarProducto(idProducto);
            return resultado;
        } catch (error) {
            throw new Error(`Error al borrar el producto con ID ${idProducto}`);
        }
    }
}

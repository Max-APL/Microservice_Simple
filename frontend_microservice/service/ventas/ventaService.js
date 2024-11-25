import { ventaApi} from "../../api/ventas/ventaApi";

export class VentaService {
    async listarVentas() {
        try {
            const ventas = await ventaApi.listarVentas();
            return ventas;
        } catch (error) {
            throw new Error('Error al obtener la lista de ventas');
        }
    }

    async obtenerVenta(idVenta) {
        try {
            const venta = await ventaApi.obtenerVenta(idVenta);
            return venta;
        } catch (error) {
            throw new Error(`Error al obtener la venta con ID ${idVenta}`);
        }
    }

    async agregarVenta(venta) {
        try {
            const nuevaVenta = await ventaApi.agregarVenta(venta);
            return nuevaVenta;
        } catch (error) {
            throw new Error('Error al agregar una nueva venta');
        }
    }

    async modificarVenta(idVenta, venta) {
        try {
            const ventaActualizada = await ventaApi.modificarVenta(idVenta, venta);
            return ventaActualizada;
        } catch (error) {
            throw new Error(`Error al modificar la venta con ID ${idVenta}`);
        }
    }

    async borrarVenta(idVenta) {
        try {
            const resultado = await ventaApi.borrarVenta(idVenta);
            return resultado;
        } catch (error) {
            throw new Error(`Error al borrar la venta con ID ${idVenta}`);
        }
    }
}

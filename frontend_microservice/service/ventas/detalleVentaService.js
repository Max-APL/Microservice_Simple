import { detalleVentaApi} from "../../api/ventas/detalleVentaApi";

export class DetalleVentaService {
    async listarDetallesVenta() {
        try {
            const detalles = await detalleVentaApi.listarDetallesVenta();
            return detalles;
        } catch (error) {
            throw new Error('Error al obtener la lista de detalles de venta');
        }
    }

    async obtenerDetalleVenta(id) {
        try {
            const detalle = await detalleVentaApi.obtenerDetalleVenta(id);
            return detalle;
        } catch (error) {
            throw new Error(`Error al obtener el detalle de venta con ID ${id}`);
        }
    }

    async agregarDetalleVenta(detalle) {
        try {
            const nuevoDetalle = await detalleVentaApi.agregarDetalleVenta(detalle);
            return nuevoDetalle;
        } catch (error) {
            throw new Error('Error al agregar un nuevo detalle de venta');
        }
    }

    async eliminarDetalleVenta(idDetalle) {
        try {
            const resultado = await detalleVentaApi.eliminarDetalleVenta(idDetalle);
            return resultado;
        } catch (error) {
            throw new Error(`Error al eliminar el detalle de venta con ID ${idDetalle}`);
        }
    }

    async actualizarDetalleVenta(idDetalle, detalle) {
        try {
            const detalleActualizado = await detalleVentaApi.actualizarDetalleVenta(
                idDetalle,
                detalle
            );
            return detalleActualizado;
        } catch (error) {
            throw new Error(
                `Error al actualizar el detalle de venta con ID ${idDetalle}`
            );
        }
    }

    async listarDetallesPorVenta(idVenta) {
        try {
            const detalles = await detalleVentaApi.listarDetallesPorVenta(idVenta);
            return detalles;
        } catch (error) {
            throw new Error(
                `Error al listar los detalles de venta para la venta con ID ${idVenta}`
            );
        }
    }
}

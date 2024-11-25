import axios from 'axios';

const BASE_URL = 'http://localhost:8002/ventas/detalle';

export const detalleVentaApi = {
    listarDetallesVenta: async () => {
        try {
            const response = await axios.get(`${BASE_URL}`);
            return response.data;
        } catch (error) {
            console.error('Error al listar los detalles de venta:', error);
            throw error;
        }
    },

    obtenerDetalleVenta: async (id) => {
        try {
            const response = await axios.get(`${BASE_URL}/${id}`);
            return response.data;
        } catch (error) {
            console.error('Error al obtener el detalle de venta:', error);
            throw error;
        }
    },

    agregarDetalleVenta: async (detalle) => {
        try {
            const response = await axios.post(`${BASE_URL}`, detalle);
            return response.data;
        } catch (error) {
            console.error('Error al agregar el detalle de venta:', error);
            throw error;
        }
    },

    eliminarDetalleVenta: async (idDetalle) => {
        try {
            const response = await axios.delete(`${BASE_URL}/${idDetalle}`);
            return response.data;
        } catch (error) {
            console.error('Error al eliminar el detalle de venta:', error);
            throw error;
        }
    },

    actualizarDetalleVenta: async (idDetalle, detalle) => {
        try {
            const response = await axios.put(`${BASE_URL}/${idDetalle}`, detalle);
            return response.data;
        } catch (error) {
            console.error('Error al actualizar el detalle de venta:', error);
            throw error;
        }
    },

    listarDetallesPorVenta: async (idVenta) => {
        try {
            const response = await axios.get(`${BASE_URL}/venta/${idVenta}`);
            return response.data;
        } catch (error) {
            console.error('Error al listar detalles por venta:', error);
            throw error;
        }
    },
};

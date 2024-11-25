import axios from 'axios';

const BASE_URL = 'http://localhost:8002/ventas/venta';

export const ventaApi = {
    listarVentas: async () => {
        try {
            const response = await axios.get(`${BASE_URL}`);
            return response.data;
        } catch (error) {
            console.error('Error al listar ventas:', error);
            throw error;
        }
    },

    obtenerVenta: async (idVenta) => {
        try {
            const response = await axios.get(`${BASE_URL}/${idVenta}`);
            return response.data;
        } catch (error) {
            console.error('Error al obtener la venta:', error);
            throw error;
        }
    },

    agregarVenta: async (venta) => {
        try {
            const response = await axios.post(`${BASE_URL}`, venta);
            return response.data;
        } catch (error) {
            console.error('Error al agregar la venta:', error);
            throw error;
        }
    },

    modificarVenta: async (idVenta, venta) => {
        try {
            const response = await axios.put(`${BASE_URL}/${idVenta}`, venta);
            return response.data;
        } catch (error) {
            console.error('Error al modificar la venta:', error);
            throw error;
        }
    },

    borrarVenta: async (idVenta) => {
        try {
            const response = await axios.delete(`${BASE_URL}/${idVenta}`);
            return response.data;
        } catch (error) {
            console.error('Error al borrar la venta:', error);
            throw error;
        }
    },
};

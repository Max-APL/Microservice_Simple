import axios from 'axios';

const BASE_URL = 'http://localhost:8001/gestion_productos/productos';

export const productoApi = {
    listarProductos: async () => {
        try {
            const response = await axios.get(`${BASE_URL}`);
            return response.data;
        } catch (error) {
            console.error('Error al listar productos:', error);
            throw error;
        }
    },

    obtenerProducto: async (idProducto) => {
        try {
            const response = await axios.get(`${BASE_URL}/${idProducto}`);
            return response.data;
        } catch (error) {
            console.error('Error al obtener producto:', error);
            throw error;
        }
    },

    agregarProducto: async (producto) => {
        try {
            const response = await axios.post(`${BASE_URL}`, producto);
            return response.data;
        } catch (error) {
            console.error('Error al agregar producto:', error);
            throw error;
        }
    },

    modificarProducto: async (idProducto, producto) => {
        try {
            const response = await axios.put(`${BASE_URL}/${idProducto}`, producto);
            return response.data;
        } catch (error) {
            console.error('Error al modificar producto:', error);
            throw error;
        }
    },

    borrarProducto: async (idProducto) => {
        try {
            const response = await axios.delete(`${BASE_URL}/${idProducto}`);
            return response.data;
        } catch (error) {
            console.error('Error al borrar producto:', error);
            throw error;
        }
    },
};

import axios from 'axios';

const BASE_URL = 'http://localhost:8001/gestion_productos/categorias';

export const categoriaApi = {
    listarCategorias: async () => {
        try {
            const response = await axios.get(`${BASE_URL}`);
            return response.data;
        } catch (error) {
            console.error('Error al listar categorías:', error);
            throw error;
        }
    },

    obtenerCategoria: async (idCategoria) => {
        try {
            const response = await axios.get(`${BASE_URL}/${idCategoria}`);
            return response.data;
        } catch (error) {
            console.error('Error al obtener la categoría:', error);
            throw error;
        }
    },

    agregarCategoria: async (categoria) => {
        try {
            const response = await axios.post(`${BASE_URL}`, categoria);
            return response.data;
        } catch (error) {
            console.error('Error al agregar la categoría:', error);
            throw error;
        }
    },

    modificarCategoria: async (idCategoria, categoria) => {
        try {
            const response = await axios.put(`${BASE_URL}/${idCategoria}`, categoria);
            return response.data;
        } catch (error) {
            console.error('Error al modificar la categoría:', error);
            throw error;
        }
    },

    borrarCategoria: async (idCategoria) => {
        try {
            const response = await axios.delete(`${BASE_URL}/${idCategoria}`);
            return response.data;
        } catch (error) {
            console.error('Error al borrar la categoría:', error);
            throw error;
        }
    },
};

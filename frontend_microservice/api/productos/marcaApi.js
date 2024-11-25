import axios from 'axios';

const BASE_URL = 'http://localhost:8001/gestion_productos/marcas';

export const marcaApi = {
    listarMarcas: async () => {
        try {
            const response = await axios.get(`${BASE_URL}`);
            return response.data;
        } catch (error) {
            console.error('Error al listar marcas:', error);
            throw error;
        }
    },

    obtenerMarca: async (idMarca) => {
        try {
            const response = await axios.get(`${BASE_URL}/${idMarca}`);
            return response.data;
        } catch (error) {
            console.error('Error al obtener la marca:', error);
            throw error;
        }
    },

    agregarMarca: async (marca) => {
        try {
            const response = await axios.post(`${BASE_URL}`, marca);
            return response.data;
        } catch (error) {
            console.error('Error al agregar la marca:', error);
            throw error;
        }
    },

    modificarMarca: async (idMarca, marca) => {
        try {
            const response = await axios.put(`${BASE_URL}/${idMarca}`, marca);
            return response.data;
        } catch (error) {
            console.error('Error al modificar la marca:', error);
            throw error;
        }
    },

    borrarMarca: async (idMarca) => {
        try {
            const response = await axios.delete(`${BASE_URL}/${idMarca}`);
            return response.data;
        } catch (error) {
            console.error('Error al borrar la marca:', error);
            throw error;
        }
    },
};

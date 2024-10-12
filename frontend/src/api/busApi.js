import axios from 'axios';

// Definir la URL base del API
// const API_URL = `${process.env.REACT_APP_API_URL}/buses`; // URL base para buses (puedes configurar REACT_APP_API_URL en el archivo .env)

const API_URL = "http://localhost:8000/api/buses/"


// Obtener la lista de todos los buses
export const fetchBuses = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data; // Devolvemos los datos recibidos de la API
  } catch (error) {
    console.error("Error fetching buses:", error);
    throw error;
  }
};

// Obtener un bus por su ID
export const fetchBusById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data; // Devolvemos los datos del bus específico
  } catch (error) {
    console.error(`Error fetching bus with id ${id}:`, error);
    throw error;
  }
};

// Crear un nuevo bus
export const createBus = async (busData) => {
  try {
    const response = await axios.post(API_URL, busData);
    return response.data; // Devolvemos los datos del bus recién creado
  } catch (error) {
    console.error("Error creating bus:", error);
    throw error;
  }
};

// Actualizar un bus existente
export const updateBus = async (id, busData) => {
  try {
    const response = await axios.put(`${API_URL}/${id}`, busData);
    return response.data; // Devolvemos los datos del bus actualizado
  } catch (error) {
    console.error(`Error updating bus with id ${id}:`, error);
    throw error;
  }
};

// Eliminar un bus
export const deleteBus = async (id) => {
  try {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data; // Devolvemos la respuesta de la API
  } catch (error) {
    console.error(`Error deleting bus with id ${id}:`, error);
    throw error;
  }
};

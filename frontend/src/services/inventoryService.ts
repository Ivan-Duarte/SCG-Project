import axios from "axios";
import { NewInventoryItem, InventoryItem } from "../types/inventoryTypes";

const BASE_URL = process.env.REACT_APP_API_URL;

if (!BASE_URL) {
  throw new Error("A URL base da API não está definida. Verifique o arquivo .env.");
}

const API_URL = `${BASE_URL}/items`;

// Função para obter os itens do inventário
export const getInventoryItems = async (): Promise<InventoryItem[]> => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar os itens do inventário:", error);
    throw error;
  }
};

// Função para criar um novo item no inventário
export const createInventoryItem = async (item: NewInventoryItem) => {
  try {
    const response = await axios.post(API_URL, item);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar um novo item no inventário:", error);
    throw error;
  }
};


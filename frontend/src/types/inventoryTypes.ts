export interface InventoryItem {
    id: number;
    name: string;
    description?: string;
    category: string;
    stock_quantity: number;
    location?: string;
    general_info?: string;
  }

export interface NewInventoryItem {
    name: string;
    description?: string;
    category: string;
    stock_quantity: number;
    location?: string;
    general_info?: string;
  }
  
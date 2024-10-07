import React, { useEffect, useState } from "react";
import { getInventoryItems } from "../../services/inventoryService";
import { InventoryItem } from "../../types/inventoryTypes";

const InventoryList: React.FC = () => {
  const [items, setItems] = useState<InventoryItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await getInventoryItems();
        setItems(response);
      } catch (error) {
        console.error("Erro ao buscar os itens do inventário:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchItems();
  }, []);

  if (loading) {
    return <p>Carregando itens...</p>;
  }

  return (
    <div>
      <h2>Itens Disponíveis no Estoque</h2>
      {items.length === 0 ? (
        <p>Nenhum item disponível no estoque.</p>
      ) : (
        <ul>
          {items.map((item) => (
            <li key={item.id}>
              <strong>ID:</strong> {item.id}
              <br />
              <strong>Nome:</strong> {item.name}
              <br />
              <strong>Descrição:</strong> {item.description || "Sem descrição"}
              <br />
              <strong>Quantidade em Estoque:</strong> {item.stock_quantity}
              <br />
              <strong>Categoria:</strong> {item.category}
              <br />
              <strong>Localização:</strong> {item.location || "Não especificado"}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default InventoryList;

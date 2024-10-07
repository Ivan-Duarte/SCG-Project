import React from 'react';
import { useNavigate } from "react-router-dom";
import ItensForm from '../../components/Form/ItensForm';


const InventoryPage: React.FC = () => {
  const navigate = useNavigate();
  return (
    <div>
      <h1>Cadastro de Itens no Inventário</h1>
      <ItensForm />
      <button onClick={() => navigate("/")}>Voltar</button>
    </div>
  );
};

export default InventoryPage;
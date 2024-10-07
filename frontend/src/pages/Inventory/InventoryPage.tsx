import React from 'react';
import ItensForm from '../../components/Form/ItensForm';

const InventoryPage: React.FC = () => {
  return (
    <div>
      <h1>Cadastro de Itens no Inventário</h1>
      <ItensForm />
    </div>
  );
};

export default InventoryPage;
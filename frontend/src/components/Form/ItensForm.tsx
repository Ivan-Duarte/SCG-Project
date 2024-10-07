import React, { useState } from 'react';
import {NewInventoryItem } from '../../types/inventoryTypes';
import { createInventoryItem } from '../../services/inventoryService';

const ItensForm: React.FC = () => {
  // Estado inicial do formulário
  const [formValues, setFormValues] = useState<NewInventoryItem>({
    name: '',
    description: '',
    category: '',
    stock_quantity: 0,
    location: '',
    general_info: '',
  });

  // Gerenciar mudanças nos inputs
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };

  // Enviar formulário
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      // Criar um novo item no inventário
      await createInventoryItem(formValues);
      alert('Item cadastrado com sucesso!');
      setFormValues({
        name: '',
        description: '',
        category: '',
        stock_quantity: 0,
        location: '',
        general_info: '',
      });
    } catch (error) {
      console.error('Erro ao cadastrar o item:', error);
      alert('Erro ao cadastrar o item. Tente novamente.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Nome do Item:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formValues.name}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label htmlFor="description">Descrição:</label>
        <textarea
          id="description"
          name="description"
          value={formValues.description}
          onChange={handleChange}
        />
      </div>

      <div>
        <label htmlFor="category">Categoria:</label>
        <select
          id="category"
          name="category"
          value={formValues.category}
          onChange={handleChange}
          required
        >
          <option value="">Selecione uma categoria</option>
          <option value="Papelaria">Papelaria</option>
          <option value="Eletronico">Eletronico</option>
          <option value="Material">Material</option>
          <option value="Peças">Peças</option>
        </select>
      </div>

      <div>
        <label htmlFor="stock_quantity">Quantidade em Estoque:</label>
        <input
          type="number"
          id="stock_quantity"
          name="stock_quantity"
          value={formValues.stock_quantity}
          onChange={handleChange}
          min="0"
        />
      </div>

      <div>
        <label htmlFor="location">Localização do Estoque:</label>
        <input
          type="text"
          id="location"
          name="location"
          value={formValues.location}
          onChange={handleChange}
        />
      </div>

      <div>
        <label htmlFor="general_info">Informações Gerais:</label>
        <textarea
          id="general_info"
          name="general_info"
          value={formValues.general_info}
          onChange={handleChange}
        />
      </div>

      <button type="submit">Cadastrar Item</button>
    </form>
  );
};

export default ItensForm;

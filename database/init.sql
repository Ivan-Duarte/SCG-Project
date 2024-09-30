-- Criar tabela de exemplo para itens de inventário
CREATE TABLE IF NOT EXISTS inventory_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserir dados iniciais
INSERT INTO inventory_items (name, description, price, quantity)
VALUES
('Item 1', 'Descrição do Item 1', 100.00, 50),
('Item 2', 'Descrição do Item 2', 200.00, 30);

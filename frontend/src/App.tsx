import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/Home/HomePage";
import InventoryPage from "./pages/Inventory/InventoryPage";

function App(){
  return (
    <Router>
      <Routes>
        {/* Rota Inicial (Home) */}
        <Route path="/" element={<HomePage />} />

        {/* Rota de Itens de Inventário*/}
        <Route path="/inventory" element={<InventoryPage />} />
      </Routes>
    </Router>
  );
}

export default App;
import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./HomePage.module.css";

const HomePage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className={styles.container}>
      <h1>Bem-vindo ao Sistema de Controle e Garantia (SCG)</h1>
      <button onClick={() => navigate("/inventory")}>Cadastrar Itens</button>
    </div>
  );
};

export default HomePage;
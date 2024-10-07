import React from "react";

interface MainLayoutProps {
  children: React.ReactNode;
}

const MainLayout: React.FC<MainLayoutProps> = ({ children }) => {
  return (
    <div>
      <header>
        <h1>Meu Projeto</h1>
      </header>
      <main>{children}</main>
      <footer>
        <p>Rodapé da Aplicação</p>
      </footer>
    </div>
  );
};

export default MainLayout;

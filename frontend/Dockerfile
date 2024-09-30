# DESENVOLVIMENTO!!!
FROM node:18-bullseye-slim AS development

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./

# Instalar as dependências
RUN npm install

# Copiar todo o código do projeto
COPY . .

# Expor a porta 3000 para desenvolvimento
EXPOSE 3000

# Comando para rodar o servidor de desenvolvimento do React
CMD ["npm", "start"]

# PRODUÇÃO!!!
# FROM node:18-bullseye-slim AS build

# # Diretório de trabalho
# WORKDIR /app

# # Copiar arquivos de dependências
# COPY package*.json ./

# # Instalar as dependências e construir o projeto
# RUN npm install && npm run build

# # Final Stage para Nginx
# FROM nginx:alpine

# # Copiar os arquivos de build para o diretório padrão do Nginx
# COPY --from=build /app/build /usr/share/nginx/html

# # Expor a porta 80 para servir os arquivos
# EXPOSE 80

# # Comando padrão do Nginx
# CMD ["nginx", "-g", "daemon off;"]

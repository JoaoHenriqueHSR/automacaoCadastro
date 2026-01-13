# 🤖 Automação de Cadastro de Produtos com Python

Este projeto demonstra uma **automação de cadastro de produtos em um sistema web**, utilizando **Python**, **PyAutoGUI** e **Pandas**.  
O objetivo é eliminar tarefas manuais repetitivas, lendo os dados de um arquivo CSV e inserindo automaticamente no sistema via navegador.

---

## 🚀 Funcionalidades

- Leitura de dados a partir de um arquivo `produtos.csv`
- Abertura automática do navegador
- Login automático no sistema
- Preenchimento e envio do formulário de cadastro de produtos
- Repetição do processo até o final da lista de produtos

---

## 🛠 Tecnologias Utilizadas

- **Python**
- **PyAutoGUI** – automação de teclado e mouse
- **Pandas** – leitura e manipulação de dados
- **Time** – controle de tempo entre ações

---

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

- Python 3 instalado
- Navegador Brave (ou ajuste o código para outro navegador)
- Arquivo `produtos.csv` no mesmo diretório do script

Instale as dependências com:

```bash
pip install pyautogui pandas

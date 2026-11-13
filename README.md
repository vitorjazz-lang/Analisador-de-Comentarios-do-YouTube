# 📊 Analisador de Comentários do YouTube

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Transformers](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

**Uma aplicação desktop em Python para extração automatizada de comentários e análise de sentimentos utilizando Inteligência Artificial.**

O **Analisador de Comentários do YouTube** é uma ferramenta desenvolvida para facilitar a coleta e a interpretação de opiniões em vídeos da plataforma. Combinando web scraping eficiente com Processamento de Linguagem Natural (PLN), o software classifica automaticamente o feedback do público e exporta os dados estruturados para planilhas Excel.

O projeto utiliza um modelo pré-treinado baseado na arquitetura **BERT multilíngue**, permitindo identificar polaridades (positivo, neutro e negativo) diretamente na máquina do usuário, sem depender de APIs pagas.

---

## 🎯 Objetivos do Projeto

* Automatizar a extração de comentários de vídeos do YouTube sem a necessidade de download da mídia.
* Aplicar modelos de Deep Learning (`Hugging Face Transformers`) para classificação de sentimentos em múltiplos idiomas.
* Oferecer uma interface gráfica simples e intuitiva (`Tkinter`) para usuários não técnicos.
* Estruturar e exportar os resultados prontos para análise de dados em formato `.xlsx`.

---

## 📸 Demonstração

> *(Dica: Tire um print da janela do seu programa rodando, salve como `preview.png` dentro da pasta `assets/` e a imagem aparecerá aqui automaticamente!)*

![Interface do Analisador de Comentários](assets/preview.png)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter** – Interface gráfica nativa (GUI)
* **yt-dlp** – Extração de metadados e comentários do YouTube
* **Hugging Face Transformers** – Pipeline de análise de sentimentos (`nlptown/bert-base-multilingual-uncased-sentiment`)
* **Pandas & OpenPyXL** – Manipulação de dados e exportação para Excel

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Passo a passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   cd NOME-DO-REPOSITORIO
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python seu_app.py
   ```
   *(Nota: Na primeira execução, o modelo BERT será baixado automaticamente, o que pode levar alguns minutos dependendo da sua conexão).*

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você tiver sugestões de melhorias (como suporte a multithreading na interface ou novos gráficos de análise), sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.

---

## 📄 Licença

Este projeto está licenciado sob a **licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

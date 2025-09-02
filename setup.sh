#!/bin/bash

# ============================================================
# 🚀 Script Universal de Setup para Projetos de Data Science
# ============================================================

echo "==========================================="
echo " Iniciando configuração do ambiente Python..."
echo "==========================================="

# 1. Atualizar pacotes do sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar dependências essenciais do sistema
sudo apt install -y python3 python3-venv python3-pip build-essential \
                    git wget curl unzip htop

# 3. Criar ambiente virtual no diretório do projeto
if [ ! -d "venv" ]; then
    echo ">> Criando ambiente virtual..."
    python3 -m venv venv
else
    echo ">> Ambiente virtual já existe, pulando..."
fi

# 4. Ativar ambiente virtual
source venv/bin/activate

# 5. Atualizar pip, wheel e setuptools
pip install --upgrade pip setuptools wheel

# 6. Instalar bibliotecas principais de Data Science
pip install numpy pandas matplotlib seaborn plotly \
            scikit-learn statsmodels scipy \
            jupyter jupyterlab ipykernel \
            requests beautifulsoup4 lxml \
            openpyxl xlrd pyarrow fastparquet \
            nbformat nbconvert

# 7. Instalar bibliotecas adicionais úteis
pip install tqdm joblib pyyaml sqlalchemy \
            mlflow shap lime \
            tensorflow torch torchvision torchaudio \
            xgboost lightgbm catboost

# 8. Instalar bibliotecas para APIs e scraping
pip install wbdata ipeadatapy yfinance

# 9. Registrar kernel do Jupyter Notebook
python -m ipykernel install --user --name=venv --display-name "Python (venv)"

echo "==========================================="
echo " ✅ Ambiente de Data Science configurado!"
echo " Ative com: source venv/bin/activate"
echo " Rode Jupyter com: jupyter notebook"
echo "==========================================="

#!/bin/bash

# Parte 1: Configurar Python

sudo apt update
sudo apt install python3-dev #(se o pip não estiver instalado, é só fazer: sudo apt install python3-pip python3-dev)



# Parte 2: Criar um ambiente virtual onde serpa instalado o jupyter

sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

# Depois disso, crie uma pasta onde estará o ambiente virtual e acesse-a. Isso pode ser feito com o botao direito do mouse ou com os comando:

mkdir ~/meu_projeto
cd ~/meu_projeto

# Crie um ambiente virtual com o comando

virtualenv meu_projeto_env #(meu_projeto_env é só um nome qualquer, poderia ser outro nome)

#---------------------------------------------------------------------------------------------------------
#Ative o ambiente virtual com

source meu_projeto_env/bin/activate
#---------------------------------------------------------------------------------------------------------

#Parte 3: Instalar e executar o jupyter:

pip install jupyter

#---------------------------------------------------------------------------------------------------------
jupyter notebook
#---------------------------------------------------------------------------------------------------------


#Obs.: os comandos que estão destacados,

# source meu_projeto_env/bin/activate
# jupyter notebook

# devem ser executados toda vez que vou usar o jupyter notebook; já os outros comandos devem ser executados apenas na hora
# de instalar.

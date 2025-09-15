# Base da imagem: Python 3
FROM python:3

# Metadados da imagem
LABEL maintainer="Garagem de Carros <dev@garagem.com>"
LABEL description="Imagem Docker para a Garagem de Carros - API de revenda de veículos"

# Diretório de trabalho (a garagem onde os carros ficam)
WORKDIR /garagem

# Copia dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código (leva os carros para dentro da garagem)
COPY . .

# Expõe a porta do showroom
EXPOSE 80

# Mensagem de boas-vindas no build
RUN echo "A garagem está pronta para receber seus carros!"

# Inicia o servidor (abre a garagem para clientes)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

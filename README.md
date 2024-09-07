# Detecção de Objetos com YOLO e FastAPI

Este projeto utiliza a rede YOLO (You Only Look Once) para detecção de objetos em imagens carregadas via API. O backend é desenvolvido em FastAPI, e a detecção é realizada utilizando o OpenCV e o modelo YOLOv3.

## Funcionalidades

- **Upload de Imagem:** Permite o upload de uma imagem para realizar a detecção de objetos.
- **Detecção de Objetos:** Realiza a detecção dos objetos presentes na imagem, retornando as coordenadas das caixas delimitadoras e a confiança de cada detecção.
- **Imagem Processada:** Retorna a imagem com as caixas desenhadas ao redor dos objetos detectados.

## Requisitos

- Python 3.x
- OpenCV
- NumPy
- FastAPI
- Uvicorn
- Pillow

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/vithorcamara/DetectorDeObjetosFastAPI.git
    cd DetectorDeObjetosFastAPI
    ```

2. Instale as dependências:
    ```bash
    pip install opencv-python numpy fastapi uvicorn pillow
    ```

3. Baixe os arquivos do YOLO:
    - [YOLOv3 Config](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
    - [YOLOv3 Weights](https://pjreddie.com/media/files/yolov3.weights)
    - [COCO Names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

    Coloque os arquivos `yolov3.cfg`, `yolov3.weights` e `coco.names` no diretório do projeto.

## Como Usar

1. Execute a API:
    ```bash
    uvicorn main:app --reload
    ```

2. Envie uma requisição `POST` para o endpoint `/detect/` com uma imagem para realizar a detecção de objetos.

## Estrutura do Projeto

```plaintext
.
├── yolov3.cfg
├── yolov3.weights
├── coco.names
├── main.py
└── README.md
```

## Endpoints

- **POST /detect/**: Carrega uma imagem e realiza a detecção de objetos, retornando as coordenadas e a imagem processada com as caixas delimitadoras.

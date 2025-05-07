## 📝 Descrição

Esta ferramenta de conversão de imagens em Python oferece processamento eficiente de imagens digitais com dois métodos principais de conversão:

1. **Conversão para Tons de Cinza**  
   Transforma imagens coloridas em escala de cinza (8-bit, 0-255) usando a fórmula padrão de luminosidade:  
   `0.299*R + 0.587*G + 0.114*B` para brilho preciso conforme a percepção humana.

2. **Conversão Binária**  
   Converte imagens para preto e branco puro (1-bit) com limiar ajustável:
   - Valor de threshold configurável (0-255)
   - Opção de inversão de cores
   - Processamento adaptativo para melhor reconhecimento de texto/objetos

Principais características técnicas:
- Implementação em Python puro (sem dependências externas além do PIL/Pillow)
- Processamento eficiente em memória usando arrays NumPy
- Suporte aos formatos de imagem mais comuns (JPEG, PNG, BMP, etc.)
- Capacidade de processamento em lote para pastas
- Interfaces CLI e API para diferentes casos de uso

A ferramenta é especialmente útil para:
- Preparar imagens para OCR (reconhecimento óptico de caracteres)
- Pré-processamento para visão computacional
- Projetos de digitalização de documentos
- Fluxos de trabalho de análise de imagens

Casos de uso comuns:
✔️ Converter documentos escaneados para extração de texto  
✔️ Pré-processar imagens para aprendizado de máquina  
✔️ Simplificar imagens complexas para análise  
✔️ Criar efeitos artísticos em preto e branco

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

## 📝 Description

acces on Google Colab: https://colab.research.google.com/drive/1iZveqsmSd-Lu_ncPB2xSYM0RRMHecSUT#scrollTo=0DGARKbkveQu
This Python-based Image Conversion Tool provides efficient processing of digital images with two primary conversion methods:

1. **Grayscale Conversion**  
   Transforms color images into 8-bit grayscale (0-255) using the standard luminosity formula:  
   `0.299*R + 0.587*G + 0.114*B` for accurate human-perceived brightness.

2. **Binary Conversion**  
   Converts images to pure black and white (1-bit) using customizable thresholding:
   - Adjustable threshold value (0-255)
   - Optional color inversion
   - Adaptive processing for optimal text/object recognition

Key technical features:
- Pure Python implementation (no external dependencies beyond PIL/Pillow)
- Memory-efficient processing using NumPy arrays
- Supports all common image formats (JPEG, PNG, BMP, etc.)
- Batch processing capabilities for folders
- CLI and API interfaces for different use cases

The tool is particularly useful for:
- Preparing images for OCR processing
- Computer vision preprocessing
- Document digitization projects
- Image analysis workflows

Example use cases:
✔️ Converting scanned documents for text extraction  
✔️ Preprocessing images for machine learning  
✔️ Simplifying complex images for analysis  
✔️ Creating artistic black-and-white effects

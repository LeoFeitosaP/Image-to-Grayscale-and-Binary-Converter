import requests
from PIL import Image
from io import BytesIO
import numpy as np
from matplotlib import pyplot as plt
from google.colab import files

#função de download da imagem
def download_image(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    return image
  except requests.exceptions.RequestException as e:
    print(f"Não foi possivel realizar o download da imagem: {e}")
    return None
  
  #função de conversão para tons de cinza e binarizada
def convert_image(color_name, threshold = 128):
  color_array = np.array(color_name)
  if len(color_array.shape) == 3 and color_array.shape[2] == 4:
    color_array = color_array[..., :3]

  if len(color_array.shape) == 3:
    gray_array = np.dot(color_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
  else:
    gray_array = color_array

  binary_array = np.where(gray_array > threshold, 255, 0).astype(np.uint8)

  return gray_array, binary_array

#plotar os resultados
print("\nExibindo resultados...")
plt.figure(figsize=(15, 5))
    
plt.subplot(1, 3, 1)
plt.imshow(color_image)
plt.title("Imagem Original")
plt.axis('off')
    
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title("Tons de Cinza")
plt.axis('off')
    
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title("Imagem Binarizada")
plt.axis('off')
    
plt.show()
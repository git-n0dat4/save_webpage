import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

def save_webpage(url, output_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 KB
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

            with open(output_path, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()
            print(f'Página web descargada y guardada en {output_path}')
        else:
            print(f'Error: Respuesta HTTP no exitosa ({response.status_code})')
    except requests.exceptions.RequestException as e:
        print(f'Error al hacer la solicitud HTTP: {e}')

# Usage
save_webpage('PAGE_URL', 'TEMPLATE_URL')
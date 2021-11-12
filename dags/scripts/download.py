from fastai.vision import download_images, verify_images
from fastai.imports import *

# Classes
classes = ['grass','dandelion']

# Download Path
path = Path('/opt/airflow/dags/data')

# Folder 1: Grass
folder = 'grass'
file = 'grass.csv'

dest = path/folder
dest.mkdir(parents=True, exist_ok=True)
download_images(path/file, dest, max_pics=200)

# Folder 2: Dandelion
folder = 'dandelion'
file = 'dandelion.csv'

dest = path/folder
dest.mkdir(parents=True, exist_ok=True)
download_images(path/file, dest, max_pics=200)

# Verify
for c in classes:
    print(c)
    verify_images(path/c, delete=True, max_size=500)
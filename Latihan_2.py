# Memanggil library
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

# PERCOBAAN 1 : CROP IMAGE
# Load gambar dari skicit.image
astronautImage = data.astronaut()
cameraImage = data.camera()

# Cropping gambar
astroCropped = astronautImage.copy()
astroCropped = astroCropped[0:256, 64:320]

camCropped = cameraImage.copy()
camCropped = camCropped[64:256, 128:320]

# Membuat figure subplot
fig, axes = plt.subplots(2, 2, figsize = (10, 10))
ax = axes.ravel()
ax[0].imshow(astronautImage)
ax[0].set_title("Citra Input 1")
ax[1].imshow(cameraImage, cmap = 'gray')
ax[1].set_title("Citra Input 2")
ax[2].imshow(astroCropped)
ax[2].set_title("Citra Output 1")
ax[3].imshow(camCropped, cmap = 'gray')
ax[3].set_title("Citra Output 2")

fig.tight_layout()
plt.show()
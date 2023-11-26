import numpy as np
from PIL import Image


class MyNN:
    def __init__(self, size: tuple, imagesAmount: int):
        """
        Keyword arguments:
        size         -- the width and height tuple
        imagesAmount -- the total images count
        """
        self.weightsInputHidden   = np.random.uniform(-0.5, 0.5, size[0] * size[1])
        self.weightsHiddentOutput = np.random.uniform(-0.5, 0.5, (imagesAmount , 2))

    def recognize(self, filePath: str, label: int):
        img = Image.open(filePath, 'r')
        width, height = img.size
        pixels = np.array(list(img.getdata())).reshape((width, height, 3))
        input = []
        for row in pixels:
            for r, g, b in row:
                input.append((r + g + b) / (255 * 3))

        input = np.array(input).reshape((width, height))
        hiddentLayer = np.matmul


nn = MyNN((28, 28), 5)
nn.recognize('0.jpg', 0)


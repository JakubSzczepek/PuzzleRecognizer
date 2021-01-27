import cv2
import numpy as np
import os


class Image:

    def __init__(self, path_to_images):
        self.path = path_to_images
        self.source_image = np.array(())
        self.puzzle_images = {}
        self.images_paths = []

    def load_source_image(self, source_image_name='source', extension="png"):
        extension = extension.replace(".", "")
        source_image_name = source_image_name.split(".")[0]
        self.source_image = cv2.imread(os.path.join(self.path, f"{source_image_name}.{extension}"))

    @staticmethod
    def load_puzzle_image(path, image_number, image_name='puzzle', extension="png"):
        extension = extension.replace(".", "")
        image_name = image_name.split(".")[0]
        return cv2.imread(os.path.join(path, f"{image_name}_{image_number}.{extension}"))

    def get_images_path(self, extension="png"):
        """

        :param extension:
        :return:
        """
        # TODO rewrite to pathlib
        extension = extension.replace(".", "")
        for root, directories, files in os.walk(self.path):
            for file in files:
                if file.endswith(f".{extension}"):
                    self.images_paths.append(os.path.join(root, file))


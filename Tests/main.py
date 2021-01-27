import unittest
from Tests.config_parser import ParseConfig
from Program.images import Image


class ImageClassTestCase(unittest.TestCase):

    def setUp(self):
        self.config = ParseConfig("config.ini")  # TODO change to attribute value sys.arg or argparser
        self.images_object = Image(self.config.path.joinpath(self.config.set))

    def test_listing_files_in_directory(self):
        self.images_object.get_images_path()
        self.assertTrue(len(self.images_object.images_paths) != 0, msg="List of paths should not be empty")

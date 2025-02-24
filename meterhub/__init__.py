"""
MeterHub is a Python library for detecting and handling meter images,
using API of [MeterHub](https://meterhub.sun-praise.com).

__author__ = "Sun Praise"
__email__ = "support@sun-praise.com"
__url__ = "https://meterhub.sun-praise.com"
__date__ = "2025-02-21"
"""

__version__ = "0.1.0"

from PIL import Image
import pathlib

class MeterHub:
  def __init__(self, api_key: str):
    self.api_key = api_key

  def handle_file(self, file: str | pathlib.Path | Image.Image):
    if isinstance(file, str | pathlib.Path):
      return Image.open(file)
    return file

  def detection(self, image: str | pathlib.Path | Image.Image):
    image = self.handle_file(image)



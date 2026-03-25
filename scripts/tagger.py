"""Tagger module entry point."""
from PIL import Image, ImageFile

from modules import script_callbacks  # pylint: disable=import-error
from tagger.ui import on_ui_tabs  # pylint: disable=import-error
from tagger.settings import on_ui_settings  # pylint: disable=import-error

try:
    from tagger.api import on_app_started  # pylint: disable=import-error
except Exception as exc:  # pragma: no cover
    # Keep UI usable even if API-side dependencies differ across forks.
    print(f"[WD14 tagger] API integration disabled: {exc}")
    on_app_started = None


# if you do not initialize the Image object
# Image.registered_extensions() returns only PNG
Image.init()

# PIL spits errors when loading a truncated image by default
# https://pillow.readthedocs.io/en/stable/reference/ImageFile.html#PIL.ImageFile.LOAD_TRUNCATED_IMAGES
ImageFile.LOAD_TRUNCATED_IMAGES = True


if on_app_started is not None:
    script_callbacks.on_app_started(on_app_started)
script_callbacks.on_ui_tabs(on_ui_tabs)
script_callbacks.on_ui_settings(on_ui_settings)

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport
from luma.core.render import canvas
from PIL import ImageFont
import time

# Setup SPI connection
serial = spi(port=0, device=0, gpio=noop())

# Create device with 1 matrix (can set cascaded=2 or more for more displays)
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
device.contrast(5)

# Optional: Load a tiny font
font = ImageFont.load_default()

# Draw scrolling text
msg = "Hello, Pi!"
with viewport(device, width=8*len(msg), height=8) as vp:
    for i in range(8 * len(msg)):
        with canvas(vp) as draw:
            draw.text((-i, 0), msg, fill="white", font=font)
        time.sleep(0.1)

#!/usr/bin/env python3
"""
Example Anvil uplink to flip image

Usage:
    anviluplinkimproc <key>

"""
import docopt
import anvil
import anvil.server
import imageio
import anviluplinkimproc.flipper as flipper

opts = docopt.docopt(__doc__)

anvil.server.connect(opts["<key>"])

@anvil.server.callable
def process_image(image):
    image_bytes = image.get_content()
    flipped_image = flipper.process_image_from_bytes(image_bytes)
    fi_bytes = imageio.imwrite(imageio.RETURN_BYTES,
                               flipped_image, "png")
    return anvil.DataMedia("image/png", fi_bytes)

def main():
    anvil.server.wait_forever()

if __name__ == "__main__":
    main()

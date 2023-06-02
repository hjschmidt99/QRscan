import sys
import traceback
import clipboard
from pyzbar import pyzbar
from PIL import Image

def scanQR(f):
    qr = pyzbar.decode(Image.open(f))
    return str(qr[0].data.decode("utf-8"))
    
if __name__ == '__main__':
    try:
        f = r"QR_deWP.svg.png"
        if len(sys.argv) > 1:
            f = sys.argv[1]
        s = scanQR(f)
        print(s)
        clipboard.copy(s)
    except:
        traceback.print_exc()
        input("...")

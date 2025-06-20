import os
import io
import datetime
from PIL import Image

os.environ["GS_DLL_PATH"] = r"C:\Program Files\gs\gs9.55.0\bin\gsdll64.dll"


def save_png(
        canvas,
        folder=r"C:\Code\Code_in_place\project\random_shape\output"
):
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    timeStamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"IMG_{timeStamp}.png"
    output_path = os.path.join(folder, filename)

    canvas.update()

    ps = canvas.postscript(
        colormode='color'
    )

    image = Image.open(
        io.BytesIO(
            ps.encode("utf-8")
        )
    )

    image.save(output_path, "png")

    print(f"{filename} saved to: {output_path}")
    return output_path

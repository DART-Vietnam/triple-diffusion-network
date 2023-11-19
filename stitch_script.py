# import imageio
# import os

# with imageio.get_writer("./anim.gif", mode="I", duration=0.5) as writer:
#     for im_path in os.listdir("network_sims"):
#         if im_path.endswith(".png"):
#             image = imageio.imread("./network_sims/" + im_path)
#             writer.append_data(image)

# ------------------------------------------------------------------------------

from PIL import Image
import os

imgs = []
for im_path in os.listdir("network_sims"):
    if im_path.endswith(".png"):
        imgs.append(Image.open("./network_sims/" + im_path))

imgs[0].save(
    "./anim.gif",
    save_all=True,
    append_images=imgs[1:],
    optimize=False,
    duration=1480,
    loop=0,
)

from PIL import Image, ImageSequence

image1 = Image.open("image11.jpg")
image2 = Image.open("image22.png")

images_list = [image1,image2]

gif_path = "output.gif"

images_list[0].save(gif_path, save_all=True, append_images=images_list[0:1], duration=300, loop=0)

print("GIF dosyasi oluşturuldu:", gif_path)
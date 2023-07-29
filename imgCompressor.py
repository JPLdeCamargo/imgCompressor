from PIL import Image, ImageDraw


class ImgCompressor:
    def __init__(self, img_path:str) -> None:
        self.__img_path = img_path


    def compress(self, save_path:str, compression_strength:int, pixel_art:bool):
        with Image.open(self.__img_path) as im:
            pixels = im.load()
            print(type(pixels))
            width, height = im.size
            print(width,height)

        new_heigth = height//compression_strength
        new_width = width//compression_strength
        print(f"new_width = {new_width}")

        new_pixels = [[tuple() for i in range(new_width)] for j in range(new_heigth)]
        for i in range(new_heigth):
            for j in range(new_width):
                color = self.__get_color(pixels, j, i, compression_strength, pixel_art)   
                new_pixels[i][j] = color

        compressed_image = Image.new(mode= "RGB", size = (new_width, new_heigth))
        draw = ImageDraw.Draw(compressed_image)
        for i in range(new_heigth):
            for j in range(new_width):
                draw.point((j,i), fill=new_pixels[i][j])

        compressed_image.save(save_path)


    def __get_color(self, pixels, x:int, y:int, compression:int, pixel_art:bool) -> tuple[int]:
        pivot = (x*compression, y*compression)
        color_sum = [0, 0, 0]
        if pixel_art:
            return pixels[pivot[0]+(compression//2), pivot[1]+(compression//2)]

        for i in range(compression):
            for j in range(compression):
                crt_x = pivot[0] + i
                crt_y = pivot[1] + j
                color = pixels[crt_x, crt_y]
                color_sum = [color_sum[k] + color[k] for k in range(3)]

        final_color = [color_sum[i]//pow(compression, 2) for i in range(3)]
        # uncomment for grey scale
        # final_color = [sum(final_color)//3] * 3
        return tuple(final_color)

if __name__ == "__main__":
    compressor = ImgCompressor("vetor.jpg")
    compressor.compress("mini_vetor.jpg", 100, False)

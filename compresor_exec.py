from imgCompressor import ImgCompressor

if __name__ == "__main__":
    print("Image path: ")
    path = input()
    print("Compression strength: ")
    strength = int(input())
    print("Save path: ")
    save_path = input()
    print("Pixel mode enabled ? y/n")
    pixel_mode  = True if input() == 'y' else False
    
    try:
        compressor = ImgCompressor(path)
        compressor.compress(save_path, strength, pixel_mode)
    except:
        print("oh no")

import os

def get_image_paths(folder):
    image_paths = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(("jpg", "jpeg", "png")):
                image_paths.append(os.path.join(root, file))

    return image_paths

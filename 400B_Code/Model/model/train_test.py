import os
import shutil
import random

# Define paths
data_folder = "E:\\Capstone\\Dataset\\Gray_Img\\G_Images"
train_folder = "E:\\Capstone\\Dataset\\Gray_Img\\train"
test_folder = "E:\\Capstone\\Dataset\\Gray_Img\\test"
split_ratio = 0.8  # 80% train, 20% test

# Iterate over each class folder
for class_folder in os.listdir(data_folder):
    class_path = os.path.join(data_folder, class_folder)
    
    # Create train and test folders for the class
    train_class_path = os.path.join(train_folder, class_folder)
    test_class_path = os.path.join(test_folder, class_folder)
    os.makedirs(train_class_path, exist_ok=True)
    os.makedirs(test_class_path, exist_ok=True)
    
    # Get list of images in the class folder
    images = os.listdir(class_path)
    random.shuffle(images)  # Shuffle images
    
    # Split images into train and test sets
    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    test_images = images[split_index:]
    
    # Move train images
    for image in train_images:
        src = os.path.join(class_path, image)
        dst = os.path.join(train_class_path, image)
        shutil.copy(src, dst)
    
    # Move test images
    for image in test_images:
        src = os.path.join(class_path, image)
        dst = os.path.join(test_class_path, image)
        shutil.copy(src, dst)

print("Splitting completed successfully.")

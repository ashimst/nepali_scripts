import os
import random
import shutil

# Set your paths
original_dataset_dir = "dataset"
train_dir = "dataset_train"
test_dir = "dataset_test"

# Optional: Set seed for reproducibility
random.seed(42)

# Clean previous train/test folders
for dir_path in [train_dir, test_dir]:
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)

# Go through each class folder
for class_name in os.listdir(original_dataset_dir):
    class_path = os.path.join(original_dataset_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # Create class folders in train and test dirs
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # List and shuffle images
    images = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]
    random.shuffle(images)

    # Ensure there are at least 25 images
    if len(images) < 25:
        print(f"Warning: Class '{class_name}' has less than 25 images.")
        continue

    # Split
    train_images = images[:20]
    test_images = images[20:25]

    # Copy train images
    for img in train_images:
        shutil.copy(os.path.join(class_path, img), os.path.join(train_dir, class_name, img))

    # Copy test images
    for img in test_images:
        shutil.copy(os.path.join(class_path, img), os.path.join(test_dir, class_name, img))

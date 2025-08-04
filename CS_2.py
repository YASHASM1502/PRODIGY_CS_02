import numpy as np
import cv2
from matplotlib import pyplot as plt

# Function to encrypt an image by swapping halves and adding a key

def encrypt_image(image_path, key):
    # Load image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Image not found or unable to load")
    # Convert to float for mathematical operations
    img_float = img.astype(np.float32)
    # Swap halves of the image horizontally
    height, width, channels = img.shape
    half_width = width // 2
    # Swap the left and right halves
    img_float[:, :half_width, :], img_float[:, half_width:, :] = \
        img_float[:, half_width:, :], img_float[:, :half_width, :]
    # Apply mathematical operation: add key
    encrypted_img = (img_float + key) % 256
    # Convert back to uint8
    encrypted_img = encrypted_img.astype(np.uint8)
    return encrypted_img

# Function to decrypt an image by reversing the operations
def decrypt_image(encrypted_img, key):
    # Reverse mathematical operation
    img_float = (encrypted_img.astype(np.float32) - key) % 256
    # Swap halves back
    height, width, channels = encrypted_img.shape
    half_width = width // 2
    # Swap halves back
    img_float[:, :half_width, :], img_float[:, half_width:, :] = \
        img_float[:, half_width:, :], img_float[:, :half_width, :]
    # Convert back to uint8
    decrypted_img = img_float.astype(np.uint8)
    return decrypted_img

# Example usage
# Replace 'your_image.jpg' with the path to your image file
image_path = "C:\\Users\\yasha\\OneDrive\\Desktop\\Imporatnt documents\\Professional pic.jpg"
key = 50  # Example key

# Encrypt the image
encrypted_img = encrypt_image(image_path, key)

# Save encrypted image
cv2.imwrite('encrypted_image.jpg', encrypted_img)

# Decrypt the image
decrypted_img = decrypt_image(encrypted_img, key)

# Save decrypted image
cv2.imwrite('decrypted_image.jpg', decrypted_img)

# Display images
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.title('Original')
original_img = cv2.imread(image_path)
plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1,3,2)
plt.title('Encrypted')
plt.imshow(cv2.cvtColor(encrypted_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1,3,3)
plt.title('Decrypted')
plt.imshow(cv2.cvtColor(decrypted_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
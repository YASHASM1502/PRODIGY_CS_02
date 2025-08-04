### 🔐 **🔹 Task 2: Image Encryption & Decryption**

The objective was to **secure image data** by implementing a custom image encryption and decryption mechanism using **OpenCV**, **NumPy**, and **Matplotlib**.

---
![Uploading image.png…]()


### 🛠️ **Technologies Used**

* **Python** 🐍
* **OpenCV** (`cv2`) – for image reading, writing, and pixel-level manipulation
* **NumPy** – for efficient matrix operations
* **Matplotlib** – for displaying original, encrypted, and decrypted images

---

### 🔍 **How it Works**

1. **Image Encryption:**

   * The image is loaded and converted to a float array.
   * The image is **horizontally split into two halves**.
   * The left and right halves are **swapped** to introduce confusion.
   * A **numerical key** is **added to every pixel** value for encryption.
   * The image is then converted back to `uint8` for saving/displaying.

2. **Image Decryption:**

   * The encrypted image is reloaded.
   * The **encryption key is subtracted** from all pixels.
   * The halves are **swapped back** to their original positions.
   * The final output is a **visually identical reconstruction** of the original image.

---

### 🌟 **Key Features**

* 🔒 **Simple encryption logic** that introduces both spatial and pixel-level transformation.
* 🔁 Fully **reversible** decryption process using the same key.
* 🖼️ Visual comparison using `Matplotlib` of:

  * Original Image
  * Encrypted Image
  * Decrypted Image

---

### 📸 **Use Case & Applications**

* Ideal for demonstrating **basic cryptography concepts** in images.
* Useful for **educational projects** on image security and pixel manipulation.
* Can be extended to support **stronger encryption** using more advanced algorithms.




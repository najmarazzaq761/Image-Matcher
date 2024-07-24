# Image Matcher

https://github.com/user-attachments/assets/46086ef2-0165-4b44-a197-90cf2a7a5246

## Overview
**Image Matcher** is a Streamlit app designed to find similar images from a pre-defined database. Leveraging the power of **OpenCV**, **scikit-image**, and **color histogram** for feature extraction, this app provides a simple and intuitive interface for image comparison.

## Features
- **Streamlit Interface**: A user-friendly web app for image uploading and similarity search.
- **OpenCV**: Utilized for image processing tasks.
- **scikit-image**: Used for advanced image analysis.
- **color histogram**: Employed for feature vector calculation to capture texture information.

## How It Works
1. **Upload an Image**: Users can upload an image in JPG, PNG, or JPEG format.
2. **Feature Extraction**: The app processes the uploaded image to extract feature vectors using LBP.
3. **Similarity Search**: The app compares the feature vectors of the uploaded image with those in the database using cosine similarity.
4. **Results Display**: The most similar image from the database is displayed alongside the uploaded image.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/image-matcher.git
   cd image-matcher
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv streamlit_env
   source streamlit_env/bin/activate   # On Windows use `streamlit_env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Upload an Image**: Use the Streamlit interface to upload an image.
3. **View Results**: The app will display the uploaded image alongside the most similar image found in the database.

## File Structure
- `app.py`: The main Streamlit app script.
- `requirements.txt`: A list of required Python packages.
- `database/`: A directory containing images for comparison.

## Dependencies
- **Streamlit**
- **OpenCV**
- **scikit-image**
- **numpy**
- **scikit-learn**

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact [najmarazzaq761@gmail.com]


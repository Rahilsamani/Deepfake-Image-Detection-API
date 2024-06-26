# Deepfake Image Detection API

This repository contains a Deepfake Image Detection API built using FastAPI. The API allows you to send images and receive a response indicating whether the image is a deepfake or not.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rahilsamani/Deepfake-Image-Detection-API.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Deepfake-Image-Detection-API
   ```

## Setup

Follow the steps below to set up and run the API locally.

### 1. Create a Virtual Environment

```bash
python -m venv fastml
```

### 2. Activate the Virtual Environment

- For Windows:

```bash
.\fastml\Scripts\activate
```

- For macOS/Linux:

```bash
source fastml/bin/activate
```

### 3. Install Dependencies

```bash
pip install uvicorn gunicorn fastapi pydantic scikit-learn pandas pillow torch transformers python-multipart
```

### 4. Run the API

```bash
uvicorn mlapi:app --reload
```

The API will be running on [http://localhost:8000](http://localhost:8000).

## Usage

To use the API, send a POST request to the `/` endpoint with an image file. Send the image using form data with key name `image` and type will be file.

## Use Case

One use case for this API is integrating it into a social media application to distinguish between deepfake images and real images, enhancing the trust and authenticity of the content shared on the platform.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## Contact

If you have any questions or feedback, please feel free to contact me at rahilahmed1720@gmail.com.


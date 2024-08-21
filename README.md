# Language Translator App

This project includes a language translator app developed using Streamlit, which converts English text to Hindi. The translation model is trained using the Helsinki-NLP/opus-mt-en-hi model from Hugging Face, leveraging the cfilt/iitb-english-hindi dataset.

## Features

- **Model Training**: Train the model using the provided Jupyter notebook.
- **User-Friendly Interface**: Simple and intuitive design for easy translation.
- **Fast and Accurate Translation**: Uses a fine-tuned pre-trained model to provide reliable translations.

## Prerequisites

- Python 3.7+
- `streamlit`
- `torch`
- `transformers`
- `tensorflow`
- `notebook` (for running the Jupyter notebook)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/language-translator-app.git
   cd language-translator-app

2. Install the required Python packages by running the requirements.txt file:

   ```bash
   pip install -r requirements.txt

## Usage

### Step 1: Train the Model

1. Open the language_translator.ipynb notebook in Jupyter or JupyterLab.

   ```bash
   jupyter notebook language_translator.ipynb

2. Follow the steps in the notebook to train the model. The model is trained for 10 epochs on the test dataset due to the large size of the training dataset.

3. The trained model will be saved in the tf_model folder.

### Step 2: Run the Streamlit App

1. After training the model, you can run the Streamlit app:

   ```bash
   streamlit run app.py

2. The app will open in your web browser. You can enter English text in the input field, and the app will translate it to Hindi using the trained model.

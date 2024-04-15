# Image Content Generator
Upload an Image and tell it what you want it to do and it will do that for you.

## Requirements to Reproduce
1. Get the API Key from `https://aistudio.google.com/app/apikey`
2. Create a `.env` file and add `GOOGLE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"`

### Steps to Reproduce

#### Step 1.0
```bash
conda create -p env
```


#### Step 1.5
```bash
conda activate ./env
```

#### Step 1.9
```bash
pip install -r requirements.txt
```


#### Step 2.0
```bash
streamlit run app.py
```

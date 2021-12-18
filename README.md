# This Project is a template to Deploy your streamlit application on your server

A tutorial is available on my website: https://www.hadarak.com/

## For development only:

### 🚧 Install dependencies :
```
conda create -n <env_name> python=3.8
conda activate <env_name>
pip install -r requirements.txt
```

### ▶️ To Run Streamlit :
```
streamlit run app.py
```

## For production :

## 🚀 Build locally using docker :

Run docker locally
```
docker build -t <image_name> .
```

Test your docker Image
```
docker run -p 8502:8502 <image_name>
```

## ✅ If your container is working you can follow the deployment tutorial
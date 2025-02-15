# ☀️ Solar Industry AI Assistant

Solar Industry AI Assistant is a **Streamlit-based application** that helps users get insights about solar energy.  
This tool provides **suggested questions** categorized into different topics, along with a **search feature** for custom queries.

---

## ⚙️ **Features**

- 🔍 **Search Bar:** Ask any question related to solar energy.
- 💡 **Suggested Questions:** Pre-categorized questions for quick insights.
- ✅ **Basic Questions:** General information about solar energy.
- ⚙️ **Technical Questions:** In-depth technical knowledge.
- 💰 **Financial & ROI Questions:** Cost, payback period, and ROI analysis.
- 📈 **Industry & Market Trends:** Latest trends and future predictions.
- 🔧 **Maintenance & Troubleshooting:** Guidance on maintaining solar systems.

---

## 🚀 **Getting Started**

### Prerequisites
- **Python 3.x** installed on your machine.
- **Streamlit** for UI rendering.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/aryanchauhan007/Solar_Industry-AI-Agent.git
    cd Solar_Assistant
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
---

## 🔑 **Setting up Hugging Face API using `secrets.toml`**

This application uses the **Hugging Face API** for generating intelligent responses.  
To securely manage the API key, we use **Streamlit's `secrets.toml`** method.  

---

### 📌 **Step 1: Get Hugging Face API Key**  
1. Create an account or log in at [Hugging Face](https://huggingface.co/join).  
2. Navigate to **Settings > API tokens**.  
3. Generate a new API token and **copy** it securely.

---

### 📁 **Step 2: Add API Key to `secrets.toml`**  
In Streamlit, we securely store secrets using `secrets.toml`.  

1. **Create a `secrets.toml` file** in the `.streamlit` directory:
    ```
    .streamlit/secrets.toml
    ```
    - If `.streamlit` directory doesn't exist, **create it manually**.

2. Add the following content to `secrets.toml`:
    ```toml
    # .streamlit/secrets.toml
    HUGGINGFACE_API_KEY = "your_api_key_here"
    ```
   - Replace `your_api_key_here` with your actual Hugging Face API key.  

---

### 🔒 **Step 3: Secure the API Key (Ignore in Git)**  
- Make sure `secrets.toml` **is not pushed to GitHub** by adding it to `.gitignore`:
    ```
    # Ignore Streamlit secrets
    .streamlit/secrets.toml
    ```
- **Note:** This is already configured in this project.  
  - Double-check before pushing to GitHub to **avoid accidental exposure**.

---

### 🌐 **Step 4: Using the API Key in Code**  
In `backend.py`, access the API key like this:
```python
import streamlit as st
import requests

# Get Hugging Face API key from secrets
API_KEY = st.secrets["HUGGINGFACE_API_KEY"]

def get_ai_response(user_query):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    url = "https://api-inference.huggingface.co/models/YOUR_MODEL_NAME"
    payload = {
        "inputs": user_query
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
```    

### Running the App
```bash
streamlit run app.py
```

# ScreenShots
<img width="595" alt="question1" src="https://github.com/user-attachments/assets/61145044-46a7-4b0a-bb2e-8b9919af8c65" />

<img width="551" alt="answer" src="https://github.com/user-attachments/assets/d339b160-c231-48ac-91bc-5a3c3fc50d68" />




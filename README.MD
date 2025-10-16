# GOOGLE OAUTH 

This project is  **google oauth** built using **Django**,and  **Django REST Framework (DRF)**  

---

## 🚀 Features
- signup and login via google account
---

## 📂 Project Structure
```
server/
│── accounts/
│   ├── views.py          # API views (GET and callback)
│   ├── urls.py           # API routes
│── server/
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main project URLs
│── env/                  # Virtual environment
│── manage.py             # Django entry point
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/muhammad-hamza-liaqat/google-oauth
```

### 2️⃣ Create & activate virtual environment
```bash
python3.11 -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root with:

```env
SECRET_KEY=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=

```

---

## ▶️ Run the Project

Start Django server:
```bash
python manage.py runserver
```

---

## 📦 Dependencies
- Django
- Django REST Framework
- python-dotenv
- google-auth
- requests
- djangorestframework-simplejwt


Install everything via:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing
Pull requests are welcome.  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is licensed under the MIT License.

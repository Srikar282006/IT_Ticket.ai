# Intelligent IT Ticket Resolver - Multi-Agent System

An AI-powered Multi-Agent IT Ticket Resolution System built using **AutoGen**, **Azure OpenAI**, and **Streamlit**. The system classifies user-submitted IT support tickets and can be extended with multiple specialized agents for intelligent ticket routing and resolution.

## 🚀 Features

- 🤖 AI-powered IT Ticket Classification
- 🧠 Multi-Agent Architecture using AutoGen
- ☁️ Azure OpenAI Integration
- 💬 Interactive Streamlit Interface
- 📊 Extensible Agent Workflow


---

## ⚙️ Prerequisites

- Python 3.10+
- Azure OpenAI Resource
- Azure OpenAI Deployment
- Azure OpenAI API Key

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Intelligent-It-Ticket-Resolver
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
AZURE_OPENAI_ENDPOINT
AZURE_DEPLOYMENT_NAME
AZURE_API_VERSION
AZURE_OPENAI_API_KEY
AZURE_SEARCH_ENDPOINT
AZURE_SEARCH_KEY
AZURE_OPENAI_DEPLOYMENT
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser at:

```
http://localhost:8501
```

---

## 🛠️ Tech Stack

- Python
- AutoGen
- Azure OpenAI
- Streamlit
- Python Dotenv

---

## 📌 Future Enhancements

- Ticket Prioritization Agent
- Knowledge Base Retrieval (RAG)
- Ticket Routing Agent
- Resolution Recommendation Agent
- Email Notification Support
- Dashboard & Analytics



---

## 📄 License

This project is intended for learning and educational purposes.

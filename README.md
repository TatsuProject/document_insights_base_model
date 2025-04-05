# 📄 Document Insights

Document Insights is an advanced document understanding system that performs three core tasks with state-of-the-art accuracy:

- 🟩 **Checkbox-Text Pair Detection**  
- 🧠 **Document Classification (OCR-Free)**  
- 📄 **Document Parsing with LLMs**

## 🚀 Key Features

### ✅ Checkbox Detection (YOLOv8)
Custom-trained **YOLOv8-large** model fine-tuned on 10,000+ diverse document images (scanned + digital) with outstanding precision.

#### 📊 Performance Comparison (F1-Score)
| Model                     | F1-Score |
|---------------------------|----------|
| Azure Form Recognizer     | 0.72     |
| GPT-4 Vision              | 0.63     |
| **YOLO Checkbox Detector** | **0.88** |

### 🧠 Document Classification (DONUT)
OCR-free classification using the **DONUT model** - fast, lightweight, and accurate.

### 📄 Document Parsing (LLM-based)
Flexible parsing options:
- ☁️ **API-based** (OpenAI, Claude)
- 💻 **Local LLMs** (`qwen:14b` via [Ollama](https://ollama.com))

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/TatsuProject/document_insights_base_model
cd document_insights_base_model
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📥 Downloading Model Weights

### ✅ YOLO Checkbox Detector

- Join our [Discord Community](https://discord.com/channels/799672011265015819/1300456223371427912) to get access to the model weights.
- Create a `model/` directory at the root of this repository.
- Place the downloaded weight file inside the `model/` folder.

---

### 🗂️ Document Classification (DONUT)

Weights for DONUT will be downloaded automatically from Hugging Face the first time the model is used.  
Please ensure you have **at least 10 GB of free disk space**.

---

## 🧠 Using LLMs
To use the LLMs through API, you need to have an API key and include it in the script located at `doc_parser/get_llm_response_api.py`. You can also implement your custom logic in this script as needed.

To run document parsing without relying on external APIs, you can host LLMs locally using **Ollama**.

### 🧰 Step 1: Install Ollama

1. Visit the official website: [https://ollama.com](https://ollama.com)  
2. Download and install Ollama for your OS (Linux, macOS, or Windows)  
3. Start the Ollama service:

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
```

### 📦 Step 2: Download Qwen 2.5 14B Locally

Run the following command to download and serve Qwen 2.5 (14B) using Ollama:

```bash
ollama pull qwen2.5:14b
ollama run qwen2.5:14b

```
---

### 🧪 Running Tests

**1. Start the main app service:**

```bash
python app.py
```

**2. Run a test on a document/image:**
```bash
python test_app.py
```
Make sure to update `test_app.py` with the correct image path.

You can set the `task_type` parameter to one of the following:

- `"checkbox"` – for checkbox-text detection  
- `"doc-class"` – for document classification  
- `"doc-parse"` – for document parsing using LLM

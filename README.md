## 🛠️ Setup Instructions (Using `uv`)

### 📋 Prerequisites
Ensure `uv` is installed on your system. You can install it using:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🐍 Install Python
```
uv python install
```

### 🌱 Create and activate virtual environment
```
uv env
source .venv/bin/activate
```

### 📦 Install Dependencies
```sh
uv sync
```

### 🔐 Setup env vars
```
export OPENAI_API_KEY
```

### 🧪 Running Tests
```
pytest
```

### 🔍 Running deepevals
```
deepeval test run tests/...
```
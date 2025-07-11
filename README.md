# AI Text Buddy (Backend) - Setup Instructions

## Backend Setup

### 1. Install Python Dependencies

Using [uv](https://github.com/astral-sh/uv) (recommended):

```bash
uv venv
uv pip install '.[dev]'
```

Or if you prefer `pip`:

```bash
pip install -e .[dev]
```

### 2. Set Up Environment Variables

Copy the sample file and update your API key:

```bash
cp .env.sample .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Or set the environment variable directly:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

---

### 3. Run the Backend Server (Local Development)

```bash
uv run server.py
```

The server will start at: `http://localhost:8000`

---

### 4. Run as Lambda Function

* Package the code with dependencies (zip or container image).
* Set the Lambda handler to:

```
lambda_handler.handler
```

**Note:**
Lambda requires the `mangum` dependency. Install it if you haven’t:

```bash
uv pip install .[lambda]
```

---

## API Endpoints

These endpoints act as your **API documentation**:

### `GET /health`

Check server status and AI availability.

**Response example:**

```json
{
  "status": "healthy",
  "message": "Backend is running"
}
```

---

### `POST /fix-text`

**Request:**

```json
{
  "text": "text to fix"
}
```

**Response:**

```json
{
  "success": true,
  "processed_text": "corrected text"
}
```

---

### `POST /rewrite-text`

**Request:**

```json
{
  "text": "text to rewrite"
}
```

**Response:**

```json
{
  "success": true,
  "processed_text": "rewritten text"
}
```

---

## Chrome Extension Setup

### 1. Prepare Extension Files

Clone repo for chrome extension at <TODO>

---

### 2. Load Extension in Chrome

1. Go to `chrome://extensions/`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select the extension folder

---

### 3. Test the Extension

1. Make sure the backend is running
2. Go to any webpage with text inputs
3. Right-click a text input
4. You should see:

* **Fix with AI**
* **Rewrite with AI**

---

## Usage

### Fix with AI

* Corrects grammar, spelling, punctuation
* Preserves original meaning and style

---

### Rewrite with AI

* Improves clarity and engagement
* Can restructure sentences


---

## Troubleshooting

### Common Issues

1. **Extension not working:** Backend may not be running on port 8000
2. **AI not responding:** Check your OpenAI API key
3. **CORS errors:** Verify CORS settings allow requests from the extension
4. **Context menu missing:** Make sure you right-click on editable fields

---

### Development Tips

* Check browser console for JavaScript errors
* Watch backend logs for API errors
* Use the `/health` endpoint to verify server status
* The extension works on `<input>`, `<textarea>`, and `contenteditable`

---

## Security Note

This implementation uses unprotected APIs. For production, consider:

* API authentication
* Rate limiting
* Input validation
* CORS restrictions
* Error handling improvements

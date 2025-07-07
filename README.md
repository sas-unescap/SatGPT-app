# About SatGPT

SATGPT, an innovative solution that leverages the current capabilities of LLMs and integrates
them with cloud computing platforms and Earth Observation data. SATGPT represents a fully
functional, next-generation spatial decision support system designed for rapid deployment,
particularly in resource-limited contexts.


### Setup Instructions

1. **(Recommended) Set up a Python virtual environment:**
   ```sh
   python3 -m venv satgpt-venv
   source satgpt-venv/bin/activate
   ```
   This keeps your dependencies isolated and avoids conflicts with other projects.

2. **Copy the example environment file:**
   ```sh
   cp .env.example .env
   ```
3. **Edit `.env`** and fill in your own credentials:

   ```env
   EE_ACCOUNT=your_service_account_email
   EE_PRIVATE_KEY_FILE=./satgpt-<your-project-id>-<unique>.json
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   MAPBOX_ACCESS_KEY=your_mapbox_access_key
   CHATGPT_API_KEY=your_openai_api_key
   ```

4. **Download your Google service account key** and place it in the project root (or wherever you specify in `EE_PRIVATE_KEY_FILE`). The file should be named with the pattern `satgpt-<your-project-id>-<unique>.json`.

5. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**

   - **If using a virtual environment:**
     ```sh
     source satgpt-venv/bin/activate
     ```
   - **Development server (not for production):**
     ```sh
     python app.py
     ```

### Security Notes
- All files matching `satgpt-*.json`, `.env`, and `.env.*` are ignored by git and should never be committed.
- The `.env.example` is safe to commit and provides a template for others to configure their own environment.

### Why this approach?
This ensures:
- No sensitive credentials are ever exposed in the public repository.
- Each user can bring their own API keys and service accounts.

---

## Quick Start

1. Copy `.env.example` to `.env`
2. Fill in your credentials
3. Place your service account key as described above
4. Install dependencies and run the app

---

For more details, see comments in `config.py` and `.env.example`.
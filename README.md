# Shadow Protocol — SHADOW_PROTOCOL_ENCRYPTOR

⚠️ **Quick start (Windows PowerShell)**

1. Install Python 3.8+ (recommended 3.10+).
2. Open PowerShell in the project folder (where `app.py` lives).
3. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation fails due to execution policy, run as administrator or:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

4. Install dependencies:

```powershell
pip install streamlit
```

(Optionally create a `requirements.txt` with `streamlit` for reproducibility.)

5. Run the app:

```powershell
streamlit run app.py
```

6. Open your browser at: `http://localhost:8501` (Streamlit prints the exact URL in the terminal).

---

## What this app does

- A simple Streamlit UI that hides text inside zero-width Unicode characters (steganography).
- Use the left panel to "inject" (encrypt) a hidden payload into a visible cover string (e.g., emojis).
- Use the right panel to paste intercepted data and attempt decryption.

## Notes & Tips

- The app uses a Google font (`Fira Code`) via a remote import — an internet connection is required for that styling to load.
- Stop the server with Ctrl+C in the terminal running Streamlit.
- Tested on Windows with Streamlit; behavior should be the same on macOS/Linux.

## Security & License

- This is an educational tool. Be careful with real sensitive data — use at your own risk.
- No license specified. Add a `LICENSE` file if you plan to publish or share.

---

If you'd like, I can also add a `requirements.txt` and a small `LICENSE` for you. ✅

import streamlit as st
import time

# --- ADVANCED CYBERPUNK CSS (SCARY/TECHY) ---
st.set_page_config(page_title="SHADOW PROTOCOL v2.0", page_icon="☣️", layout="wide")

st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&display=swap');
    
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(#112211 0.5px, transparent 0.5px);
        background-size: 20px 20px;
    }
    
    * {
        font-family: 'Fira Code', monospace !important;
        color: #00FF41 !important;
    }

    /* Red Alerts for Scary Vibes */
    .stAlert {
        background-color: #1a0000 !important;
        border: 1px solid #ff0000 !important;
        color: #ff0000 !important;
    }

    /* Input Boxes with Neon Glow */
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        box-shadow: inset 0 0 5px #00FF41;
        border-radius: 0px !important;
    }

    /* Glitchy Button Effect */
    .stButton>button {
        width: 100%;
        background-color: transparent !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        font-weight: bold;
        letter-spacing: 2px;
        transition: 0.3s;
        height: 50px;
    }
    
    .stButton>button:hover {
        background-color: #00FF41 !important;
        color: black !important;
        box-shadow: 0 0 20px #00FF41;
        cursor: crosshair;
    }

    /* Sci-Fi Headings */
    h1 {
        text-align: center;
        text-shadow: 2px 2px #ff0000, -2px -2px #00FF41;
        font-size: 3rem !important;
        letter-spacing: 5px;
    }
    
    /* Terminal Console Style */
    .terminal-output {
        background: #000;
        border: 1px solid #333;
        padding: 10px;
        font-size: 0.8rem;
        color: #00FF41;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CORE LOGIC (Zero-Width Cryptography) ---
CHARS = {'0': '\u200b', '1': '\u200c'}
REV_CHARS = {v: k for k, v in CHARS.items()}

def encrypt(cover, secret):
    bits = bin(int.from_bytes(secret.encode('utf-8'), 'big'))[2:].zfill(8)
    encoded = "".join(CHARS[b] for b in bits)
    return cover[0] + encoded + cover[1:]

def decrypt(cipher):
    bits = "".join(REV_CHARS[c] for c in cipher if c in REV_CHARS)
    if not bits: return None
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8')
    except: return "CORRUPTED_STREAM_ERROR"

# --- INTERFACE ---
st.markdown("<h1>☣️ SHADOW_PROTOCOL_ENCRYPTOR ☣️</h1>")
st.markdown("<p style='text-align:center; color:red !important;'>WARNING: AUTHORIZED ACCESS ONLY - ENCRYPTION LEVEL: MILITARY</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📡 INJECT HIDDEN PAYLOAD")
    cover = st.text_input("SET COVER EMOJIS (TARGET_VISUAL)", "👹☢️")
    secret = st.text_area("ENTER SENSITIVE DATA (ENCRYPTED_STRING)")
    
    if st.button("RUN_INJECTION_SEQUENCE"):
        if secret:
            with st.status("Initializing Encryption...", expanded=True) as status:
                st.write("Bypassing firewalls...")
                time.sleep(0.5)
                st.write("Mapping Unicode layers...")
                time.sleep(0.5)
                final = encrypt(cover, secret)
                status.update(label="PAYLOAD READY", state="complete")
            
            st.code(final, language="text")
            st.toast("Packet Injected Successfully")
        else:
            st.error("FATAL ERROR: NULL_INPUT_DETECTED")

with col2:
    st.subheader("🔬 DEEP_SPACE_DECRYPTION")
    cipher = st.text_area("PASTE INTERCEPTED DATA")
    
    if st.button("EXECUTE_DECODE_PROTOCOL"):
        if cipher:
            with st.spinner("Brute-forcing Unicode layers..."):
                time.sleep(1)
                result = decrypt(cipher)
                
            if result:
                st.markdown(f"""
                <div style="border: 2px solid #00FF41; padding: 20px; background: #001100;">
                    <p style="color: #00FF41; font-weight: bold;">[DECRYPTION_SUCCESS]</p>
                    <p style="font-size: 20px;">RAW_DATA: {result}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("NO HIDDEN SIGNATURES FOUND IN DATA STREAM")
        else:
            st.error("FATAL ERROR: DATA_STREAM_EMPTY")

st.markdown("---")
# Fake Log Feed
st.markdown("""
<div class='terminal-output'>
[SYSTEM LOGS]<br>
> Connection established to 127.0.0.1...<br>
> Layer 7 Steganography Active...<br>
> Status: <span style='color:red;'>STAY_ANONYMOUS</span>
</div>
""", unsafe_allow_html=True)
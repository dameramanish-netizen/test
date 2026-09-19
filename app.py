import streamlit as st

st.set_page_config(
    page_title="Infor LN Trace Debugger", page_icon="🔍", layout="wide"
)

# 1. Slider for Container Transparency inside the sidebar or appearance panel
# Let's assume the user sets a value from 0 to 100 for container opacity
container_opacity = st.slider("Container Opacity", 0, 100, 70) / 100.0
dim_opacity = (
    st.slider("Dim background", 0, 100, 45) / 100.0
)  # Background overlay opacity

# 2. Inject CSS using the Python variables for opacity
st.markdown(
    f"""
    <style>
    /* Force nature background image on the whole app */
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* Make inner wrappers transparent */
    .main, .stMain, [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}

    /* Dynamic Background Dim Overlay layer */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, {dim_opacity});
        z-index: 0;
        pointer-events: none;
    }}

    /* Dynamic Translucent Container controlled by the slider */
    .block-container {{
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, {container_opacity}) !important;
        padding: 2.5rem;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }}
    
    /* Ensure text readability */
    h1, h2, h3, p, label, span {{
        color: #1e293b !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Infor LN Trace Debugger")
st.caption("Search logs and inspect execution stacks")
st.markdown("---")

left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
  st.subheader("Trace setup")
  st.file_uploader("Upload trace file", type=["gz", "log", "txt"])
  st.text_input("Add keyword", placeholder="dal.handle.field.error")

with right_col:
  st.info("📁 **bshell.14724.gz**  |  128 matches  |  🟢 **Ready**")
  st.write("The background mountain scene will now dynamically fade through!")

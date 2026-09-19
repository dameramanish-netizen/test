import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Infor LN Trace Debugger", page_icon="🔍", layout="wide"
)

# 2. Two-Column Layout Setup & Controls (Placed early to capture slider value)
left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
  st.subheader("Trace setup")
  uploaded_file = st.file_uploader(
      "Upload trace file", type=["gz", "log", "txt"]
  )

  st.markdown("### Keywords")
  keyword = st.text_input("Add keyword", placeholder="dal.handle.field.error")

  st.markdown("### Filters")
  dal_filter = st.checkbox("DAL filter", value=True)
  depth_filter = st.checkbox("Depth filter", value=True)
  trim_timestamps = st.checkbox("Trim timestamps")

  if st.button("🚀 Analyze trace", type="primary", use_container_width=True):
    st.success("Analysis complete!")

  st.markdown("---")
  with st.expander("Appearance", expanded=True):
    # Capture slider value (0 to 100)
    dim_slider = st.slider("Dim background", 0, 100, 45)

# Calculate overlay opacity based on the slider (0.0 to 0.85)
overlay_opacity = dim_slider / 110.0

# 3. Dynamic CSS Injection using the Slider Value
st.markdown(
    f"""
    <style>
    /* Force the nature background image */
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

    /* Dynamic Dim Overlay layer */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, {overlay_opacity});
        z-index: 0;
        pointer-events: none;
    }}

    /* Make the main content boxes translucent (Glassmorphism effect) */
    .block-container {{
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.65) !important; /* Lower this number (e.g. 0.5) to make it more see-through */
        padding: 2.5rem;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }}
    
    /* Ensure text stays sharp and readable over the transparent background */
    h1, h2, h3, p, label, span {{
        color: #1e293b !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
# 4. Main Content Header & Right Column
with right_col:
  st.title("Infor LN Trace Debugger")
  st.caption("Search logs and inspect execution stacks")
  st.markdown("---")

  st.info(
      "📁 **bshell.14724.gz**  |  128 matches  |  🟢 **Ready**", icon="ℹ️"
  )

  tab1, tab2 = st.tabs(["Search results", "Call stack"])

  with tab2:
    st.markdown("##### Selected call")
    st.code(
        "dal.handle.field.error    Process 00029    Depth 12", language="text"
    )

    st.markdown("##### Call stack")
    stack_code = """
1 ---> (depth 6):  program.execute("tds350")
2      (depth 7):  process.order(order_id=450123)
3      (depth 8):  validate.order(order_id=450123)
4      (depth 9):  check.fields(table="tdsls", order_id=450123)
5      (depth 10): dal.field.get("tdsls.due_date")
6      (depth 11): dal.field.validate(value="")
7 ---> (depth 12): dal.handle.field.error(field="due_date", reason="mandatory", code="DAL-042")
    """.strip()

    st.code(stack_code, language="python")
    st.caption("Showing the reconstructed path to the selected call.")

  with tab1:
    st.write("Search results will appear here...")

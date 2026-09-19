import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Infor LN Trace Debugger", page_icon="🔍", layout="wide"
)

# 2. Custom CSS Injection for Background and Glassmorphism Effect
st.markdown(
    """
    <style>
    /* Set background image for the entire app (nature theme) */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Give the main content block a frosted glass look */
    .block-container {
        background: rgba(255, 255, 255, 0.88);
        padding: 2.5rem;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
    }
    
    /* Style headers and text for readability */
    h1, h2, h3, p, label {
        color: #1e293b !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Header Section
st.title("Infor LN Trace Debugger")
st.caption("Search logs and inspect execution stacks")
st.markdown("---")

# 4. Two-Column Layout
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
    with st.expander("Appearance"):
        st.slider("Dim background", 0, 100, 45)

with right_col:
    # Status Banner / File Info
    st.info(
        "📁 **bshell.14724.gz**  |  128 matches  |  🟢 **Ready**", icon="ℹ️"
    )

    # Tabs for navigation
    tab1, tab2 = st.tabs(["Search results", "Call stack"])

    with tab2:
        st.markdown("##### Selected call")
        st.code(
            "dal.handle.field.error    Process 00029    Depth 12",
            language="text",
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

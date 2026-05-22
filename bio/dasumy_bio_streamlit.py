import os
import base64
import streamlit as st

st.set_page_config(page_title="DaSuMy Music Bio", page_icon="🎵", layout="wide")

logo_path = "dasumy_logo.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_src = "data:image/png;base64," + base64.b64encode(f.read()).decode()
else:
    logo_src = "https://via.placeholder.com/260x260.png?text=DaSumy"

channel_icon_paths = ["dasumy_channel_icon.png", "dasumy_channel_icon.png.png"]
channel_icon_src = "https://img.icons8.com/color/256/youtube-play.png"
for path in channel_icon_paths:
    if os.path.exists(path):
        with open(path, "rb") as f:
            channel_icon_src = "data:image/png;base64," + base64.b64encode(f.read()).decode()
        break

PLAYLIST_URL = "https://www.youtube.com/watch?v=souGcWFKblM&list=PL2PFhA2YROwUztnpCbXmJCAXs-43gt9TI"
FACEBOOK_URL = "https://www.facebook.com/duy.pham.437330/?locale=vi_VN"

PRIMARY_COLOR = "224, 150, 131"
ACCENT_COLOR = "rgb(224,150,131)"
DOT_COLOR = "#f8b4a2"

st.markdown(f"""
<style>
:root {{
    --primary: {PRIMARY_COLOR};
    --accent: {ACCENT_COLOR};
    --accent-soft: rgba({PRIMARY_COLOR}, .12);
    --shadow: rgba(0, 0, 0, 0.22);
}}
html, body {{ background: #09090b; color: #f4f4f5; }}
[data-testid="stAppViewContainer"] {{ background: transparent; color: #f4f4f5; }}
.stApp {{ background: transparent; }}
body {{ overflow-x: hidden; }}
::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: #09090b; }}
::-webkit-scrollbar-thumb {{ background: #27272a; border-radius: 999px; }}
::-webkit-scrollbar-thumb:hover {{ background: #444; }}
.glass-panel {{
    background: rgba(15, 15, 20, 0.68) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    box-shadow: 0 24px 80px -48px var(--shadow) !important;
    backdrop-filter: blur(18px) !important;
    -webkit-backdrop-filter: blur(18px) !important;
    border-radius: 28px !important;
    padding: 2rem !important;
}}
.hero-shell {{
    position: relative;
    border-radius: 32px;
    overflow: hidden;
    padding: 3rem 2.5rem 2.5rem;
    background: linear-gradient(180deg, rgba(14,14,19,.96) 0%, rgba(14,14,19,.9) 100%);
    border: 1px solid rgba(255,255,255,0.08);
}}
.hero-shell::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top left, rgba({PRIMARY_COLOR},0.18), transparent 28%),
                radial-gradient(circle at bottom right, rgba(255,255,255,0.06), transparent 22%);
    pointer-events: none;
}}
.hero-shell > * {{ position: relative; z-index: 1; }}
.hero-title {{
    font-size: clamp(2.4rem, 4vw, 4.4rem);
    line-height: 1.02;
    font-weight: 800;
    letter-spacing: -0.05em;
    margin: 0;
    background: linear-gradient(90deg, rgba({PRIMARY_COLOR},1), rgba(255,255,255,0.88));
    -webkit-background-clip: text;
    color: transparent;
}}
.hero-subtitle {{
    margin-top: 0.85rem;
    font-size: 0.88rem;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: {ACCENT_COLOR};
}}
.hero-copy {{
    margin-top: 1.6rem;
    color: #c7c7d2;
    line-height: 1.85;
    font-size: 1rem;
}}
.big-cta {{
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    border-radius: 999px;
    padding: 0.95rem 1.5rem;
    background: rgb(224,150,131);
    color: #09090b;
    border: 1px solid rgba(255,255,255,0.1);
    font-weight: 700;
    text-decoration: none;
}}
.big-cta:hover {{ opacity: 0.95; transform: translateY(-1px); }}
.section-title {{
    font-size: 0.86rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 1rem;
}}
.card-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
}}
.card-grid.sm {{ grid-template-columns: repeat(1, minmax(0, 1fr)); }}
.link-card {{
    display: block;
    padding: 1.25rem 1.35rem;
    border-radius: 22px;
    text-decoration: none;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 18px 40px -28px var(--shadow);
    transition: transform 0.2s ease, border-color 0.2s ease;
    background: rgba(255,255,255,0.02);
}}
.link-card:hover {{ transform: translateY(-2px); border-color: rgba(var(--primary),0.24); }}
.link-card-title {{ font-size: 1rem; font-weight: 700; margin: 0 0 0.35rem; color: #f4f4f5; }}
.link-card-desc {{ margin: 0; color: #b9bdc9; font-size: 0.92rem; }}
.stButton>button {{ border-radius: 18px; padding: 0.96rem 1.2rem; font-weight: 700; }}
.stTextArea>div>div>textarea, .stTextInput>div>div>input {{ background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(255,255,255,0.12) !important; color: #f4f4f5 !important; border-radius: 16px !important; padding: 1rem !important; }}
.stTextArea>div>label, .stTextInput>label {{ color: #f4f4f5 !important; }}
</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <section class="glass-panel hero-shell">
        <div style="display:flex; align-items:center; gap:1.25rem; flex-wrap:wrap; justify-content:space-between;">
            <div style="max-width: 640px;">
                <div style="display:inline-flex; gap:0.6rem; align-items:center; background: rgba(224,150,131,0.12); border: 1px solid rgba(255,255,255,0.08); padding: 0.8rem 1rem; border-radius: 999px; color: #f4f4f5; font-size: 0.85rem; letter-spacing: 0.12em; text-transform: uppercase;">
                    <span style="width:0.65rem; height:0.65rem; background: #f8b4a2; border-radius: 999px; display:inline-block;"></span>
                    LIVE NOW
                </div>
                <h1 class="hero-title">DASUMY</h1>
                <p class="hero-subtitle">Lo-fi & Chillhop Music</p>
                <p class="hero-copy">🎧 Không gian âm nhạc nhẹ nhàng, mộc mạc và thư giãn. Hãy dừng chân, đeo tai nghe và thả hồn theo những giai điệu của DaSumy.</p>
                <a class="big-cta" href="https://www.youtube.com/@DaSuMyMusic" target="_blank">▶ Ghé kênh YouTube</a>
                <p style="margin-top: 1rem; color: #c7c7d2;">Hoặc kết nối với mình trên <a href="{FACEBOOK_URL}" target="_blank" style="color: rgb(224,150,131); text-decoration: none;">Facebook</a>.</p>
            </div>
            <div style="width: 260px; height: 260px; border-radius: 28px; overflow:hidden; border: 1px solid rgba(255,255,255,0.08); box-shadow: 0 20px 60px -40px var(--shadow); background: rgba(255,255,255,0.03);">
                <img src="{channel_icon_src}" alt="DaSumy YouTube channel logo" style="width:100%; height:100%; object-fit: cover; display:block;">
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.container():
    left, right = st.columns([2, 1], gap="large")
    with left:
        st.markdown("<div class='section-title'>Trình nghe nhạc</div>", unsafe_allow_html=True)
        st.video(PLAYLIST_URL)
        st.markdown(
            """
            <div class="glass-panel" style="margin-top: 1.5rem;">
                <div class="section-title">Playlist từ kênh YouTube</div>
                <p style="color: #c7c7d2; margin: 0;">Nghe playlist chính thức của kênh DaSumy ngay tại đây.</p>
                <p style="margin-top: 1rem;"><a href="https://www.youtube.com/playlist?list=PL2PFhA2YROwUztnpCbXmJCAXs-43gt9TI" target="_blank" style="color: rgb(224,150,131); text-decoration: none;">Mở playlist trên YouTube</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown("<div class='section-title'>Gửi yêu cầu hợp tác</div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class='glass-panel' style='padding:1rem 1.25rem;'>
                <p style='margin:0 0 0.75rem; color:#c7c7d2;'>Nhấn vào link để kết nối trực tiếp với Facebook của mình.</p>
                <a href='{FACEBOOK_URL}' target='_blank' style='display:inline-block; color: rgb(224,150,131); text-decoration:none; font-weight:700;'>Facebook: duy.pham.437330</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.form("contact_form"):
            name = st.text_input("Tên của bạn")
            email = st.text_input("Email liên hệ")
            message = st.text_area("Lời nhắn hoặc yêu cầu mua beat")
            submitted = st.form_submit_button("Gửi tin nhắn")
            if submitted:
                st.success("Gửi lời nhắn thành công! Mình sẽ liên hệ lại sớm 📨")

st.markdown(
    """
    <div class="glass-panel" style="text-align:center; margin-top: 1.5rem;">
        <p style="margin: 0; color: #8b8b9a; font-size: 0.9rem;">Thank you for listening ✨</p>
        <p style="margin: 0.35rem 0 0; color: #656571; font-size: 0.82rem;">© 2026 DASUMY. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

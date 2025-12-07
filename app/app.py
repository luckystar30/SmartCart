import streamlit as st
import pandas as pd
from pathlib import Path
import ast
from datetime import datetime

# ----------------------------
# 🎨 PAGE CONFIGURATION
# ----------------------------
st.set_page_config(
    page_title="🛒 Personalized E-Commerce Recommendations",
    page_icon="🛍️",
    layout="wide",
)

# ----------------------------
# 💅 CUSTOM CSS
# ----------------------------
st.markdown("""
<style>
.stApp { background: linear-gradient(to right, #0f2027, #203a43, #2c5364); color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
[data-testid="stSidebar"] { background-color: #1c1c1c; color: #f0f0f0; }
h1, h2, h3, h4 { color: #f8f9fa !important; }
.recommend-card { background: linear-gradient(145deg, #1e1e1e, #2c2c2c); border-radius: 20px; padding: 25px; margin: 15px 0; box-shadow: 0px 8px 20px rgba(0,0,0,0.5); transition: transform 0.3s ease, box-shadow 0.3s ease; }
.recommend-card:hover { transform: scale(1.03); box-shadow: 0px 12px 28px rgba(0,0,0,0.6); }
.top-product { background-color: #2a2a2a; border-left: 5px solid #00e676; padding: 5px 10px; margin-bottom: 5px; border-radius: 8px; font-weight: bold; color: #ffffff; }
.hot-deal { color: #ff4d4d; font-weight: bold; margin-left: 5px; }
.promo-text { font-size: 1rem; color: #fffa90; font-weight: bold; margin-top: 15px; }
.stSelectbox label { font-size: 1.1rem; color: #00c4cc; }
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# 📂 LOAD DATA
# ----------------------------
data_path = Path("data/final_recommendations_with_promos.csv")

st.title("🛍️ Personalized E-Commerce Recommendations")
st.markdown("### 🎯 Discover products tailored just for you!")

# ----------------------------
# Dynamic greeting
# ----------------------------
def get_greeting(user_id):
    now = datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        greeting = f"Good morning, User {user_id}! ☀️"
    elif 12 <= hour < 17:
        greeting = f"Good afternoon, User {user_id}! 🌤️"
    elif 17 <= hour < 21:
        greeting = f"Good evening, User {user_id}! 🌙"
    else:
        greeting = f"Hello, User {user_id}! 🌙"
    month = now.month
    if month == 12: greeting += " 🎄 Holiday specials for you!"
    elif month == 10: greeting += " 🎃 Spooky deals for Halloween!"
    return greeting

# ----------------------------
if data_path.exists():
    df = pd.read_csv(data_path)
    df.columns = [col.strip().replace("'", "").replace('"', '') for col in df.columns]

    try:
        df['UserID'] = df['UserID'].astype(int)
        user_ids = sorted(df['UserID'].unique().tolist())
    except:
        user_ids = sorted(df['UserID'].unique().tolist())

    st.sidebar.header("🔍 Filters")
    selected_user = st.sidebar.selectbox("Select a User ID:", user_ids)

    user_data = df[df['UserID'] == selected_user]

    if not user_data.empty:
        products_string = user_data['RecommendedProducts'].values[0]
        try:
            products_list = ast.literal_eval(products_string)
        except:
            products_list = [products_string]

        greeting_message = get_greeting(selected_user)

        if products_list:
            if len(products_list) <= 3:
                product_text = ", ".join(products_list)
            else:
                product_text = ", ".join(products_list[:3]) + ", and more!"
            promo_message = f"{greeting_message} Check out these awesome products: {product_text}"
        else:
            promo_message = f"{greeting_message} Check out our top picks!"

        st.markdown(f"## 🧾 Recommendations for **User {selected_user}**")
        st.markdown(f'<div class="promo-text">{promo_message}</div>', unsafe_allow_html=True)

        # Build products HTML with top 3 + hot-deal
        products_html = ""
        for idx, product in enumerate(products_list):
            top_class = "top-product" if idx < 3 else ""
            hot_deal = '<span class="hot-deal">🔥 Hot Deal</span>' if idx < 3 else ""
            products_html += f'<div class="{top_class}">{product}{hot_deal}</div>'

        st.markdown(f'<div class="recommend-card">{products_html}</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ No recommendations found for this user.")

else:
    st.error(f"❌ Data file not found at: `{data_path}`")
    st.info("Please make sure the CSV file is inside the `/data` folder.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<div style='text-align: center; margin-top: 50px; color: #ccc; font-size: 0.9rem;'>
Built with ❤️ using <b>Streamlit</b> — Data auto-refreshes from CSV 💾
</div>
""", unsafe_allow_html=True)

🛒 **SmartCart – Personalized E-Commerce Recommendation Engine**

**AI-powered product recommendations + LLM-generated promo messages + interactive Streamlit dashboard**

👉 **Live App:**
https://smartcart-dkkyrbzvk6pbc2q5qxjhjs.streamlit.app/

🌟 **Overview**

SmartCart is an intelligent e-commerce recommendation system that blends:

- **Collaborative Filtering (CF) to learn user-item interactions**

- **LLM-based semantic embeddings to understand product meaning**

- **RFM segmentation + clustering to profile customer behavior**

- **AI-generated promotional messages personalized per user**

- **A modern Streamlit dashboard to explore recommendations visually**

This hybrid design improves personalization, enhances product discovery, and supports marketing automation.

✨ **Key Features**

🔮 **Personalized Product Recommendations**

- Suggestions adapt to the selected user ID

- Hybrid scoring combines behavior + semantic similarity

- “Hot Deal” badges highlight relevant promotions

✉️ **AI-Generated Promotional Messages**

- Dynamic greetings (ex: "Good evening, User 0 ✨")

- Themed promos based on seasons or user behavior

- LLM generates smart, context-aware product mentions

🎯 **Streamlit-Based Interactive Dashboard**

- Sleek dark-themed UI

- Sidebar to select user IDs

- Clear visualization of top 3 product recommendations

- Footer displaying data source and auto-refresh behavior

📊 **Customer Segmentation (Backend)**

- **RFM scoring identifies:**

    - Loyal customers

    - At-risk users

    - New shoppers

- Behavioral clusters guide personalized promotions

🧠 **Hybrid Recommendation Engine**

SmartCart merges two intelligence layers:

**Component**	                    **Purpose**
Collaborative Filtering (CF)	Learns interactions between users + items
Semantic Embeddings	            Understands product descriptions with LLM embeddings
Hybrid Score	                Combines both for highly accurate recommendations

This results in a **~30% improvement** over using CF alone.

🏗️ **Architecture**
Transaction Data → Cleaning → CF Model
                     ↘
      Product Descriptions → Embeddings → Hybrid Engine
                                              ↓
                                     Streamlit App → User

🧰 **Tech Stack**

**Languages**

Python

**Libraries**

- Streamlit

- Pandas, NumPy

- scikit-learn

- Surprise (SVD/KNN CF models)

- SentenceTransformers (HuggingFace)

- KMeans (segmentation)

**Deployment**

- Streamlit Cloud

📂 **Project Structure**

SmartCart/
│
├── app/
│   └── app.py                     # Main Streamlit UI
│
├── data/
│   └── final_recommendations_with_promos.csv
│
├── notebooks/                     # EDA, RFM, CF, embeddings
│
├── fix_headers.py
├── requirements.txt
├── SmartCart_Desc.docx            # Full project documentation
├── PLAN.docx
└── .gitignore

🚀 **Run Locally**

1️⃣ **Clone the repository**
git clone https://github.com/luckystar30/SmartCart.git
cd SmartCart

2️⃣ **Create and activate a virtual environment**(Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

3️⃣ **Install required dependencies**
pip install -r requirements.txt

4️⃣ **Launch the Streamlit app**
streamlit run app/app.py

🌐 **Live Deployment**

Your app is deployed and accessible here:

👉 https://smartcart-dkkyrbzvk6pbc2q5qxjhjs.streamlit.app/

Hosted via **Streamlit Cloud**, the app refreshes dynamically and loads all recommendations directly from the processed dataset.

📊 **Evaluation Summary**

- CF model evaluated using RMSE and precision@k

- Hybrid CF + embeddings improved precision by ~30%

- LLM messages reviewed for relevance and fluency

- Dashboard validated across multiple user scenarios

💡 **Future Enhancements**

- Real-time recommendation updates

- User authentication

- A/B testing for promotional message impact

- Integration with live e-commerce APIs

🤝 **Contributing**

Contributions are welcome!
Feel free to fork, open issues, or submit pull requests.

📄 **License**

MIT License (recommended)


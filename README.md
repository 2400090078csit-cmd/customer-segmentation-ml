# 📊 Customer Segmentation & Marketing Analytics

An interactive Machine Learning dashboard that analyzes customer behavior and groups customers into meaningful segments using **K-Means Clustering**.

## 🌐 Live Demo

🚀 [Open Customer Segmentation & Marketing Analytics](https://customer-segmentation-ml-khxtb44kbozjha5ghwuxkq.streamlit.app/)

## 🚀 Features

* 📋 Customer dataset visualization
* 📈 Exploratory Data Analysis
* 👥 Age and customer behavior analysis
* 💰 Annual Income analysis
* 🛍️ Spending Score analysis
* 📉 Elbow Method for selecting K
* 🤖 K-Means clustering
* ⚖️ Feature scaling using StandardScaler
* 📊 Silhouette Score evaluation
* 🎚️ Interactive K selection
* 🎯 Customer segment classification
* 💡 Marketing recommendations
* 🔍 Customer segment filtering
* 📥 Download clustered customer data

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Streamlit**
* **Plotly**

## 🤖 Machine Learning

The project uses **K-Means Clustering** to group customers based on their characteristics and spending behavior.

The clustering can use:

* Age
* Annual Income
* Spending Score

### Model Evaluation

The project uses:

* **StandardScaler** for feature scaling
* **Elbow Method** to analyze suitable values of K
* **Silhouette Score** to evaluate cluster quality
* **K-Means Clustering** to create customer groups

## 📊 Customer Segments

The application provides business-oriented customer insights such as:

* 💎 **Premium Customers**
* 🎯 **Potential Customers**
* 🛍️ **Value Customers**
* 📉 **Low Engagement Customers**

Each segment is associated with suitable marketing recommendations.

## 💡 Marketing Insights

The dashboard provides recommendations such as:

* Loyalty rewards for high-value customers
* Personalized offers for potential customers
* Affordable products and combo offers for value customers
* Promotional campaigns for low-engagement customers

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/2400090078csit-cmd/customer-segmentation-ml.git
```

### 2. Open the project folder

```bash
cd customer-segmentation-ml
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
customer-segmentation-ml
│
├── data
│   └── Mall_Customers.csv
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📈 Dataset

The project uses the **Mall Customers dataset**, which contains customer information including:

* Customer ID
* Gender
* Age
* Annual Income
* Spending Score

## 🎯 Future Improvements

* Upload custom customer datasets
* Automatic optimal K recommendation
* Advanced customer lifetime value analysis
* Interactive Plotly visualizations
* Additional customer behavior analysis
* Cloud deployment improvements

## 👩‍💻 Project

**Customer Segmentation & Marketing Analytics**

Built using Python, Machine Learning and Streamlit.

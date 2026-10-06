import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

df = pd.read_csv("data/Mall_Customers.csv")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Model Settings")

st.sidebar.write("Choose the settings for customer segmentation.")

feature_options = [
    "Age",
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

selected_features = st.sidebar.multiselect(
    "Select features for clustering",
    feature_options,
    default=[
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
)

k = st.sidebar.slider(
    "Number of Clusters (K)",
    min_value=3,
    max_value=6,
    value=5
)

st.sidebar.markdown("---")

st.sidebar.info(
    "K-Means groups customers with similar characteristics "
    "based on the selected features."
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Customer Segmentation & Marketing Analytics")

st.write(
    "An interactive machine learning dashboard for analyzing "
    "customer behavior and generating marketing insights."
)

# --------------------------------------------------
# CHECK FEATURES
# --------------------------------------------------

if len(selected_features) < 2:

    st.warning(
        "Please select at least 2 features for clustering."
    )

    st.stop()

# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        len(df)
    )

with col2:
    st.metric(
        "Average Age",
        round(df["Age"].mean(), 1)
    )

with col3:
    st.metric(
        "Average Income",
        round(df["Annual Income (k$)"].mean(), 1)
    )

with col4:
    st.metric(
        "Average Spending",
        round(
            df["Spending Score (1-100)"].mean(),
            1
        )
    )

# --------------------------------------------------
# DATASET
# --------------------------------------------------

st.subheader("📋 Customer Dataset")

st.dataframe(
    df,
    use_container_width=True
)

# --------------------------------------------------
# EDA
# --------------------------------------------------

st.subheader("📈 Exploratory Data Analysis")

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots()

    ax.hist(
        df["Age"],
        bins=10
    )

    ax.set_title("Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Customers")

    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots()

    ax.hist(
        df["Spending Score (1-100)"],
        bins=10
    )

    ax.set_title("Spending Score Distribution")
    ax.set_xlabel("Spending Score")
    ax.set_ylabel("Customers")

    st.pyplot(fig)

# --------------------------------------------------
# FEATURE SCALING
# --------------------------------------------------

X = df[selected_features]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# --------------------------------------------------
# ELBOW METHOD
# --------------------------------------------------

st.subheader("📉 Elbow Method")

wcss = []

for k_value in range(2, 11):

    model = KMeans(
        n_clusters=k_value,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    wcss.append(model.inertia_)

fig, ax = plt.subplots()

ax.plot(
    range(2, 11),
    wcss,
    marker="o"
)

ax.set_title("Elbow Method")
ax.set_xlabel("Number of Clusters")
ax.set_ylabel("WCSS")

st.pyplot(fig)

# --------------------------------------------------
# K-MEANS
# --------------------------------------------------

st.subheader("🤖 K-Means Customer Segmentation")

model = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X_scaled)

# --------------------------------------------------
# SILHOUETTE SCORE
# --------------------------------------------------

score = silhouette_score(
    X_scaled,
    df["Cluster"]
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Selected K",
        k
    )

with col2:

    st.metric(
        "Silhouette Score",
        round(score, 3)
    )

# --------------------------------------------------
# CLUSTER VISUALIZATION
# --------------------------------------------------

st.subheader("🎯 Customer Clusters")

if (
    "Annual Income (k$)" in selected_features
    and
    "Spending Score (1-100)" in selected_features
):

    fig, ax = plt.subplots()

    for cluster in range(k):

        cluster_data = df[
            df["Cluster"] == cluster
        ]

        ax.scatter(
            cluster_data["Annual Income (k$)"],
            cluster_data["Spending Score (1-100)"],
            label=f"Cluster {cluster + 1}"
        )

    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score")
    ax.set_title("Customer Segmentation")

    ax.legend()

    st.pyplot(fig)

else:

    st.info(
        "The scatter plot is displayed when Annual Income "
        "and Spending Score are selected together."
    )

# --------------------------------------------------
# CLUSTER SUMMARY
# --------------------------------------------------

st.subheader("📊 Cluster Summary")

cluster_summary = df.groupby("Cluster").agg(
    Customers=("CustomerID", "count"),
    Average_Age=("Age", "mean"),
    Average_Income=("Annual Income (k$)", "mean"),
    Average_Spending=("Spending Score (1-100)", "mean")
).round(2)

st.dataframe(
    cluster_summary,
    use_container_width=True
)

# --------------------------------------------------
# CUSTOMER SEGMENT LABELS
# --------------------------------------------------

st.subheader("🎯 Customer Segment Analysis")

overall_income = df["Annual Income (k$)"].mean()
overall_spending = df["Spending Score (1-100)"].mean()

segment_names = {}
strategies = {}

for cluster in range(k):

    cluster_data = df[
        df["Cluster"] == cluster
    ]

    income = cluster_data[
        "Annual Income (k$)"
    ].mean()

    spending = cluster_data[
        "Spending Score (1-100)"
    ].mean()

    if (
        income >= overall_income
        and
        spending >= overall_spending
    ):

        segment_names[cluster] = "Premium Customers"

        strategies[cluster] = (
            "Offer loyalty rewards, premium products, "
            "exclusive memberships and personalized offers."
        )

    elif (
        income >= overall_income
        and
        spending < overall_spending
    ):

        segment_names[cluster] = "Potential Customers"

        strategies[cluster] = (
            "Use personalized recommendations, discounts "
            "and targeted campaigns to increase spending."
        )

    elif (
        income < overall_income
        and
        spending >= overall_spending
    ):

        segment_names[cluster] = "Value Customers"

        strategies[cluster] = (
            "Promote affordable products, combo offers "
            "and seasonal discounts."
        )

    else:

        segment_names[cluster] = "Low Engagement Customers"

        strategies[cluster] = (
            "Use low-cost promotions, awareness campaigns "
            "and special introductory offers."
        )

df["Customer Segment"] = df[
    "Cluster"
].map(segment_names)

# --------------------------------------------------
# SEGMENT DISTRIBUTION
# --------------------------------------------------

st.subheader("📊 Customer Segment Distribution")

segment_counts = df[
    "Customer Segment"
].value_counts()

fig, ax = plt.subplots()

ax.bar(
    segment_counts.index,
    segment_counts.values
)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Customers")
ax.set_title("Customers by Segment")

plt.xticks(
    rotation=20,
    ha="right"
)

st.pyplot(fig)

# --------------------------------------------------
# SEGMENT FILTER
# --------------------------------------------------

st.subheader("🔍 Explore Customer Segments")

selected_segment = st.selectbox(
    "Select a segment",
    ["All Segments"]
    + sorted(
        df["Customer Segment"].unique()
    )
)

if selected_segment == "All Segments":

    filtered_df = df

else:

    filtered_df = df[
        df["Customer Segment"]
        == selected_segment
    ]

st.dataframe(
    filtered_df,
    use_container_width=True
)

# --------------------------------------------------
# MARKETING RECOMMENDATIONS
# --------------------------------------------------

st.subheader("💡 Marketing Recommendations")

for cluster in range(k):

    st.markdown(
        f"### 🏷️ {segment_names[cluster]}"
    )

    st.write(
        strategies[cluster]
    )

# --------------------------------------------------
# DOWNLOAD
# --------------------------------------------------

st.subheader("📥 Download Results")

csv_data = df.to_csv(
    index=False
)

st.download_button(
    label="Download Clustered Customer Data",
    data=csv_data,
    file_name="customer_segments.csv",
    mime="text/csv"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Customer Segmentation & Marketing Analytics | "
    "Python • Pandas • Scikit-learn • Streamlit"
)
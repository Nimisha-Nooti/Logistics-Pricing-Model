# 📊 **Logistics Pricing Optimization Model** 

##**Overview:** This machine learning model predicts freight shipping rates by identifying patterns across various shipping conditions. It helps logistics managers automate invoice validation and uncover hidden cost drivers.

##**🔎 Key Components**
- **Model Type:** Random Forest Regressor (an ensemble machine learning algorithm that combines multiple decision trees to prevent overfitting and ensure reliable price predictions).
- **Target Variable:** Actual_Price_USD (the final invoice cost of the shipment).

##**📈 Structural Cost Factors**
The model analyzes two main types of inputs to calculate a delivery price:
1. **Core Numerical MetricsDistance (Miles):** The physical length of the haul route.
   - **Weight (Lbs):** The physical size and load impact of the cargo.
   - **Lead Time (Days):** How far in advance the shipment was booked.
   - **Fuel Surcharge Rate:** Floating energy cost indexing adjustments.
   - **Urgency Flag:** Priority express shipping status.
2. **Categorical Operational Slicers**
   - **Origin / Destination:** Regional geographical shipping hubs.
   - **Transport Mode:** Fleet classification (Air Freight, Truckload, or Less-Than-Truckload).
   - **Carrier:** The specific shipping company handling the transit.
##💡 **Automated Data Pipeline Features**
- **Robust Cleaning:** The model automatically replaces corrupt spatial entries (like -999 mileage errors) and fills missing load parameters using localized statistical values.
- **One-Hot Encoding:** It instantly translates textual data (like city names or carrier names) into mathematical structures that the machine learning engine can understand.

# 🚚 Optimization Engine Work Flow

This flowchart outlines the complete end-to-end data pipeline, machine learning workflow, and interactive dashboard deployment architecture for the project. 

Copy and paste the markdown block below directly into your GitHub `README.md` file. GitHub will automatically render it as a visual diagram using its native **Mermaid** support.

```mermaid
graph TD
    %% Styling Configuration with Fixed Dark Font Colors
    classDef source fill:#EBF5FB,stroke:#2E86C1,stroke-width:2px,color:#000000;
    classDef cleaning fill:#FEF9E7,stroke:#D4AC0D,stroke-width:2px,color:#000000;
    classDef pipeline fill:#EAFAF1,stroke:#27AE60,stroke-width:2px,color:#000000;
    classDef training fill:#FBEEE6,stroke:#CB4335,stroke-width:2px,color:#000000;
    classDef deploy fill:#F4ECF7,stroke:#8E44AD,stroke-width:2px,color:#000000;

    %% Phase 1: Data Ingestion
    subgraph Phase 1: Data Sources & Inputs
        A[logistics_pricing_dataset.csv]:::source --> B[Load DataFrame via Pandas]:::source
    end

    %% Phase 2: Data Cleaning
    subgraph Phase 2: Preprocessing Pipeline
        B --> C{Detect Corrupt Data?}:::cleaning
        C -- Yes --> D[Replace -999 Outliers with NaN]:::cleaning
        C -- No --> E[Split Matrix: Features & Target]:::cleaning
        D --> E
        E --> F[Scikit-Learn ColumnTransformer]:::pipeline
        F --> G[Numerical Pipeline: Median Imputer]:::pipeline
        F --> H[Categorical Pipeline: One-Hot Encoder]:::pipeline
    end

    %% Phase 3: Model Training
    subgraph Phase 3: Machine Learning Engine
        G --> I[Combine Transformations]:::training
        H --> I
        I --> J[Train-Test Split 80/20]:::training
        J --> K[Random Forest Regressor Fit]:::training
        K --> L[Evaluate Metrics: R² & MAE Score]:::training
    end

    %% Phase 4: Integration & Deployment
    subgraph Phase 4: Output & Streamlit UI
        K --> M[Generate Predictions on Full Dataset]:::deploy
        M --> N[Export dashboard_pricing_data.csv]:::deploy
        N --> O[Streamlit Web App app.py]:::deploy
        O --> P[Interactive Sidebar Slicers & Filters]:::deploy
        O --> Q[Plotly Performance Scatter Visualizations]:::deploy
    end

    %% Section Links
    class A,B source;
    class C,D cleaning;
    class E,F,G,H pipeline;
    class I,J,K,L training;
    class M,N,O,P,Q deploy;


```

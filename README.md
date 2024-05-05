# Financial Services Innovation Lab, Georgia Tech [TASK] - RAG App for Interpreting SEC-EDGAR Findings :bar_chart:

This repository contains a Retrieval-Augmented Generation application designed to interpret SEC-EDGAR findings efficiently. Using Large Language Models technologies, it extracts, processes, and analyzes financial documents to provide actionable insights.

**LOCAL DEMO OF APP :calling:** - https://drive.google.com/file/d/1We6an1R797MVolu2NFSzFG2u9j2faNEf/view?usp=sharing

## Tech Stack Used :page_facing_up:
- **Python Programming**: The core programming language powering the application.
- **Gemini-pro LLM API**: Interfaces with LLMs to implement RAG for insightful response generation.
- **Seaborn (sns) plots**: Enhances data visualization, providing clear, insightful charts.
- **Streamlit**: Simplifies application deployment and provides an interactive user interface.

## PIPELINE :page_facing_up:
1. **Data Extraction**: Extracts financial data from SEC-EDGAR documents.
2. **Data Cleaning**: Prepares the extracted data by cleaning and preprocessing.
3. **Integrating LLM API for RAG**: Interfaces with the Gemini-pro API to generate relevant responses.
4. **Response Generation**: Produces comprehensive responses to interpret SEC-EDGAR findings.
5. **Deploy**: Makes the application available for real-time use via Streamlit.
6. **Interpret and Visualize**: Presents data in a clear, easy-to-understand format using Seaborn.

![image](https://github.com/ShubhMittal44/Georgia-Tech-Work/assets/76169253/4877d4e1-01f8-4272-ad2d-c3b8ac83b63f)

## **Backend Workflow 📂**

1. **Data Acquisition:**
   - **Navigate to `Data Integration`:** Start by extracting raw data from SEC 10-K filings.
   - **Run `Data Extraction.py`:** This script processes and aggregates essential data.

2. **Normalization and Cleaning:**
   - **Run `zip_to_text_report_extractor.py`:** Normalize and convert data into a structured, ready-to-analyze format.

3. **Create Embeddings:**
   - **Execute `loader.py`:** Segment and generate embeddings for faster retrieval.

4. **Query with Gemini:**
   - **Run `app_main.py`:** Query and analyze the data using the Gemini model.

5. **Visualization:**
   - **Execute `visualizer.py`:** Load visualizations and interactively explore the results.


## **Example Outputs 📊**

1. **Segment Revenue Analysis for IBM**
   **Prompt:** *How do the revenues of IBM's different segments (Technology, Personal Systems, Global Financing) compare, and what are their growth trends over the years 2019, 2020, and 2021?*
  ![image](https://github.com/ShubhMittal44/Georgia-Tech-Work/assets/76169253/90ea123a-4ad2-4879-8382-80f8b31f271a) ![image](https://github.com/ShubhMittal44/Georgia-Tech-Work/assets/76169253/9e1ae0f2-0c03-43b3-bd7d-4a4bfbece238)

   See how IBM's revenues change across different business segments. By creating a bar chart or stacked bar graph that compares revenues across segments (Technology, Personal Systems, Global Financing, etc.) over several fiscal years, stakeholders can visually identify which segments are driving growth and which are stagnating or declining. This visualization helps management identify potential opportunities or challenges. For example, the "Technology" and "Personal Systems" segments show steady growth, which management can leverage to expand investments, while "Global Financing" remains comparatively flat.

2. **R&D Investment Trends for NVIDIA**
   **Prompt:** *How does NVIDIA's R&D spending correlate with revenue generation across the years 2019, 2020, and the year 2021? Give a proper tabular answer.*
   ![image](https://github.com/ShubhMittal44/Georgia-Tech-Work/assets/76169253/02296a1e-332c-44ce-9e6a-02af08bf2b6b)
 
   The consistent increase in R&D spending reflects NVIDIA's focus on innovation and developing competitive technology. Despite a rise in R&D expenses, overall revenue has increased, indicating that investments are translating into improved products and market performance.

3. **Geographic Market Share Analysis for AMAZON**
   **Prompt:** *How does Amazon's market share vary across different geographic regions, and what does it indicate about regional strategies? Give the required visualizations.*
   ![image](https://github.com/ShubhMittal44/Georgia-Tech-Work/assets/76169253/ae6bb115-5c57-4939-a3d6-c5918d267a8b)

   Amazon's largest market, North America, continues to generate significant revenue growth due to strategic marketing, a strong logistics network, and Prime membership expansion. Europe exhibits steady growth but at a slower pace, emphasizing the need for improved localization and compliance with regional regulations. Meanwhile, Asia and other regions present rising growth potential, which can be harnessed through increased investments in logistics, cloud computing, and strategic partnerships tailored to local markets.


## Getting Started :key:
To get started, clone the repository. Make sure you have the required dependencies installed for smooth execution.


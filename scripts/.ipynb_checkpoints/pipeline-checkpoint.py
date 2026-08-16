"""
Automated data pipeline for e-commerce sales analysis.
Task 5 - Final Report, Automation & Presentation - ApexPlanet Internship
Loads raw data, cleans it, calculates KPIs, and exports results.
"""
import pandas as pd
import numpy as np
import os
from datetime import datetime
def load_data(filepath):
    """Load raw dataset from CSV or Excel."""
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")
    print(f"Loaded {len(df)} rows from {filepath}")
    return df
def clean_data(df):
    """Clean the dataset: remove junk columns, handle missing values, fix dtypes."""
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.drop_duplicates()
    if 'Postal Code' in df.columns:
        df['Postal Code'] = df['Postal Code'].fillna(0)
    for date_col in ['Order Date', 'Ship Date']:
        if date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce', dayfirst=True)
    print(f"Cleaned data: {len(df)} rows remaining")
    return df
def calculate_kpis(df):
    """Calculate key business KPIs from the cleaned dataset."""
    kpis = {
        'Total Sales': df['Sales'].sum(),
        'Total Profit': df['Profit'].sum(),
        'Total Orders': df['Order ID'].nunique(),
        'Total Customers': df['Customer ID'].nunique(),
        'Average Order Value': df['Sales'].mean(),
        'Average Profit Margin (%)': (df['Profit'].sum() / df['Sales'].sum()) * 100,
        'Top Category': df.groupby('Category')['Sales'].sum().idxmax(),
        'Top Region (by Profit)': df.groupby('Region')['Profit'].sum().idxmax(),
    }
    kpi_df = pd.DataFrame(list(kpis.items()), columns=['KPI', 'Value'])
    return kpi_df
def export_results(df, kpi_df, output_dir='data'):
    """Save cleaned data and KPIs to Excel."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    excel_path = os.path.join(output_dir, f'pipeline_output_{timestamp}.xlsx')
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Cleaned Data', index=False)
        kpi_df.to_excel(writer, sheet_name='KPIs', index=False)
    print(f"Results exported to {excel_path}")
    return excel_path
def run_pipeline(input_filepath, output_dir='data'):
    """Run the full pipeline end-to-end."""
    print("=" * 50)
    print("Starting data pipeline...")
    print("=" * 50)
    df = load_data(input_filepath)
    df_clean = clean_data(df)
    kpi_df = calculate_kpis(df_clean)
    output_path = export_results(df_clean, kpi_df, output_dir)
    print("=" * 50)
    print("Pipeline completed successfully!")
    print("=" * 50)
    print("\nKey KPIs:")
    print(kpi_df.to_string(index=False))
    return df_clean, kpi_df
if __name__ == "__main__":
    run_pipeline(input_filepath='data/ecomm_data_cleaned.csv', output_dir='data')

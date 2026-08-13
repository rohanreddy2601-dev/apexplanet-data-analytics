"""
Reusable database utility functions for the e-commerce SQLite database.
Task 2 - SQL for Data Extraction - ApexPlanet Internship
"""

import pandas as pd
import sqlite3


def get_connection(db_path='data/ecommerce.db'):
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(db_path)


def run_query(query, db_path='data/ecommerce.db'):
    """Run a SQL query and return the result as a pandas DataFrame."""
    conn = get_connection(db_path)
    try:
        result = pd.read_sql(query, conn)
    finally:
        conn.close()
    return result


def load_csv_to_db(csv_path, table_name, db_path='data/ecommerce.db'):
    """Load a CSV file into a SQLite table."""
    df = pd.read_csv(csv_path)
    conn = get_connection(db_path)
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Loaded {len(df)} rows into table '{table_name}'")
    finally:
        conn.close()


def get_top_n(table, column, n=10, order='DESC', db_path='data/ecommerce.db'):
    """Get the top N rows from a table ordered by a specific column."""
    query = f'SELECT * FROM {table} ORDER BY "{column}" {order} LIMIT {n};'
    return run_query(query, db_path)


def get_summary_by_group(table, group_col, agg_col, agg_func='SUM', db_path='data/ecommerce.db'):
    """Get an aggregated summary grouped by a column."""
    query = f'''
    SELECT "{group_col}", {agg_func}("{agg_col}") AS result
    FROM {table}
    GROUP BY "{group_col}"
    ORDER BY result DESC;
    '''
    return run_query(query, db_path)


# Example usage (only runs if this file is executed directly, not imported)
if __name__ == "__main__":
    result = get_summary_by_group('orders', 'Category', 'Sales')
    print(result)
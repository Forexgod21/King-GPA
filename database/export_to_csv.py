#!/usr/bin/env python3
"""
SQLite to CSV Export
Exports all tables from the vet clinic SQLite database to CSV files
These CSV files can then be imported into Microsoft Access

Usage:
    python3 database/export_to_csv.py
"""

import sqlite3
import csv
import os
from pathlib import Path

def export_sqlite_to_csv(db_path, output_dir="database/csv_exports"):
    """Export all tables from SQLite database to CSV files"""
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if not tables:
        print("❌ No tables found in database")
        conn.close()
        return False
    
    print(f"📊 Exporting {len(tables)} tables from {db_path}...")
    
    # Export each table to CSV
    for table_name in tables:
        table_name = table_name[0]
        
        # Get table data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        
        # Write to CSV file
        csv_file = os.path.join(output_dir, f"{table_name}.csv")
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(columns)  # Write header
            writer.writerows(rows)    # Write data rows
        
        print(f"✅ Exported {table_name} ({len(rows)} rows) → {csv_file}")
    
    conn.close()
    print(f"\n✅ All tables exported to {output_dir}")
    return True

if __name__ == "__main__":
    db_path = "database/vet_clinic.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found: {db_path}")
        exit(1)
    
    export_sqlite_to_csv(db_path)
    print("\n📋 Next step: Import these CSV files into Microsoft Access")
    print("   1. Open Microsoft Access")
    print("   2. Create a new blank database")
    print("   3. For each CSV file:")
    print("      - External Data > New Data Source > From File > Text File")
    print("      - Select the CSV file")
    print("      - Choose 'Append to existing table' or 'Create new table'")

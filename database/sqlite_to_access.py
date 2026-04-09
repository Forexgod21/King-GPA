#!/usr/bin/env python3
"""
SQLite to Access Converter
Converts vet_clinic.db (SQLite) to vet_clinic.accdb (Microsoft Access)

This script is designed to run on Windows with Microsoft Access installed.
It uses pypyodbc to create a native .accdb file.

Installation (Windows):
    pip install pypyodbc

Usage:
    python3 database/sqlite_to_access.py
"""

import sqlite3
import os
import sys

def sqlite_to_access(sqlite_path, access_path):
    """Convert SQLite database to Microsoft Access format"""
    
    try:
        import pypyodbc
    except ImportError:
        print("❌ pypyodbc not installed")
        print("   Windows users: pip install pypyodbc")
        print("   Then run this script again")
        return False
    
    if not os.path.exists(sqlite_path):
        print(f"❌ SQLite database not found: {sqlite_path}")
        return False
    
    print(f"📊 Converting {sqlite_path} to Access format...")
    
    try:
        # Connect to SQLite
        sqlite_conn = sqlite3.connect(sqlite_path)
        sqlite_cursor = sqlite_conn.cursor()
        
        # Create new Access database
        driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
        conn_str = f"Driver={driver};DBQ={access_path};"
        
        access_conn = pypyodbc.connect(conn_str)
        access_cursor = access_conn.cursor()
        
        # Get all tables from SQLite
        sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = sqlite_cursor.fetchall()
        
        for table_name in tables:
            table_name = table_name[0]
            
            # Get schema
            sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
            columns = sqlite_cursor.fetchall()
            
            # Create table in Access
            create_table_sql = f"CREATE TABLE {table_name} ("
            col_defs = []
            
            for col in columns:
                col_name = col[1]
                col_type = col[2]
                col_notnull = col[3]
                
                # Convert SQLite types to Access types
                if col_type.upper() == "INTEGER":
                    access_type = "INTEGER"
                elif col_type.upper() == "TEXT":
                    access_type = "TEXT"
                elif col_type.upper() == "DATETIME":
                    access_type = "DATETIME"
                else:
                    access_type = "TEXT"
                
                col_def = f"{col_name} {access_type}"
                if col_notnull:
                    col_def += " NOT NULL"
                if col_name.endswith("ID") and col_type.upper() == "INTEGER PRIMARY KEY":
                    col_def = f"{col_name} AUTOINCREMENT PRIMARY KEY"
                
                col_defs.append(col_def)
            
            create_table_sql += ", ".join(col_defs) + ")"
            
            try:
                access_cursor.execute(create_table_sql)
                print(f"✅ Created table: {table_name}")
            except Exception as e:
                print(f"⚠️  Could not create table {table_name}: {e}")
        
        # Copy data from SQLite to Access
        for table_name in tables:
            table_name = table_name[0]
            
            sqlite_cursor.execute(f"SELECT * FROM {table_name}")
            rows = sqlite_cursor.fetchall()
            
            if rows:
                // Get column count
                sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
                col_count = len(sqlite_cursor.fetchall())
                
                placeholders = ", ".join(["?"] * col_count)
                insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
                
                for row in rows:
                    access_cursor.execute(insert_sql, row)
                
                print(f"✅ Copied {len(rows)} rows to {table_name}")
        
        access_conn.commit()
        access_conn.close()
        sqlite_conn.close()
        
        print(f"\n✅ Successfully created: {access_path}")
        print(f"   Open this file in Microsoft Access to view all tables")
        return True
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    sqlite_path = "database/vet_clinic.db"
    access_path = "database/vet_clinic.accdb"
    
    if sys.platform != "win32":
        print("⚠️  This script is designed for Windows with Microsoft Access installed")
        print("   Use export_to_csv.py instead for cross-platform CSV export")
        exit(1)
    
    sqlite_to_access(sqlite_path, access_path)

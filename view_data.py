import sqlite3
import os

def view_all_calls():
    # Look for health.sqlite in current directory
    db_path = "health.sqlite"
    
    if not os.path.exists(db_path):
        print(f"Error: health.sqlite not found at {os.path.abspath(db_path)}")
        print(f"Make sure you run the IVR app first to generate the database.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM ivr_calls ORDER BY id DESC")
        rows = cursor.fetchall()
        
        if not rows:
            print("No records found in the database.")
            return
        
        # Get column names
        cursor.execute("PRAGMA table_info(ivr_calls)")
        columns = [col[1] for col in cursor.fetchall()]
        
        print("\n" + "="*160)
        print("IVR CALL RECORDS".center(160))
        print("="*160)
        
        for i, row in enumerate(rows, 1):
            print(f"\n[Record {i}]")
            for col, val in zip(columns, row):
                if col == "past_surgery":
                    val = "Yes" if val == 1 else "No"
                print(f"  {col:20s}: {val}")
        
        print("\n" + "="*160)
        print(f"Total Records: {len(rows)}".center(160))
        print("="*160 + "\n")
        
    except Exception as e:
        print(f"Error reading database: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    view_all_calls()
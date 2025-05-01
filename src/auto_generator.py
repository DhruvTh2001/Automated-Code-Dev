import datetime
import os

def generate_code():
    os.makedirs("src", exist_ok=True)  # Ensure 'src' folder exists
    code = f'''# Auto-generated code on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def auto_generated_function():
    print("This function was generated automatically!")
'''
    with open("src/generated_code.py", "w") as f:
        f.write(code)

if __name__ == "__main__":
    generate_code()

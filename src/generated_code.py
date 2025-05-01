from datetime import datetime

template_path = "src/template.txt"
output_path = "src/generated_code.py"

function_name = "auto_generated_function"
message = "This function was generated automatically!"

# Read the template
with open(template_path, "r") as file:
    template = file.read()

# Replace placeholders with actual values
code = template.replace("$function_name", function_name).replace("$message", message)

# Write the generated code to the output file
with open(output_path, "w") as file:
    file.write("# Auto-generated code on " + str(datetime.now()) + "\n\n")
    file.write(code)

# Define the auto_generated_function
def auto_generated_function():
    return "This function was generated automatically!"

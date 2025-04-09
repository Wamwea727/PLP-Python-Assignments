def modify_file_content(content):
    """Example modification function - converts text to uppercase"""
    return content.upper()

def file_processor():
    try:
        input_filename = input("Enter the input filename: ")
        
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
    
        modified_content = modify_file_content(content)
        
        output_filename = f"modified_{input_filename}"
        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File processed successfully! Modified version saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: Unable to read/write file - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_processor()
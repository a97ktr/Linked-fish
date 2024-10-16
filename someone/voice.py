import ast

def extract_voicetext(file_path):
    """Reads a text file and extracts the content after 'voicetext: \\n' until the end."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
                T=file.read()
                T=T[1:-1]
                
                L=string_to_list(T)
              
                return L[1]  # Remove leading/trailing whitespace
        
        return "hello"

    except FileNotFoundError:
        return "The specified file does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def string_to_list(input_string):
    try:
        result = ast.literal_eval(input_string)
        return result
    except (ValueError, SyntaxError) as e:
        print(f"Error: {e}")
        return None

# Example usage:


if __name__ == "__main__":
	print(extract_voicetext("./ahmed-katrou_messages.txt"))
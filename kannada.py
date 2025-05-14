import sys
import importlib.abc
import importlib.util
from pathlib import Path

import ast
import tokenize
from tokenize import TokenInfo
import io


# kannada-to-Python mappings
kannada_keywords = {
    "ಸರಿ":"True",
    "ತಪ್ಪು":"False",
    "ಏನಿಲ್ಲ":"None",
#--------------------------
    "ಮತ್ತೆ":"and",
    "ಇಲ್ಲಾ":"or",
    "ಅಲ್ಲ":"not",
#--------------------------
    "ಆದರೆ": "if",
    "ಇಲ್ಲವೇ": "else",
    "ಇಲ್ಲಂದ್ರೆ": "elif",
#--------------------------
    "ಮಾಡ್ಕೊತಿರು": "for",
    "ಇರೋವರೆಗೂ": "while",
    "ನಿಲ್ಲು": "break",
    "ಮುಂದುವರೆ": "continue",
    "ಬಿಡು":"pass", 
#--------------------------
    "ದಗದ": "def",
    "ಕಳಿಸು": "return",
    "ಹೆಸರಿಲ್ಲದ": "lambda",
#--------------------------
    "ಮಾಡು": "try",
    "ಆಗದಿದ್ದರೆ": "except",
    "ಕಡೆಗೆ":"finally",
    "ಅಡ್ಡಿಮಾಡು":"raise",
    "ಮತ್ತೆನೋಡು":"assert",
#--------------------------
    "ತಗೋ": "import",
    "ಇಂದ":"from",
    "ಹಾಗೆ":"as",
#--------------------------
    "ಎಲ್ಲಿಯ":"global",
    "ಇಲ್ಲಿಯ":"nonlocal",
    "ಕಿತ್ತು":"del",
#--------------------------
    "ದಾರಿಗೆ ": "class",
    "ಕೂಡ":"with",
    "ಅಡ್ಡಿಮಾಡದೆ":"async",
    "ಅಲ್ಲಿವರೆಗೂ":"await",
#--------------------------
    "ಒಳಗೆ": "in",
    "ಇದ್ದು":"is",
    "ಇಳುವು":"yield",
#--------------------------functions
    "ಇದಿಷ್ಟು": "range",
    "ಹೇಳು": "print",
    "ಕೊಡು":"input",
#---------------------------temporary_use
    "ಯುನಿಕೋಡ್_ಅಂಕ":"ord",
#---------------------------
    "kannada":"python"
}

def parse_syntax(translated_code):
    try:
        ast.parse(translated_code)
        return translated_code  # Valid Python code
    except SyntaxError as e:
        print(f"Syntax error in translated code: {e}")
        return None  # Return None to indicate invalid code

def translate_kannada(code: str) -> str:
    result = []
    # tokenize.tokenize() requires bytes input
    bytes_io = io.BytesIO(code.encode('utf-8'))
    tokens = tokenize.tokenize(bytes_io.readline)

    #making sure previous token should not be '.' so the it is not part of any class
    prev_tok_string = 0

    for tok in tokens:
        if tok.type == tokenize.NAME and tok.string in kannada_keywords and prev_tok_string != '.':
            tok = TokenInfo(tok.type, kannada_keywords[tok.string], tok.start, tok.end, tok.line)
        prev_tok_string = tok.string
        result.append(tok)

    translated_code = tokenize.untokenize(result).decode('utf-8')
    return parse_syntax(translated_code)


# Custom import loader and finder
class kaypyLoader(importlib.abc.SourceLoader):
    def __init__(self, path):
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            kannada_code = f.read()
        return translate_kannada(kannada_code).encode('utf-8')

class kaypyFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        module_path = Path(fullname.replace(".", "/") + ".kaypy")
        if module_path.exists():
            return importlib.util.spec_from_loader(fullname, kaypyLoader(str(module_path)))
        return None

# Activate the import hook globally
sys.meta_path.insert(0, kaypyFinder())

# Script runner
def run_kannada_file(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            kannada_code = f.read()
        translated_code = translate_kannada(kannada_code)
        exec(compile(translated_code, file_path, "exec"), {"__name__": "__main__"})
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error while running kannada code:\n{e}")

# CLI entrypoint
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python kannada.py <file.kaypy>")
    else:
        run_kannada_file(sys.argv[1])

import os
import sys
import importlib

current_dir = os.path.dirname(os.path.abspath(__file__))

def to_camel_case(s):
    """Convert a string to camel case."""
    parts = s.split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

def import_checkers_from_modules():
    """Import checker functions from all relevant modules."""
    checkers = {}
    
    for entry in os.listdir(current_dir):
        dir_path = os.path.join(current_dir, entry)
        if os.path.isdir(dir_path) and entry[0].isdigit():
            module_name = to_camel_case(entry.split(' - ')[1])
            
            sys.path.insert(0, dir_path)
            
            try:
                imported_module = importlib.import_module(module_name)
                # Find and store checker functions
                for attr in dir(imported_module):
                    if attr.endswith('Checker'):
                        checkers[attr] = getattr(imported_module, attr)
                # print(f"Successfully imported module + checkers: {module_name}")
            except ImportError as e:
                print(f"Failed to import module {module_name}: {e}")
            finally:
                # Clean up sys.path
                sys.path.pop(0)
    
    return checkers




def unitTest():
    """Test all of your methods"""
    tests = 0
    incorrect = []
    checkers = import_checkers_from_modules()
    # execute each checker
    for name, checker in checkers.items():
        tests +=1
        print(f'------------------{name}--------------------')
        try:
            checker()
        except Exception as e:
            incorrect.append(name)
            print(f"Error running {name}: {e}")
        print()
    
    print(f'***** {tests - len(incorrect)}/{tests} passed *****')
    if len(incorrect) > 0:
        print(f'Failed tests: {incorrect}')

if __name__ == "__main__":
    unitTest()

def dedupe(items):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def add_numbers(a, b):
    """Additional functionality for testing"""
    return a + b

if __name__ == "__main__":
    # Test dedupe functionality
    sample = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {sample}")
    print(f"Deduplicated: {dedupe(sample)}")
    
    # Test addition functionality
    print(f"5 + 3 = {add_numbers(5, 3)}")
# transpiler.py
def transpile_c_to_rust(c_code: str) -> str:
    """
    نمونه اولیه ترنسپایلر C -> Rust
    این نسخه ساده جایگزین‌ها و ترجمه اولیه انجام میده
    """
    rust_code = c_code.replace("printf", "println!") \
                      .replace("int", "i32") \
                      .replace("return 0;", "")
    return rust_code

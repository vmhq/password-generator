# 🔐 Password Generator 🐍

This Python script provides a robust solution for generating secure and customizable passwords. By leveraging the `secrets` module, it ensures a high degree of randomness, crucial for creating strong passwords.

## 🌟 Features

- **Customizable Length**: Choose the length of your password.
- **Optional Character Sets**:
  - Uppercase Letters (excluding 'I' and 'O' for clarity)
  - Numbers (excluding '0' and '1' for clarity)
  - Symbols
- **Exclusions for Better Clarity**: Certain characters like 'l', 'I', 'O', '0', and '1' are excluded to avoid confusion.

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vmhq/password-generator.git
   ```
2. **Run the script**:
   ```bash
   python password_generator.py
   ```

## 📝 How to Use

When you run the script, it will prompt you for:

- **Password Length**: Enter a positive integer.
- **Character Inclusions**:
  - Uppercase letters (Y/n)
  - Numbers (Y/n)
  - Symbols (Y/n)

After providing the input, the script will generate and display a secure password.

## 💡 Example

```
Password length: 10
Do you want to include uppercase letters? (y/n): y
Do you want to include numbers? (y/n): y
Do you want to include symbols? (y/n): n
Your new password is: eG7kq2s8Af
```

## 🛠️ Built With

- Python
- `secrets` module for secure random generation

## ✨ Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/vmhq/password-generator/issues).

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Created with ❤️ and Python. 


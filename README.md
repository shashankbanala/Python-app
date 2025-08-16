# Math Calculator Web Application

A simple and beautiful web application that can compute mathematical expressions. Built with Python Flask and modern HTML/CSS.

## Features

- 🧮 **Mathematical Operations**: Basic arithmetic (+, -, *, /, **)
- 📐 **Mathematical Functions**: sin, cos, tan, sqrt, log, exp, abs
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 📱 **Responsive**: Works on desktop and mobile devices
- ⚡ **Real-time**: Instant calculation results
- 🔒 **Secure**: Input validation and safe expression evaluation

## Supported Operations

### Basic Arithmetic
- Addition: `2 + 3`
- Subtraction: `5 - 2`
- Multiplication: `4 * 3`
- Division: `10 / 2`
- Exponentiation: `2**3`

### Mathematical Functions
- Trigonometric: `sin(3.14)`, `cos(0)`, `tan(1.57)`
- Square root: `sqrt(16)`
- Natural logarithm: `log(10)`
- Exponential: `exp(1)`
- Absolute value: `abs(-5)`

### Complex Expressions
- Parentheses: `(2 + 3) * (4 - 1)`
- Mixed operations: `2 + 3 * 4 - 1`

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter any mathematical expression in the input field
2. Click "Calculate Result" or press Enter
3. View the result instantly

### Example Expressions

- `2 + 3 * 4` → 14
- `sin(3.14)` → 0.0015926529164868282
- `sqrt(16)` → 4.0
- `(2 + 3) * (4 - 1)` → 15
- `2**3` → 8
- `log(10)` → 2.302585092994046

## Project Structure

```
Python app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/
│   └── index.html     # HTML template with CSS and JavaScript
└── GIT_SETUP_GUIDE.md # Git setup guide
```

## Technical Details

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Security**: Input validation and safe expression evaluation
- **Styling**: Modern CSS with gradients and animations
- **Responsive**: Mobile-first design approach

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` line 47
2. **Module not found**: Run `pip install -r requirements.txt`
3. **Browser not loading**: Check if the server is running on `http://localhost:5000`

### Development

To run in development mode with auto-reload:
```bash
python app.py
```

The application will automatically reload when you make changes to the code.

## Security Notes

- The application uses safe expression evaluation
- Only mathematical operations and functions are allowed
- Input is validated before processing
- No arbitrary code execution is possible

## Process Followed

### Development Steps

1. **Project Setup**
   - Created the main Flask application (`app.py`)
   - Set up the project structure with templates directory
   - Created requirements.txt with necessary dependencies

2. **Backend Development**
   - Implemented Flask web server with two routes:
     - `/` - Serves the main HTML page
     - `/calculate` - Handles POST requests for mathematical calculations
   - Created `evaluate_expression()` function with security features:
     - Input validation to prevent malicious code execution
     - Support for basic arithmetic operations (+, -, *, /, **)
     - Support for mathematical functions (sin, cos, tan, sqrt, log, exp, abs)
     - Safe expression evaluation using restricted namespace

3. **Frontend Development**
   - Created responsive HTML template with modern design
   - Implemented CSS with:
     - Gradient background and glass-morphism effects
     - Smooth animations and hover effects
     - Mobile-responsive design
   - Added JavaScript for:
     - Asynchronous form submission
     - Real-time result display
     - Error handling and loading states
     - Enter key support for form submission

4. **Security Implementation**
   - Input sanitization and validation
   - Restricted character set for mathematical expressions
   - Safe evaluation environment with limited namespace
   - Error handling for invalid expressions

5. **Documentation**
   - Created comprehensive README with:
     - Installation instructions
     - Usage examples
     - Feature descriptions
     - Troubleshooting guide
     - Security notes

### Technologies Used

- **Backend**: Python Flask framework
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Security**: Input validation and safe expression evaluation
- **Styling**: Modern CSS with gradients and animations
- **Development**: Git version control

### Key Features Implemented

- ✅ Mathematical expression evaluation
- ✅ Real-time calculation results
- ✅ Modern, responsive UI design
- ✅ Security measures against code injection
- ✅ Error handling and user feedback
- ✅ Mobile-friendly interface
- ✅ Comprehensive documentation

## License

This project is open source and available under the MIT License. 
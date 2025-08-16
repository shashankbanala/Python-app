# Git Setup Guide: Challenges and Solutions

## Overview
This document outlines the challenges faced while setting up Git tracking for a Python project and the solutions implemented to overcome them.

## Challenge : Git Works in System PowerShell but Not in IDE Terminal

### Problem
Git commands worked in PowerShell opened from Windows Start but failed in Cursor IDE's integrated terminal.

### Root Cause
IDE-integrated terminals often have different PATH environment variables or run in isolated contexts.

### Investigation Steps
1. **Check user profile**:
   ```powershell
   $env:USERNAME          # Returns: shash
   $env:USERPROFILE       # Returns: C:\Users\shash
   ```

2. **Check administrator privileges**:
   ```powershell
   ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
   # Returns: False
   ```

3. **Verify Git installation**:
   ```powershell
   git --version
   # Works in system PowerShell: git version 2.50.0.windows.1
   # Fails in IDE terminal: CommandNotFoundException
   ```

### Solutions

#### Solution 1: Use Full Git Path
```powershell
"C:\Program Files\Git\bin\git.exe" --version
```

#### Solution 2: Add Git to Current Session PATH
```powershell
$env:PATH += ";C:\Program Files\Git\bin"
git --version
```

#### Solution 3: Use Git Bash in IDE
- Open terminal dropdown in Cursor
- Select "Git Bash" instead of PowerShell
- Git Bash comes with Git pre-configured

#### Solution 4: Check PATH in IDE Terminal
```powershell
$env:PATH -split ';' | Where-Object {$_ -like "*git*"}
```

## Complete Git Setup Process

### Step 1: Initialize Repository
```powershell
git init
```

### Step 2: Configure Git (First Time)
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Create .gitignore
Create a `.gitignore` file with Python-specific exclusions:
```
# Byte-compiled files
__pycache__/
*.py[cod]

# Virtual environments
venv/
env/
.env

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

### Step 4: Add and Commit Files
```powershell
git add .
git commit -m "Initial commit"
```

### Step 5: Connect to Remote (Optional)
```powershell
git remote add origin <repository-url>
git push -u origin main
```

## Key Takeaways

1. **Environment Differences**: System terminals and IDE terminals may have different PATH configurations
2. **Installation Verification**: Always verify Git installation with `git --version`
3. **Multiple Solutions**: Several approaches exist for PATH issues in IDE terminals
4. **Git Bash Alternative**: Using Git Bash in IDEs often resolves PATH-related issues
5. **Session-Specific Fixes**: Adding Git to PATH for current session is a quick workaround

## Troubleshooting Checklist

- [ ] Git installed on system
- [ ] Git accessible in system PowerShell
- [ ] Git accessible in IDE terminal
- [ ] Repository initialized
- [ ] Git configured with user details
- [ ] .gitignore file created
- [ ] Initial commit made
- [ ] Remote repository connected (if applicable)

## Common Commands Reference

```powershell
# Check Git version
git --version

# Check current user
$env:USERNAME

# Check user profile path
$env:USERPROFILE

# Check if running as administrator
([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

# Add Git to current session PATH
$env:PATH += ";C:\Program Files\Git\bin"

# Check PATH for Git entries
$env:PATH -split ';' | Where-Object {$_ -like "*git*"}
```

---

*This guide documents the challenges faced during Git setup for a Python project and provides practical solutions for similar issues.* 
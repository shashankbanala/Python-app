# Day 2 Progress

## Objective
Host the Flask application on an EC2 instance.

---

## Steps Performed

### 1. Launched an EC2 Instance
- Logged into AWS Management Console.
- Navigated to the **EC2** service and launched a new instance with the following configuration:
  - **AMI**: Amazon Linux 2.
  - **Instance Type**: t2.micro (Free Tier eligible).
  - **Key Pair**: Selected the existing key pair `Math Calculator EC2.pem`.
  - **Security Group**: Configured to allow SSH (port 22) and HTTP (port 80).
  - **Storage**: Used default storage settings (8 GB).
- Successfully launched the instance and noted its public IP address.

### 2. Connected to the Instance via SSH
- Used the following command to connect to the instance:
  ```powershell
  ssh -i "C:\Users\shash\Downloads\Math Calculator EC2.pem" ec2-user@<public-ip>
  ```
- Verified the connection and accessed the EC2 instance.

### 3. Installed Python and Flask
- Updated the package manager:
  ```bash
  sudo yum update -y
  ```
- Installed Python 3:
  ```bash
  sudo yum install python3 -y
  ```
- Installed Flask:
  ```bash
  pip3 install Flask
  ```

### 4. Transferred Application Code
- Use this command outside ssh session, in your local terminal
- Used the following SCP command to transfer the application code to the EC2 instance from your local:
  ```powershell
  scp -i "C:\Users\shash\Downloads\Math Calculator EC2.pem" -r "C:\Users\shash\Cursor projects\Python app" ec2-user@<public-ip>:~/
  ```
- Verified that the files were successfully transferred to the EC2 instance.

### 5. Ran the Flask Application
- Navigated to the project folder on the EC2 instance:
  ```bash
  cd Python\ app
  ```
- Started the Flask app:
  ```bash
  python3 app.py
  ```
- Accessed the application using the public IP address of the EC2 instance.

### 6. Configured Security Groups
- Modified the security group to allow HTTP traffic on port 80:
  - **Type**: HTTP
  - **Protocol**: TCP
  - **Port Range**: 80
  - **Source**: Anywhere (0.0.0.0/0).

---

## Deliverables
- Flask app hosted on an EC2 instance.
- Application accessible via the public IP address.

---


## Important Learnings and Changes

- **SCP File Transfer:**
  - Run `scp` from your local machine, not from within the SSH session.
  - To avoid transferring unnecessary files (like `.pyc`), use a `.gitignore` with Git-based deployment, or create a `.tar.gz`/`.zip` archive excluding those files.

- **Flask App Not Accessible Externally:**
  - The Flask app must be started with `host='0.0.0.0'` to be accessible from outside the EC2 instance.
  - Use `sudo` to run on port 80, or use port 5000 and update security group rules and Nginx config accordingly.

## Code Snippet: Starting the Flask App

Make sure your `app.py` ends with:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

To start the app on EC2:

```bash
python3 app.py
# or, if running on port 80 (requires sudo):
sudo python3 app.py
```

If using Nginx as a reverse proxy, keep Flask on port 5000 and Nginx on port 80.

- **Debugging Access Issues:**
  - Always check that the app is running and listening on the correct port.
  - Use `curl http://localhost/` on the EC2 instance to verify local access.
  - If local access works but browser access fails, check security group rules and use `http://` (not `https://`) unless SSL is configured.

- **Nginx as a Reverse Proxy:**
  - Nginx is used to forward external HTTP(S) requests to the Flask app running on a different port (e.g., 5000).
  - If Nginx is running on port 80, Flask should run on another port (commonly 5000).
  - Update Nginx config in `/etc/nginx/conf.d/flaskapp.conf` to proxy to the correct port.

- **HTTPS/SSL with Let’s Encrypt:**
  - Let’s Encrypt does **not** issue certificates for AWS EC2 public DNS names (like `ec2-52-203-17-194.compute-1.amazonaws.com`).
  - For real HTTPS, use a custom domain name pointing to your EC2 instance, then use Certbot to obtain a certificate.
  - For testing, you can use a self-signed certificate, but browsers will show a warning.

- **General Troubleshooting:**
  - If you get `ModuleNotFoundError: No module named 'flask'` with `sudo`, install Flask using `sudo pip3 install Flask`.
  - If you get `Address already in use`, another process (likely Nginx) is using the port. Run Flask on a different port or stop Nginx.

- **Security:**
  - Always restrict SSH access in your security group to your own IP for better security.

- **Summary:**
  - Successfully deployed and accessed the Flask app via HTTP.
  - Learned about reverse proxying, port conflicts, and SSL limitations on EC2 public DNS.
  - Ready to proceed to Day 3 tasks.

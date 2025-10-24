# 🧾 Assignment Brief

**Task:**  
Buy your own domain via **Cloudflare** or **AWS Route53**.  

Create an **EC2 instance** running **NGINX** on port **80**.  
Add an **A Record** to Cloudflare or Route53 and point it to your EC2 instance.  

You should be able to access the NGINX webpage using your domain — for example:  
> `nginx.luqman.co.uk`

## 📘 Introduction

This README is a **demonstration** of how I completed the networking assignment.  
It provides a **step-by-step outline** of the process I followed to successfully set up and connect my EC2 instance to a custom domain.

Initially, I attempted to use **Cloudflare** and **AWS Route53** for my domain setup, but due to configuration and access issues, they did not work as expected.  
As a result, I decided to use **Namecheap** for my DNS management, which allowed me to configure my domain records smoothly.
## 🪩 Step 1 — Setting Up the EC2 Instance

I began by setting up a new **Amazon EC2 instance**.  
From the AWS Management Console, I navigated to **EC2** and clicked **“Launch Instance.”**

I selected the following configuration:
- **Name:** Networking-Assignment  
- **AMI:** Ubuntu Server (latest version)  
- **Instance Type:** t2.micro (Free Tier eligible)  
- **Key Pair:** Created a new key pair and downloaded the `.pem` file for SSH access  

> ⚠️ Selecting a key pair is **essential**, as it allows you to securely connect to your EC2 instance later using SSH.

Once launched, my instance was up and running successfully.  
At this stage, it’s important to **take note of the Public IPv4 Address**, as it will be used to connect your EC2 instance to your custom domain.

🖼️ *Screenshot:* `ec2_connect_page.png` (Shows the instance running and the public IP address)
## 🌐 Step 2 — Purchasing the Domain and Configuring DNS

For this step, I purchased my own domain from **Namecheap** — `ahmedo.co.uk`.  

Since the assignment required the use of **NGINX**, I created a **subdomain** with the host name `nginx`.  
This means my website would be accessible at **nginx.ahmedo.co.uk**.

In the Namecheap DNS settings:
- **Type:** A Record  
- **Host:** nginx  
- **Value:** (Public IPv4 address of my EC2 instance)  
- **TTL:** 300 seconds (5 minutes)  

This A record connects my domain to my EC2 instance, allowing anyone who visits the domain to reach the NGINX web server hosted on my instance.

🖼️ *Screenshot:* `namecheap_dns.png` (Shows the Namecheap DNS A record setup)

## 🔐 Step 3 — Connecting to the EC2 Instance (SSH Access)

Once my EC2 instance was running, I attempted to **SSH** into it through the terminal using my `.pem` key file.  
However, I encountered a problem — the connection kept being **refused** and would not allow me to access the instance.

To troubleshoot this, I checked my **security group settings** and realised that **SSH (port 22)** traffic was not properly allowed.  
I edited the **inbound rules** to include the following:

- **Type:** SSH  
- **Protocol:** TCP  
- **Port Range:** 22  
- **Source:** My IP  

Even after updating the security group, I still could not connect.  
After further investigation, I discovered that my **Network ACL (NACL)** was also blocking SSH traffic.  
I updated the NACL rules to allow inbound and outbound connections for **port 22** as well.  

'/home/ahmedo/Coder_co_Modules/Networking-Assigment/screenshots/security_groups.png' 
 (Shows the security group inbound rules allowing SSH)
🖼
'/home/ahmedo/Coder_co_Modules/Networking-Assigment/screenshots/nacl_rules.png' 
 (Shows the NACL rules configured to allow SSH)


Once both were updated, I successfully SSH’d into my EC2 instance using:

Before connecting, I also reviewed the EC2 Connect Page on the AWS console, which provides detailed SSH instructions.
It’s important to follow this page carefully to ensure your connection works properly.

⚠️  Make sure to give your .pem file the correct permissions before connecting:

`chmod 400 n-assignment.pem`

`ssh -i n-assignment.pem ubuntu@<public-ip-address>`

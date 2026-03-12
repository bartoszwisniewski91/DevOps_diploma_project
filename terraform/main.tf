terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

# 1. GENEROWANIE KLUCZA SSH
resource "tls_private_key" "devops_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# 2. REJESTRACJA KLUCZA W AWS
resource "aws_key_pair" "generated_key" {
  key_name   = "devops-project-key"
  public_key = tls_private_key.devops_key.public_key_openssh
}

# 3. WYSZUKIWANIE NAJNOWSZEGO UBUNTU
data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] 
}

# 4. KONFIGURACJA SIECI (SECURITY GROUP)
resource "aws_security_group" "devops_sg" {
  name        = "devops-project-sg-final"
  description = "Allow HTTP, SSH and App Port"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # DODANE: Porty pod monitoring, o których wspominaliśmy
  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 5. SERWER (EC2)
resource "aws_instance" "devops_server" {
  # ZMIANA: Używamy dynamicznego wyszukiwania AMI zamiast sztywnego ID
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  key_name      = aws_key_pair.generated_key.key_name
  vpc_security_group_ids = [aws_security_group.devops_sg.id]
  
  user_data_replace_on_change = true 

  user_data = <<-EOF
              #!/bin/bash
              exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
              
              apt-get update -y
              apt-get install -y docker.io
              systemctl start docker
              systemctl enable docker
              
              # Poprawka uprawnień - restart dockera po dodaniu grupy
              usermod -aG docker ubuntu
              
              # Opcjonalnie k3s, jeśli go planujesz
              curl -sfL https://get.k3s.io | sh -
              chmod 644 /etc/rancher/k3s/k3s.yaml
              EOF

  tags = {
    Name = "DevOps-Project-Server"
  }
}

# 6. WYJŚCIA (OUTPUTS)
output "server_public_ip" {
  value = aws_instance.devops_server.public_ip
}

output "private_key" {
  value     = tls_private_key.devops_key.private_key_pem
  sensitive = true
}
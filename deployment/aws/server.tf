provider "aws" {
  profile = "default"
  region  = "us-east-1"
}


resource "aws_instance" "rasa-instance" {
  ami = "ami-04b9e92b5572fa0d1"
  instance_type = var.instance_type
  key_name = var.key_pair
  security_groups = ["${aws_security_group.rasa-instance.name}"]
  root_block_device {
    volume_type = "gp2"
    volume_size = "100"
    delete_on_termination = "true"
    }
  tags = {
    Name = "instill-assistant"
  }

  connection {
    type     = "ssh"
    user     = "ubuntu"
    private_key = file("~/.ssh/rasa-chatbot.pem")
    host     = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.24.1/install.sh",
    ]
  }
}
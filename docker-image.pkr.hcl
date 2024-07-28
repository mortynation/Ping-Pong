packer {
  required_plugins {
    docker = {
      version = ">= 0.0.7"
      source  = "github.com/hashicorp/docker"
    }
  }
}

variable "docker_image" {
  type    = string
  default = "ubuntu:20.04"
}

source "docker" "ubuntu" {
  image  = var.docker_image
  commit = true
  changes = [
    "ENV DEBIAN_FRONTEND=noninteractive",
    "ENV TZ=Etc/UTC",
    "WORKDIR /app",
    "CMD [\"python3\"]"
  ]
}

build {
  name = "learn-packer"
  sources = [
    "source.docker.ubuntu"
  ]

  provisioner "shell" {
    inline = [
      "mkdir -p /opt/pong-srv"
    ]
  }

  provisioner "file" {
    source      = "pong.py"
    destination = "/opt/pong-srv/pong.py"
  }

  provisioner "shell" {
    inline = [
      "apt-get update",
      "ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime",
      "apt-get install -y tzdata",
      "dpkg-reconfigure --frontend noninteractive tzdata",
      "apt-get install -y python3",
      "chmod 700 /opt/pong-srv/pong.py",
      "ls -lrth /opt/pong-srv/",
    #   "python3 /opt/pong-srv/pong.py"
    ]
  }

  post-processor "docker-tag" {
    repository = "pong-server-image"
    tags       = ["latest"]
  }
}
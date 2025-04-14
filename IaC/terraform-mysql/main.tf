terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.16.0"
    }
  }
} 

variable "mysql_env" {
  type = string({
    internal = 3306
    external = 3307

    })
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "mysql" {
  name = "mysql:5.7"
}

resource "docker_container" "mysql_1" {
  name = "mysql-1"
  image = docker_image.mysql.latest
  ports {
    internal = var.mysql_env.internal
    external = var.mysql_env.external
  }
  env = [
    "MYSQL_ROOT_PASSWORD=rootpassword",
    "MYSQL_DATABASE=db1"
  ]
}

resource "docker_container" "mysql_2" {
  name = "mysql-2"
  image = docker_image.mysql.latest
  ports {
    internal = 3306
    external = 3308
  }
  env = [
    "MYSQL_ROOT_PASSWORD=rootpassword",
    "MYSQL_DATABASE=db2"
  ]
}


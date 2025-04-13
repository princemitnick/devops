terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.16.0"
    }
  }
} 

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "mysql" {
  name = "mysql:5.7"
}

resource "docker_conatiner" "mysql_1" {
  name = "mysql"
  image = docker_image.mysql.latest
  ports {
    internal = 3306
    external = 3307
  }
  env = [
    "MYSQL_ROOT_PASSWORD=rootpassword",
    "MYSQL_DATABASE=db1"
  ]
}

resource "docker_conatiner" "mysql_2" {
  name = "mysql"
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


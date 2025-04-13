terraform {
  required_version = ">= 0.12"
}

resource "null_resource" "nginx_installation" {
  provisioner "local-exec" {
    command = <<-EOF
        echo "Update packages"
        sudo apt-get update
        echo "Nginx installation"
        sudo apt-get install -y nginx
    EOF
  }

  provisioner "local-exec" {
    when = destroy
    command = <<-EOF
        echo "Uninstall nginx"
        sudo apt-get remove -y nginx
    EOF
  }
}
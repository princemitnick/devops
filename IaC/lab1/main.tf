terraform {
    required_providers {
        local = {
            source = "hashicorp/local"
        }
    }
}

resource "local_file" "example" {
  content = "First lab"
  filename = "${path.module}/hello.txt"
}
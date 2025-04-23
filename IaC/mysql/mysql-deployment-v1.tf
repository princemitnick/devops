provider "kubernets" {
    config_path: "~/.kube/config"
}

resource "kubernetes_namespace" "mysql_ns" {
  metadata {
    name = "mysql-namespace"
  }
}

#Secret Mysql

resource "kubernetes_secret" "mysql-secret" {
  metadata {
    name = "mysql-secret"
    namespace = kubernetes_namespace.mysql_ns.metadata[0].name
  }
  data = {
    mysql-root-password = base64decode("test")
    mysql-user = "test"
    mysql-password = "test"
  }
  type = "Opaque"
}

# Persistent Volume
resource "kubernetes_persistent_volume" "mysql_pv" {
  metadata {
    name = "mysql-pv"
  }
  spec {
    capacity = {
      storage = "1Gi"
    }
    access_modes = [ "ReadWriteOnce" ]
    host_path {
        path = "/mnt/data/mysql"
    }
  }
}

# Persistent Volume Claim
 resource "kubernetes_persistent_volume_claim" "mysql_pvc" {
   metadata {
     name = "mysql-pvc"
     namespace = kubernetes_namespace.mysql_ns.metadata[0].name
   }
   spec {
     access_modes = ["ReadWriteOnce"]
     resources {
       requests = {
         storage = "1Gi"
       }
     }
   }
 }

 # Deployment MySQL

 resource "kubernetes_deployment" "mysql" {
   metadata {
     name = "mysql-deployment"
     namespace = kubernetes_namespace.mysql_ns.metadata[0].name
     labels = {
       app = "mysql"
     }
   }
   spec {
     replicas = 2
     selector {
       match_labels = {
         app = "mysql"
       }
     }
     template {
       metadata {
         labels = {
           app = "mysql"
         }
       }
       spec {
         container {
           name = "mysql"
           image = "mysql:5.7"
           port {
             container_port = 3306
           }
           env {
             name = "MYSQL_ROOT_PASSWORD"
             value_from {
               secret_key_ref {
                 name = kubernetes_secret.mysql_secret.metadata[0].name
                 key = "mysql-root-password"
               }
             }
           }
           env {
             name = "MYSQL_USER"
             value_from {
               secret_key_ref {
                 name = kubernetes_secret.mysql_secret.metadata[0].name
                 key = "mysql-user"
               }
             }
           }
           env {
             name = "MYSQL_PASSWORD"
             value_from {
               secret_key_ref {
                 name = kubernetes_secret.mysql_secret.metadata[0].name
                 key = "mysql-password"
               }
             }
           }
           volume_mount {
             name = "mysql-storage"
             mount_path = "/var/lib/mysql"
           }
         }
         volume {
           name = "mysql-storage"
           persistent_volume_claim {
             claim_name = kubernetes
           }
         }
       }
     }
   }
 }

 # Service MySQL

 resource "kubernetes_service" "name" {
   metadata {
     name = "mysql-service"
     namespace = kubernetes_namespace.mysql_ns.metadata[0].name
   }
   spec {
     selector = {
       app = "mysql"
     }
     port{
        port = 3306
        target_port = 3306
        node_port = 30036
     }
     type = "NodePort"
   }
 }
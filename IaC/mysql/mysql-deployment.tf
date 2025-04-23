# Provisionnement Kubernetes avec Terraform pour déployer MySQL (2 réplicas) avec Secret, PV, PVC, Deployment, Service et phpMyAdmin

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Namespace dédié
resource "kubernetes_namespace" "mysql_ns" {
  metadata {
    name = "mysql-namespace"
  }
}

# Secret MySQL
resource "kubernetes_secret" "mysql_secret" {
  metadata {
    name      = "mysql-secret"
    namespace = kubernetes_namespace.mysql_ns.metadata[0].name
  }
  data = {
    mysql-root-password = base64encode("mysqlroot")
    mysql-user           = base64encode("myuser")
    mysql-password       = base64encode("mypass")
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
    access_modes = ["ReadWriteOnce"]
    host_path {
      path = "/mnt/data/mysql"
    }
  }
}

# Persistent Volume Claim
resource "kubernetes_persistent_volume_claim" "mysql_pvc" {
  metadata {
    name      = "mysql-pvc"
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
    name      = "mysql-deployment"
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
          name  = "mysql"
          image = "mysql:5.7"

          port {
            container_port = 3306
          }

          env {
            name = "MYSQL_ROOT_PASSWORD"
            value_from {
              secret_key_ref {
                name = kubernetes_secret.mysql_secret.metadata[0].name
                key  = "mysql-root-password"
              }
            }
          }

          env {
            name = "MYSQL_USER"
            value_from {
              secret_key_ref {
                name = kubernetes_secret.mysql_secret.metadata[0].name
                key  = "mysql-user"
              }
            }
          }

          env {
            name = "MYSQL_PASSWORD"
            value_from {
              secret_key_ref {
                name = kubernetes_secret.mysql_secret.metadata[0].name
                key  = "mysql-password"
              }
            }
          }

          volume_mount {
            name       = "mysql-storage"
            mount_path = "/var/lib/mysql"
          }
        }

        volume {
          name = "mysql-storage"
          persistent_volume_claim {
            claim_name = kubernetes_persistent_volume_claim.mysql_pvc.metadata[0].name
          }
        }
      }
    }
  }
}

# Service MySQL (NodePort pour accès depuis l'extérieur du cluster)
resource "kubernetes_service" "mysql_service" {
  metadata {
    name      = "mysql-service"
    namespace = kubernetes_namespace.mysql_ns.metadata[0].name
  }
  spec {
    selector = {
      app = "mysql"
    }
    port {
      port        = 3306
      target_port = 3306
      node_port   = 30036
    }
    type = "NodePort"
  }
}

# Deployment phpMyAdmin
resource "kubernetes_deployment" "phpmyadmin" {
  metadata {
    name      = "phpmyadmin"
    namespace = kubernetes_namespace.mysql_ns.metadata[0].name
    labels = {
      app = "phpmyadmin"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "phpmyadmin"
      }
    }
    template {
      metadata {
        labels = {
          app = "phpmyadmin"
        }
      }
      spec {
        container {
          name  = "phpmyadmin"
          image = "phpmyadmin:latest"
          port {
            container_port = 80
          }
          env {
            name  = "PMA_HOST"
            value = kubernetes_service.mysql_service.metadata[0].name
          }
          env {
            name  = "PMA_PORT"
            value = "3306"
          }
        }
      }
    }
  }
}

# Service phpMyAdmin (NodePort)
resource "kubernetes_service" "phpmyadmin_service" {
  metadata {
    name      = "phpmyadmin-service"
    namespace = kubernetes_namespace.mysql_ns.metadata[0].name
  }
  spec {
    selector = {
      app = "phpmyadmin"
    }
    port {
      port        = 80
      target_port = 80
      node_port   = 30081
    }
    type = "NodePort"
  }
}

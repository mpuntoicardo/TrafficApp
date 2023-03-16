# Define the Docker image
resource "docker_image" "my_app" {
  name = "my_app"
  tag  = "latest"
}

# Define the Docker container
resource "docker_container" "my_app" {
  name  = "my_app"
  image = "${docker_image.my_app.name}:${docker_image.my_app.tag}"

  ports {
    internal = 8080
    external = 8080
  }

  env {
    VARIABLE1 = "value1"
    VARIABLE2 = "value2"
  }
}


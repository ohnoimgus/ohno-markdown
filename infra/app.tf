
resource "digitalocean_app" "markdown-server" { 
  spec {
    name   = "markdown-server"
    region = "ams"

    service {
      name               = "server"
      environment_slug   = "python"
      instance_count     = 1
      instance_size_slug = "basic-xxs" 

      run_command   = "gunicorn --worker-tmp-dir /dev/shm main:app -w 4 -k uvicorn.workers.UvicornWorker"
      # build_command = "pip install requirements.txt" # TODO

      github {
        repo           = "ohnoimgus/ohno-markdown" # TODO
        branch         = "main"
        deploy_on_push = false
      }
    }
  }
}

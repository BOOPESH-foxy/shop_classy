terraform {
  backend "s3" {
    bucket = "state-host"
    key    = "terraform-state/terraform.tfstate"
    region = "ap-south-1"
    dynamodb_table = "terraform_locks"
  }
}


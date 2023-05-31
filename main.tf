variable "variable1" {
  description = "Description of variable1"
  type        = string
  default     = "default_value"
}

resource "aws_instance" "example" {
  instance_type = var.variable1
  # ...
}
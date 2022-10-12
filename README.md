# Thesis API

## Prerequisites

Use Python version 3.9+.

## Develop

To generate the code docs pages run the following command: `mkdocs serve`

## Build

### mkdocs

Build the docs pages: `mkdocs build`

### Docker

Build the docker image: ``

Test your docker by running it locally: `source .env; docker-compose up`

## Publish

### Build on AWS Elastic Beanstalk

1. `eb init -p docker api-docs --region`
2. `eb create api-docs`
3. Test your application with `eb open`

### Deploy on AWS Elastic Beanstalk

Before deploying the EB application, build and push your `Dockerfile` files. Only then follow the following steps:

1. `eb use api-docs`
2. `eb deploy`
3. Test your application with `eb open`

## Further reading

[Using the Docker platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker.html)

[AWS — Deploying React App With NodeJS Backend On EKS](https://medium.com/bb-tutorials-and-thoughts/aws-deploying-react-app-with-nodejs-backend-on-eks-e5663cb5017f)

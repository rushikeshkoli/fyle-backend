# Django App for the Assignment
- The project can be built using dockerfile.
- Port 8000 is exposed in docker image.

### Two Routes
```
'/api/branches' - to get bank branches as per city.
'/api/branches/autocomplete' - to get bank braches according to the input.
```

## Deployment

- This application is deployed on kubernetes cluster(EKS).
- Any commit to the repository starts the codepipline.
- The codebuild generates docker image and pushes it to the ECR. New image can be updated using deployment.spec in EKS.
- The deployment is exposed using load-balancer service.
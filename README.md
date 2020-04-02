# Tag EKS managed node group AutoScaling instances

EKS managed node groups creates instances with no `Name` tag, making it hard to identify in the AWS management console. This serverless app tags all launched instances with the node group name by receiving a AutoScaling group Cloudwatch event via Event Bridge triggering a corresonding lambda function.

## License
MIT

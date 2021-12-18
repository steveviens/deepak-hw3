aws cloudformation create-stack \
            --stack-name 'hw3-sagemaker-stack' \
            --capabilities CAPABILITY_NAMED_IAM \
            --template-body file://../cft/sagemaker_stack.yml

# REFERENCES:
#   AWS CloudFormation CLI Command Reference v2
#   https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html

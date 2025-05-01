# AzureDevOps-fabric-cicd-with-automated-tests to show how to operationalize fabric-cicd to work with Microsoft Fabric and YAML Pipelines in Azure DevOps and perform automated tests

Contains three different YAML files which can be used operationalize [fabric-cicd](https://github.com/microsoft/fabric-cicd) to work with Microsoft Fabric and YAML Pipelines in Azure DevOps and perform automated tests. 

Initially based on a blog post I published that shows how to [automate testing Microsoft Fabric Data Pipelines with YAML Pipelines in Azure DevOps](https://www.kevinrchant.com/2025/03/18/operationalize-fabric-cicd-to-work-with-microsoft-fabric-and-yaml-pipelines/).

This repository currently caters for the three below scenarios.

1. [fabric-cicd-demo-variables.yml](/AzureDevOpstemplates/fabric-cicd-demo-variables.yml) - Pipeline that is fully orchestrated Azure Pipeline variables. For scenarios where all the values are constant.
2. [fabric-cicd-demo-wsparameters.yml](/AzureDevOpstemplates/fabric-cicd-demo-wsparameters.yml) - Pipeline that contains parameters that affect workspace values. Including workspace ID and items to deploy.
3. [fabric-cicd-demo-gblparameters.yml](/AzureDevOpstemplates/fabric-cicd-demo-gblparameters.yml) - Pipeline that contains global parameters. Suited for Option four in the recommended CI/CD options article by Microsoft.

You can find all the YAML files in the [AzureDevOpstemplate subfolder](/AzureDevOpstemplates). All of files contain details about what variables and/or prarameters are required for each one.

Currently there is stage in each pipeline called Test data Pipeline which caters for performing tests aginst the "Run Hello World" Data Pipeline. Based on the [Data Factory Testing Framework](https://github.com/microsoft/data-factory-testing-framework) .You can find the relevant python file in the "Tests" subfolder of the repository.

One quick way to get started is to [import the repository into Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/git/import-git-repository?view=azure-devops&WT.mc_id=DP-MVP-5004032%3Fview%3Dazure-devops). From there, [create a pipeline from an existing YAML file](https://xeladu.medium.com/how-to-create-a-pipeline-from-an-existing-yaml-file-in-azure-devops-4c41e74fde2b).

All of the samples of Fabric items provided in the worskpace folder are from the [original fabric-cicd repository](https://github.com/microsoft/fabric-cicd). However, I do recommend testing with your own items stored in a repository that is the backend for a workspace configured with Microsoft Fabric Git integration.

In addition, you can customize the ["parameter.yml" file](/workspace/parameter.yml) to suit your requirements.

This repository is provided "as is" based on the [MIT license](https://opensource.org/licenses/MIT). Basically, I am not responsible for your use of it.

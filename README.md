# Clock Eexcersise
This codebase shows how to calculate angle between clock faces.Ex.Hours=05 minutes=30 Angle :15.00
user input the time on frontend html form and he/she gets the angle in return.
# Link for front end input form for user hosted on Cloud RUN
**https://clock-angle-icbqkvt2oa-ue.a.run.app/** 

# Technology Stack 
1) Python
2) Cloud source repository
3) Cloud build
4) docker
5) Cloud container
6) Cloud Run 

# Architechire 
![Image]()

# CICD Working 

1) Developer creates feature branch for new feature and push into feature branch.

2) Reviewer Checks the changes and Commit that changes into Master Branch.

3) As soon as commit happens in master branch Cloud build triggers.

4) Cloudbuild Builds a docker image which is written in Dockerfile(in root direcotry)  and install a necessary dependency.
   Also Cloud build runs the **unit test cases** and ***pylint**.if test case fails then deployment fails
   
5) After successfully building a docker image it gets deployed on Cloud Run(Server less compute engine for container).

# How to deploy 
1) Make sure in master branch of your repository **cloudbuild.yml** and **Dockerfile** is in place and on the root directrory.

2) Create a trigger in cloudbuild for your master branch.
    - Name -name Of trigger
    - Event (Repository event that invokes trigger)- Push to branch
    - Source(Branch)- ^master$
    - Build configuration- Specify the path to a Cloud Build configuration file in the Git repo
    - Save.
    
3) Once any commit happen into master branch, build and deployment starts on cloud build and cloud run respectively.

# Future Scope
1) Time can be sent through pubsub and can be pull from python app.
2) Once app calculates a angle that can be store on bigquery or cloud sql.
3) kubernetes and Anthos can be explored and can be evaluated for deployment.
4) As more focus was on Devops practices ,beautification of front end can be done later.
5) Add local and stackdriver logging




  
# devops-april-2021

#Commonly used maven commands

### Checking maven version
```
mvn --version
```

### Listing Maven default life-cycle phases
```
mvn help:describe -Dcmd=compile
mvn help:describe -Dcmd=validate
mvn help:describe -Dcmd=test
```

Any one of the above commands will list the Maven default life-cycle phases.  
You may substitute any phase that you remember in the default lifecycle.

### Listing Maven clean life-cycle phases
```
mvn help:describe -Dcmd=clean
```

### Listing Maven site life-cycle phases
```
mvn help:describe -Dcmd=site
```

### Finding the goals supported by a plugin
```
mvn help:describbe -Dplugin=org.apache.maven.plugins:maven-compiler-plugin:3.1 -Ddetail
```

### Just compile all the files in src/main/java and its sub-directories
```
mvn compile
```

### Compile application and execute automated test cases 
```
mvn test
```

### Deleting target folder
```
mvn clean
mvn pre-clean
mvn post-clean
```
Any one of the above commands will list clean life-cycle phases.

### Creating jar/war/ear depending on the Maven project type
```
mvn package
```

### Installing the artifacts(jar,war,ear) into Maven local repository(.m2 folder)
```
mvn install
```

### Deploying maven artifacts(jar,war,ear,etc) into Sonatype Nexus/JFrog Artifactory or Weblogic/Websphre/Tomcat etc.,
```
mvn deploy
```

This requires adding distributionManagement tag in pom.xml file
```
<distributionManagement>
     <repository>
          <id>artifactory</id>
          <url>http://localhost:8081/artifctory/tektutor</url>
     </repository>
</distributionManagement>
```

You also need to provide the artifactory credential in settings.xml file
```
<servers>
   <server>
       <id>artifactory>
       <username>admin</username>
       <password>Admin@123</password>
   </server>
</servers>
```

### Enabling build debug info(verbosity)
```
mvn clean deploy -X
```
The -X switch helps in troubleshooting issues by enabling verbosity. This can be used with any maven command.


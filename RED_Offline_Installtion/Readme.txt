Instruction for Offline installation of RED 

For Windows

1) Install Java if not already installed. (jdk-8u151-windows-x64.exe)
2) Extract RED[RED_0.8.2.20171218124404-win32.win32.x86_64.zip] in folder of your choice. I would prefer C:\ or C:\users\<youruername>\
3) We need Pydev to develop and/or debug python. so extract the pydev's zip and copy features and plugins fodler to <REDExtractedFolder>\

We are done with RED installation and we need to do one additional configuration to debug Robot and Python togeather.

1) Copy runPyDevDebug.py to <REDExtractedFolder>\
2) Open RED and open your project (In our case TestAutomation or iRobot folder) using File --> Open Projects from File System
3) open Windows --> Perspective --> Open Perspective --> Other --> Pydev
4) Right Click on project and Click on RobotFramework --> Configure as Robot Project
5) Right Click on project and Click on pydev --> set as pydev project (It may ask for config of python, please configure python2.7) (If you are using different version python map appropriate)
6) Go to Windows --> Preference --> Pydev --> Debug and select Remote debugger server activation as Keep always on
7) Go to Windows --> Preference --> RobotFramework --> Launching --> Default Launch Configuration. Give following values
	7.1) Additional Robot Framework arguments as -d C:/tmp/tempresults -L TRACE
	7.2) In Executable file: Select python.exe under python 2.7 installation (If you are using different version python map appropriate)
	7.3) In Additional executable file arguments: give the complete path of runPyDevDebug.py. As we copied this to <REDExtractedFolder>, it should be there
	7.4) Click Apply and Close
8) Keep the break point in robot and python files and debug the script :) 

Happy scrpting and Debugging.

# Face-Recognition

To run Python Script, a script_runner.bat file has already been created. You just have to edit this
file and change addresses of python.exe (as it will be different in your laptop as compared to
mine) and script which you want to run.
• Download all the files and get the location where you have saved your files.
• Install all the prerequisites using pip install -r requirements.txt
• Run create_face_datasets.py using .bat file (as mentioned above). Make sure you have
changed the address of xml file in script otherwise you will get an error.
• Now run training_model.py. You can check trainer folder has been created and yml file is
inside it.
• Now change name of script in .bat file to lock_unlock_face_recognition.py and run .bat
file. This will run lock_unlock_face_recognition.py.
• In order to make above py file run automatically, you will have to setup task scheduler.
For this open Windows Task Scheduler and Create Task. A window will appear. In
Triggers tab click New and select 'On workstation Unlock' in drop down menu.
• Now in Action tab, click new and select 'Start a Program' in drop down menu, Then
browse the script_runner.bat file and select it.
It has helped me in the security purpose to secure the system so that no other person can
use my PC without my permission .It is the advanced version of security other than finger
print and the password. Compared to other biometric traits like palm print, Iris, finger print
etc., face biometrics can be non-intrusive. They can be taken even without user’s
knowledge and further can be used for security based applications like criminal detection,
face tracking, airport security, and forensic surveillance systems. Face recognition involves
capturing face image from a video or from a surveillance camera

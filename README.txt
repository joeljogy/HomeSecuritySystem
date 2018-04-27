For running the SSH file, 

1) Find the IP address of the Raspberry Pi using the command 'arp -a' on cmd after connecting the Raspberry Pi to laptop. 
2) Edit the IP address mentioned in the code. 
3) To test the IP address, open Putty, add the IP address on Port 22, SSH and hit Open. If the option, 'login as' comes then the entered IP address is valid. 
4) login as: 'pi', password: 'raspberry' 
5) Use VNC Viewer to be able to use laptop as monitor for the Raspberry Pi. 
6) Before opening VNC Viewer, enter 'vncserver :1' in the terminal of Raspberry Pi 
7) Then open VNC Viewer, enter the valid IP address of Raspberry Pi with ':1'. 
   Eg: 197.02.1.255:1 
8) If password is requested, enter 'raspberry'

In case, IP address is unable to be found, 

1) Use Advanced IP Scanner and scan through '10.86.0.1 - 10.86.7.254'
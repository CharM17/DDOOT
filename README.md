# <p align="center">DDOOT</p>

<p align="center">Uses winreg in Python to enable/disable several Windows Update services such as:</p>

<p align="center"> Delivery Optimization
 
<p align="center"> Windows Update Orchestrator Service
 
 <p align="center">Windows Update Medic Service
  
 ## <p align="center"> First time use requires changing privilege's so each service can enabled/disabled by the program </p>

Open registry editor

![Step1](https://user-images.githubusercontent.com/62578869/185758619-fc0f2359-05af-46e0-b80c-dd0abbb5fc84.png)


Go to Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services

This is where all Windows Update services are located.


Find the "DoSvc" service (Delivery Optimization)

Right click on it and choose permissions

![Step2](https://user-images.githubusercontent.com/62578869/185758744-f4b495fd-2f16-43bd-82de-c5069bd6bcf8.png)


Click Add

![step3](https://user-images.githubusercontent.com/62578869/185769117-7c629dc3-b42b-4dd5-81b9-e0a5e38a3276.png)


Click Advanced

![step4](https://user-images.githubusercontent.com/62578869/185758782-57a4879a-984b-4971-984b-f970025e081a.png)


Click Find Now

![step5](https://user-images.githubusercontent.com/62578869/185758783-9e51ea4e-2c6a-45f6-b702-cc04949b02e3.png)


Select the account that you are currently using from the list

![step6](https://user-images.githubusercontent.com/62578869/185758785-e54ff4e5-4da7-463c-8092-c95a883e9e81.png)


Press OK

![step7](https://user-images.githubusercontent.com/62578869/185758788-8eabd435-f061-4027-b9f5-40107eb62c0a.png)


Select your account from the list, click "Allow" under full control, click apply, then ok.

![step8](https://user-images.githubusercontent.com/62578869/185802024-cf1b0796-7b96-4543-a614-2b85394dcfba.png)


Repeat this for "UsoSvc" and "WaaSMedicSvc"





# EOTS  — Journal Export

- Exported at: 2026-06-22T15:51:53Z
- Project ID: 4547
- Entries: 9

## Entry 1
- ID: 14120
- Author: diaxx
- Created At: 2026-06-14T23:48:10Z

### Content

## starting a new project 

this project is a eots ( electro optical targeting system ) it works like a gimbal can rotate and pan since its a 2 axis because 3 axis cost is not justified thats why i went with two axis in this journal i made a lot of advancement i created the chassis the gimbal interior added component such as the motor , rasberry pi zero 0 and camera which consist of 2 spectrum camera we call this a dual band EO so i have a day / night camera and a thermal camera ( its a 8x8 camera its good enough for me i can do fusion between those two ) the reason on why i decided to make this project is that i love gimbal and electro optics the feeling when you can track something with just a click of a button a passing car for exemple ( shit this doesn't sound good ) 
![Capture d'écran 2026-06-14 041628.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzM1NjIsInB1ciI6ImJsb2JfaWQifX0=--79d61c866f862d4bb8a18fca466144c50e6fec8b/Capture d'écran 2026-06-14 041628.png)
![Capture d'écran 2026-06-14 023041.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzM1NjMsInB1ciI6ImJsb2JfaWQifX0=--849a3a51abadd2e062156bc303d0be163617089c/Capture d'écran 2026-06-14 023041.png)
 next i am going to build the foc ( field oriented control ) board so i can precisely control those bldc motors and i will build the gcs ( ground control station ) out of python !!! im sooo  excited see yall 

### Recording Links

- https://lookout.hackclub.com/api/media/6ee5df61-956c-4f03-adf4-5b3cd5fa044e/video.mp4

## Entry 2
- ID: 14203
- Author: diaxx
- Created At: 2026-06-15T09:17:59Z

### Content

hi and welcome again to my journal today i attacked the FOC board and did 90% completion. this foc board will control almost everything of the gimbal it will move the 2 brushless motor and power them from my 3s lipo 12V i built it around a stm32f405rgt6 because its powerful enough with its clockspeed of around 168Mhz i used a step down module to step 11v to 5v then i got an ldo to get 3.3v from that 5v 
![SCH_Schematic1_1-P1_2026-06-15.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzM3NTAsInB1ciI6ImJsb2JfaWQifX0=--dcbbf9b04cda10dfd29d1cac95c08bf2944af05e/SCH_Schematic1_1-P1_2026-06-15.png)


### Recording Links

- https://lookout.hackclub.com/api/media/261ad7bf-df15-4741-a416-8691a65aea68/video.mp4

## Entry 3
- ID: 14206
- Author: diaxx
- Created At: 2026-06-15T09:34:38Z

### Content

i just finished the schematics of the FOC board i added connectors to facilitate connection between sensor and motors i will hop on the pcb layout for the next journal 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzM3NTcsInB1ciI6ImJsb2JfaWQifX0=--e977817cdf6d548c84c0b241a9340a5ac4f45ec9/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/e740d2a4-c575-43ca-b38f-cbfea2605d6d/video.mp4

## Entry 4
- ID: 14592
- Author: diaxx
- Created At: 2026-06-16T18:17:43Z

### Content

FINALLY AFTER GREAT SUFFERING  i finished the FOC board layout and routing i implemented usb-c to flash and talk with the foc and also added jst pin for two encoder and one imu that is going to be inside the ball ( the spinning ball with camera lets call it the payload ball ) i thickened the vbat and motor phase trace to support their voltage  
![Capture d'écran 2026-06-15 122545.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ2MDIsInB1ciI6ImJsb2JfaWQifX0=--360a8a1c72ff5748d557a41432f1aef1da1375eb/Capture d'écran 2026-06-15 122545.png) here i had to change the usb -c for the differential 
![Capture d'écran 2026-06-15 132907.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ2MDMsInB1ciI6ImJsb2JfaWQifX0=--16245e342786fafa96d3a47256a2f91b6393c8da/Capture d'écran 2026-06-15 132907.png)
![Capture d'écran 2026-06-15 144745.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ2MDQsInB1ciI6ImJsb2JfaWQifX0=--af7b998cf49fc4a602d9cda42db420d7335621a9/Capture d'écran 2026-06-15 144745.png) also i went thru stm to assign pins to their respective role here is an image resuming that 
![Capture d'écran 2026-06-15 095450.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ2MDUsInB1ciI6ImJsb2JfaWQifX0=--d4f0763216e9bcca77c3a05eb5a7a92c06f9d397/Capture d'écran 2026-06-15 095450.png) here is the encoder that is going to be used
![Capture d'écran 2026-06-14 232111.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ2MDksInB1ciI6ImJsb2JfaWQifX0=--3b5eadc37ad3f568bd8a257b3f472eef5b1ba68c/Capture d'écran 2026-06-14 232111.png)


### Recording Links

- https://lookout.hackclub.com/api/media/5754e1eb-07df-446a-a06e-c7e1d952c2b2/video.mp4

## Entry 5
- ID: 15087
- Author: diaxx
- Created At: 2026-06-18T22:24:40Z

### Content

i made some huge changes in the cad such as i split the ball to 3d print it and added screw hole because we are professional we don't do glue here! other than that i added mounts for the cameras ,the raspberry pi zero 2w and i also modeled a slip ring cuz i didn't find in grabcad then i implemented it while adding its mount  
![Capture d'écran 2026-06-14 041628.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzU5NDQsInB1ciI6ImJsb2JfaWQifX0=--f110cabb10735ae40860ea4b0f2a5faa13cf0d92/Capture d'écran 2026-06-14 041628.png) i also added hole to mount the whole ball to the motor 


### Recording Links

- https://lookout.hackclub.com/api/media/6ea9e612-d17a-4604-8edc-575acab59e57/video.mp4

## Entry 6
- ID: 15094
- Author: diaxx
- Created At: 2026-06-18T23:37:51Z

### Content

i just set up my github repo did a good readme for this eots project i also decided to call this project: EOTS i added a bom.csv 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzU5NzEsInB1ciI6ImJsb2JfaWQifX0=--266cc95e745ce7c42904c94c8b6af04b9d341e7d/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/4ee8fb73-376d-4626-85e3-62814cef8b55/video.mp4

## Entry 7
- ID: 15096
- Author: diaxx
- Created At: 2026-06-18T23:46:42Z

### Content

the last steps before sending this project i updated some of the cad models thanks to a person suggestion, also i made the zine 
![zine.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzU5NzUsInB1ciI6ImJsb2JfaWQifX0=--8eabc817d32a92e31c2c7d38f37f2014cfbdc57a/zine.png)
i know its not that good but its all i could do im not proficient with Figma. I set up my github repo with a good readme added all the necessary files like bom.csv / gerber / cad model and structured them nicely with folder  
![Capture d'écran 2026-06-18 184651.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzU5NzYsInB1ciI6ImJsb2JfaWQifX0=--09488b99f958d734b9c44570ee9ec5adee4ff5ea/Capture d'écran 2026-06-18 184651.png)


### Recording Links

- https://lookout.hackclub.com/api/media/410a64bc-7fc6-4ba3-8244-18ac1eea6165/video.mp4

## Entry 8
- ID: 15402
- Author: diaxx
- Created At: 2026-06-20T00:52:01Z

### Content

i HAD to reduce my pcba price since my BOM wasn't really optimized also i added screw hole to the pcb the total price of the pcb went from 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY2ODUsInB1ciI6ImJsb2JfaWQifX0=--83ea5a267bb167abc3346fcb6697bd1fba6dc477/image.png)
to this 
![Capture d'écran 2026-06-20 005239.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY2ODcsInB1ciI6ImJsb2JfaWQifX0=--3c48562152357d032b3fdd29d9251b6fd11a51e0/Capture d'écran 2026-06-20 005239.png) 
### how did i do it 

i just changed passive component from extend to basic because extended component charge 3$ loading fee 

i choose the cheapest shipping 
![Capture d'écran 2026-06-20 005801.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY2OTEsInB1ciI6ImJsb2JfaWQifX0=--101ee50e96b26e8c961c56ce2050c22b9a4fe6fb/Capture d'écran 2026-06-20 005801.png)
i also picked the biggest coupons 
![Capture d'écran 2026-06-20 005755.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY2OTIsInB1ciI6ImJsb2JfaWQifX0=--d20c4468f4d6d217185ef48fcd90805fb74a0fa2/Capture d'écran 2026-06-20 005755.png)
and here is the total 

### Recording Links

- https://lookout.hackclub.com/api/media/ff1a3a90-957c-4574-b43e-1b231e1720c8/video.mp4

## Entry 9
- ID: 15769
- Author: diaxx
- Created At: 2026-06-20T20:31:33Z

### Content

# The Last Checks 
i just optimized my bom like crazy ( made it less expensive ) switched to cheaper alternative just like what i did with pcb Assembly for exemple i switched a 7$ connector with a 3$ one same same but diff price! Additionally i made the geometry of the 3d printed metal bracked easier to print and that made the price 10$ cheaper here is how the bom was before :  
## the old bom
![Capture d'écran 2026-06-18 181653.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzc2MTIsInB1ciI6ImJsb2JfaWQifX0=--88e2977727c2f20ad03dc04ff93080a8dd6a5c37/Capture d'écran 2026-06-18 181653.png)
### THE TOTAL WAS : 3,770.84 DH ( 400$) 
## the new bom
![Capture d'écran 2026-06-20 205505.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzc2MTcsInB1ciI6ImJsb2JfaWQifX0=--f6f04d23a005f11b7cd3467850e152dd4e3484d1/Capture d'écran 2026-06-20 205505.png)
### the total is now : 3,153.12dh ( 341.8) 

this is 617.72 dh difference 

## Now doing the last checks 
▢ The PCB is finished 
▢ 3D cad model is done 
▢ github repo is fully built and done 
▢ the bom was done and optimized 
▢ Zine page is awesomely done
▢  Firmware is ok 
▢ no floating object in the cad 

I think this is the end of our little project ( or not depends if i get reject hopefully not ! ) i am ready to click send !!!! (●'◡'●) this was fun. 



### Recording Links

- https://lookout.hackclub.com/api/media/f54878fe-931f-4c71-a32d-f38f5f914b6a/video.mp4

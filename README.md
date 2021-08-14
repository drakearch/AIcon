# AIcon

App for the Artificial Intelligence Conference, AIcon makes the largest event of the Artificial Intelligence community in which passionate about learning, undertaking and innovating are in the same place to listen to the industry experts who share their knowledge for hours.</string>
    

## App Navigation
![AIcon app navigation](https://cdn.jsdelivr.net/gh/drakearch/shared@master/ai-con/img/ai_con_navigation.png)

## Project Setup

### Firebase

1. Go to https://console.firebase.google.com/ and create a new project.
2. Once the project is created, go to the *Firestore Database* section, then create a new database in **Test mode**.
3. For the next step, go to **Project settings > Service accounts**, then generate a new private key in **Firebase Admin SDK** for **Python**. After downloading the file, rename it to ``serviceAccountKey.json`` and move it to the root of the project.
![Firestore generate key](https://cdn.jsdelivr.net/gh/drakearch/shared@master/ai-con/img/firestore_generate_key.png)

4. If you don't have python. install it, then install the firestore_admin library.
```console
$ pip install firestore_admin
```
5. Then, execute the python script to populate the firestore collections.
```console
$ python firestore_setup.py
Done!
```
6. On the other hand, create a new Android app on the *Project Overview* section. Fill the Register app form with data of the android app, for Singning certificate SHA-1, go to gradle tab on the right side of Android Studio, and generate it.
7. Following the guide to **Add Firebase to your Android app**, donwload the configuration file ``google-services.json`` and move it to the ``app/`` folder. Then, continue with the next Firebase instructions. Finally, rebuild the project.

### Google Maps

1. Go to https://console.cloud.google.com/apis/dashboard and select you project on the top toolbar. Then, click on the **+ Enable apis and services** button, then enable the **Maps SDK for Android**.
2. To create new credentials, go to the section *Credentials* and click on the **+ Create Credentials** button. Then, select **API key**, copy your API key and paste it on the line 14 of the ``AndroidManifest.xml`` file.
![Google Maps API key](https://cdn.jsdelivr.net/gh/drakearch/shared@master/ai-con/img/google_maps_api_key.png)
3. Finally, restrict the key just for Android apps and create a new item with the same values as step 6 on Firebase setup section.

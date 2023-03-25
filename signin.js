import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDybkQ-gyeyXoXZlF8fy26Y5JXo4svBq6Y",
  authDomain: "parking-management-4e32d.firebaseapp.com",
  projectId: "parking-management-4e32d",
  storageBucket: "parking-management-4e32d.appspot.com",
  messagingSenderId: "1091771919954",
  appId: "1:1091771919954:web:1fa7d43eecdf4e6cdd798b",
  measurementId: "G-QQ1YN4MW68"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);

import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

import { getAuth, onAuthStateChanged } from "firebase/auth";

onAuthStateChanged(auth, (user) => {
  if (user) {
    // https://firebase.google.com/docs/reference/js/firebase.User
    const uid = user.uid;
    location.href = "C:/Users/dell/Documents/GitHub/hashcode-meandthebois/Smart-Parking-System/figmatohtml/7/index.html";
    // ...
  } else {
    //wrong password instructions
    location.href = "C:/Users/dell/Documents/GitHub/hashcode-meandthebois/Smart-Parking-System/figmatohtml/7/index.html";
  }
});
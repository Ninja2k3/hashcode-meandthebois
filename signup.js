import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
//config
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

createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed in 
    const user = userCredential.user;
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    // ..
  });
// index.js
import React from 'react';
import './index.css';
// Import your Redux store
import App from './App'; // Replace with the path to your main component

// Import createRoot from "react-dom/client" instead of "react-dom"
import { createRoot } from 'react-dom/client';


// Use createRoot instead of ReactDOM.render
createRoot(document.getElementById('root')).render(

    <App />
  
);

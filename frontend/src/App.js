// src/App.js

import React from 'react';
import './App.css';
import HelloWorld from './HelloWorld';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to React with Flask</h1>
        <HelloWorld />
      </header>
    </div>
  );
}

export default App;

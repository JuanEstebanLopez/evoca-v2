import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

// Import Rebass Components
import { Button, Badge } from 'rebass'
// Customized components
import Navbar from './Navbar'


class App extends Component {
  render() {
    return (
      <div className="App">
		<Navbar />

        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          <h2>Rebass Component Test</h2>
          <Button>Click here</Button>
          <Badge>Badge</Badge>
        </div>
      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';
import Home from './Home';
import AnimoosNavbar from './AnimoosNavbar';

class App extends Component {
  render() {
    return (
	  <div>
	  	  <AnimoosNavbar />	
      	  <Home />
      </div>
    );
  }
}

export default App;

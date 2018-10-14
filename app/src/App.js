import React, { Component } from 'react';

// redux components
import { connect } from "react-redux"

// app imports
// import { actions } from "./actions/someActions"


class App extends Component {
  state = {}

  render() {
    // const someAction = this.props.someActionMethod

    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to React</h1>
        </header>
      </div>
    );
  }
}


function mapStateToProps(state) {
  return {
    // Add slice of the store you want to import into the component
  };
}

export default connect(mapStateToProps)(App);

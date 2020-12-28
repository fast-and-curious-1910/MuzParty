import React, { Component } from "react"  // We destructure Component from react 
import {render } from "react-dom" // Very important

class App extends Component {
    constructor(props) {
        super(props); // We take in props (needed for react)

    }
    render() {
        return (
        <div> 
            <h1> Hello World</h1>
        </div>) // This is not a string , this is a JSX element. React also requires one parent element
    }
};

export default App;

let appDiv = document.getElementById('app');
render(<App/>,appDiv) // Very Important!
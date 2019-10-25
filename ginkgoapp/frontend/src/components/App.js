import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import MainContainer from './MainContainer'

class App extends Component {
	render() {
		return (
			<div className="App">
				<MainContainer/>
			</div>
		);
	}
}

ReactDOM.render(<App/>, document.getElementById('app'));

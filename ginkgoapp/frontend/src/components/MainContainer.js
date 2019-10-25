import React, {Component} from 'react';

class MainContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			input: "hellor"
		}
	}

	render() {
		return (
			<h1>{this.state.input}</h1>
		);
	}
}

export default MainContainer;

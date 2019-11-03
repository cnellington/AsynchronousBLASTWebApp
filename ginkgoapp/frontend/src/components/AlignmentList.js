import React, {Component} from 'react';

class AlignmentList extends Component {

	constructor(props) {
		super(props);
		this.state = {
			alignments: [],
			display: []
		};
	}

	update() {
	    this.loadAlignments();
	    this.updateAlignments();
	 }

	componentDidMount() {
		this.interval = setInterval(() => this.update(), 1000);
		this.loadAlignments();
	    this.updateAlignments();
	}

	componentWillUnmount() {
		clearInterval(this.interval);
	}

	loadAlignments() {
		let connection = "http://"+this.props.backend+":8000/api/alignments/id-specific/";
		let payload = {"ids": localStorage.getItem(this.props.save_loc)};
		fetch(connection,
			{
				method: 'post',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(payload)
			})
			.then(res => res.json())
			.then(
				(json) => {
					if (typeof(json) != "undefined") {
						this.setState({seconds: this.state.seconds, alignments: json, display: this.state.display});
					}
				}
			);
	};

	updateAlignments() {
		let newAlignments = [];
		for(let i = 0; i < this.state.alignments.length; i++) {
			let result = this.state.alignments[i];
			console.log(result);
			newAlignments.push(
				<div key={i}>
					<br></br>
					<p>query: {result["sequence"]}</p>
					<p>found in <strong>{result["result_name"]}</strong> at bp {result["result_start"]} </p>
				</div>
			);
		}
		this.setState({seconds: this.state.seconds, alignments: this.state.alignments, display: newAlignments});
	};

	render() {
		return (
			<div>
				<p>Alignment Results:</p>
				{this.state.display}
			</div>
		);
	}
}

export default AlignmentList;

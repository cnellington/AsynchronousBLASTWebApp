import React, {Component} from 'react';
import SearchBar from './SearchBar';
import Button from './Button';
import AlignmentList from './AlignmentList';
import * as fetch from "node-fetch";

class MainContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			seq: "",
			alignments: ["dna seq"]
		}
	}

	componentDidMount() {
		this.loadAlignments();
	}

	loadAlignments = () => {
		let connection = "http://localhost:8000/api/alignments/";
		fetch(connection, {method: 'get'})
			.then(res => res.json())
			.then(
				(json) => {
					console.log(json);
					if (typeof(json) != "undefined") {
						this.setState({seq: this.state.seq, alignments: json});
					}
				}
			);
		console.log("getting query results");
	};

	updateSeq = (event) => {
		let sequence = event.target.value;
		this.setState({seq: sequence, alignments: this.state.alignments});
	};

	submit = (event) => {
		let connection = "http://localhost:8000/api/alignments/";
		let payload = {"sequence": this.state.seq}
		fetch(connection, {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(payload)
		}).catch((error) => alert("error"));
		this.setState({seq: "", alignments: this.state.alignments});
		console.log("submitted query");
	};

	render() {
		return (
			<div>
				<SearchBar title={"DNA Alignment: "} value={this.state.seq} onChange={this.updateSeq}/>
				<Button color="primary" onClick={this.submit} value="Submit"/>
				<AlignmentList alignments={this.state.alignments}/>
			</div>
		);
	}
}

export default MainContainer;

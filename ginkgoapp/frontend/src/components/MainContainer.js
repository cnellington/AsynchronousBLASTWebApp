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
			alignments: []
		};
		this.save_loc = "ginkgoSearchIds";
		this.backend = "localhost";
		if (localStorage.getItem(this.save_loc) === null) {
			localStorage.setItem(this.save_loc, JSON.stringify([]));
		}
	}

	updateSeq = (event) => {
		let sequence = event.target.value;
		this.setState({seq: sequence});
	};

	submit = (event) => {
		let connection = "http://"+this.backend+":8000/api/alignments/";
		let payload = {"sequence": this.state.seq};
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
					if (typeof (json) != "undefined") {
						let searchIds = JSON.parse(localStorage.getItem(this.save_loc));
						searchIds.push(json["id"]);
						localStorage.setItem(this.save_loc, JSON.stringify(searchIds));
					}
				}
			);
		this.setState({seq: ""});
	};

	resetUser = (event) => {
		localStorage.setItem(this.save_loc, JSON.stringify([]));
	}

	render() {
		return (
			<div className={"text-center"}>
				<SearchBar title={"Enter DNA Query: "} value={this.state.seq} onChange={this.updateSeq}/>
				<Button color="primary" onClick={this.submit} value="Submit"/>
				<Button color="secondary" onClick={this.resetUser} value="Clear"/>
				<AlignmentList save_loc={this.save_loc} backend={this.backend}/>
			</div>
		);
	}
}

export default MainContainer;

import React, {Component} from 'react';
import SearchBar from './SearchBar';
import Button from './Button';
import AlignmentList from './AlignmentList';

class MainContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			seq: "",
			alignments: []
		}
	}

	componentDidMount() {
		this.loadAlignments();
	}

	loadAlignments = () => {
		let connection = "grab all processed submissions";
		let alignmentList = ["DNA SEQ"];
		this.setState({seq: this.state.seq, alignments: alignmentList});
		console.log("getting query results");
	};

	updateSeq = (event) => {
		let sequence = event.target.value;
		this.setState({seq: sequence, alignments: this.state.alignments});
	};

	submit = (event) => {
		let connection = "submit an alignment request";
		this.setState({seq: "", alignments: this.state.alignments});
		console.log("submitting query");
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

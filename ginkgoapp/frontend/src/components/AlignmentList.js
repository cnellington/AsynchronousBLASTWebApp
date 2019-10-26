import React, {Component} from 'react';

class AlignmentList extends Component {

	constructor(props) {
		super(props);
		this.state = { time: Date.now() };
	}

	formatAlignments = () => {
		let ret = []
		for(let i = 0; i < this.props.alignments.length; i++) {
			let result = this.props.alignments[i];
			ret.push(
				<div style={{border: "solid 1px red"}} key={i}>
					<p>{result["sequence"]}</p>
					<p>{result["status"]}</p>
					<p>{result["created"]}</p>
				</div>
			);
		}
		return ret;
	};

	render() {
		return (
			<div>
				{this.formatAlignments(this.props.alignments)}
			</div>
		);
	}
}

export default AlignmentList;

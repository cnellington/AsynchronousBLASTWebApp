import React, {Component} from 'react';

class AlignmentList extends Component {
	
	formatAlignments = () => {
		let ret = []
		for(var i = 0; i < this.props.alignments.length; i++) {
			ret.push(<p key={i}>{this.props.alignments[i]}</p>);
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

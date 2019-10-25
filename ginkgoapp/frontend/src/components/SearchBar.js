import TextField from '@material-ui/core/TextField';
import React, {Component} from 'react';

class SearchBar extends Component {
	render() {
		return (
			<div className="center-text">
				<p>{this.props.title}</p>
				<TextField
					id={this.props.id}
					label={this.props.label}
					value={this.props.value}
					onChange={this.props.onChange}
					className={this.props.className}
					InputLabelProps={{
						shrink: true,
					}}
					autoFocus
				/>
			</div>
		);
	}
}

export default SearchBar;

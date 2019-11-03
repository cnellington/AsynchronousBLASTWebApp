import TextField from '@material-ui/core/TextField';
import React, {Component} from 'react';

class SearchBar extends Component {
	render() {
		return (
			<div>
				<h3>{this.props.title}</h3>
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

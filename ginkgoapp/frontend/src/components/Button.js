import Button from '@material-ui/core/Button';
import React, {Component} from 'react';

class CustomButton extends Component {
  render() {
    return (
      <div className="center-text button">
        <Button variant="contained" color={this.props.color} onClick={this.props.onClick}>
          {this.props.value}
        </Button>
      </div>
    );
  }
}

export default CustomButton;

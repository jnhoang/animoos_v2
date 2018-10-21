import React, { Component } from 'react';
import { Navbar, NavItem } from 'react-materialize';

class AnimoosNavbar extends Component {
	render() {
		return (
			<Navbar brand='logo' left>
			    <NavItem href='get-started.html'>Getting started</NavItem>
			    <NavItem href='components.html'>Components</NavItem>
			</Navbar>
		)
	}
}

export default AnimoosNavbar;
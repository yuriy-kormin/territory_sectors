import React from 'react';
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import {useDispatch, useSelector} from "react-redux";
import {userLogout} from "../store/UserReducer";
import {getUser} from "../store/selectors/getUser";

const NavBar = () => {
    const dispatch = useDispatch()
    const user = useSelector(getUser);

    return (
        <Navbar expand="md" bg="dark" data-bs-theme="dark" className="bg-body-tertiary">
            <Container>
                <Navbar.Brand>
                    <Nav.Link href="/" active className="text-primary">Territory</Nav.Link>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Item className={"text-light"}>{user.is_login?user.username:""}</Nav.Item>
                        {user.is_login && (<Nav.Link onClick={() =>dispatch(userLogout())}>logout</Nav.Link>)}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default NavBar;
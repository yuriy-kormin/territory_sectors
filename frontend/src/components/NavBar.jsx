import React from 'react';
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import {useDispatch, useSelector} from "react-redux";
import {userLogout} from "../store/UserReducer";
import {getUser} from "../store/selectors/getUser";
import Offcanvas from 'react-bootstrap/Offcanvas';
import {faUser} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";


const NavBar = () => {
    const dispatch = useDispatch()
    const user = useSelector(getUser);

    return (
        <Navbar expand={false} bg="dark" data-bs-theme="dark">
            <Container fluid>
                <Navbar.Brand>
                    <Nav.Link href="/" active className="text-primary">Territory</Nav.Link>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Offcanvas bg="dark" data-bs-theme="dark" id="responsive-navbar-nav" placement="end">
                    <Offcanvas.Header closeButton>
                        {user.is_login
                        ?(<Navbar.Text className="text-light justify-content-end flex-grow-1 pe-3">
                                    <FontAwesomeIcon icon={faUser}/>   {user.username}
                            </Navbar.Text>)
                        :<div></div>
                        }
                    </Offcanvas.Header>
                    <Offcanvas.Body>

                        {user.is_login && (<Navbar.Text onClick={() =>dispatch(userLogout())}>logout</Navbar.Text>)}
                    </Offcanvas.Body>

                    {/*<Nav className="me-auto">*/}
                    {/*    <Nav.Item className={"text-light"}>{user.is_login?user.username:""}</Nav.Item>*/}
                    {/*    {user.is_login && (<Nav.Link onClick={() =>dispatch(userLogout())}>logout</Nav.Link>)}*/}
                    {/*</Nav>*/}
                </Navbar.Offcanvas>
            </Container>
        </Navbar>
    );
};

export default NavBar;
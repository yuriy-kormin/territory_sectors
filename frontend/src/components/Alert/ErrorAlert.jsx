import React from 'react';
import {Alert, Modal} from "react-bootstrap";

const ErrorAlert = ({onClose,show,...props}) => {


    return (
        <Modal show={show} onHide={onClose}>
        <Alert
            className='m-0'
            variant='danger'
            {...props}
        >{props.children}</Alert>
        </Modal>
    );
};

export default ErrorAlert;
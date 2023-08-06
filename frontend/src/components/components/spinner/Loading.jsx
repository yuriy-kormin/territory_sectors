import React from 'react';
import {Spinner} from "react-bootstrap";

const Loading = () => {
    return (
            <Spinner
                className='mx-2'
                as="span"
                animation="border"
                size="sm"
                aria-hidden="true"
            />
    );
};

export default Loading;
import React from 'react';
import {Spinner} from "react-bootstrap";

const Loading = ({className, ...props}) => {
    return (
            <Spinner
                className={className}
                as="div"
                animation="border"
                size="sm"
                aria-hidden="true"
                {...props}
            />
    );
};

export default Loading;
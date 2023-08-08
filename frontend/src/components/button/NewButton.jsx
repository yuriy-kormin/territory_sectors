import React from 'react';
import {Button} from "react-bootstrap";

const NewButton = ({children,variant,classes,...props}) => {
    return (
        <Button variant={variant} className={classes} {...props}>{children}</Button>
    );
};

export default NewButton;
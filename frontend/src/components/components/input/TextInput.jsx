import React, {useState} from 'react';
import Form from 'react-bootstrap/Form';
import {Button, FloatingLabel, InputGroup} from "react-bootstrap";
import { faEye, faEyeSlash, faUser, faLock } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const TextInput = ({
                       id,
                       label,
                       icon,
                       type,
                       is_password=false,
                       _ref,
                       ...props
}) => {

    const [showPassword, setShowPassword] = useState(false);
    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    return (
        <InputGroup className="mb-3">
            <InputGroup.Text>
                <FontAwesomeIcon icon={icon}/></InputGroup.Text>
            <FloatingLabel label={label}>
                <Form.Control placeholder={label} id={id}
                              type = {is_password
                                  ? showPassword ? 'text' : 'password'
                                  :"text"
                                }
                              ref={_ref} {...props} />
            </FloatingLabel>
            {is_password &&
                <Button
                    variant="secondary"
                    onClick={togglePasswordVisibility}
                >
                    <FontAwesomeIcon icon={showPassword ? faEyeSlash : faEye} />
                </Button>
            }
        </InputGroup>
    );
};

export default TextInput;
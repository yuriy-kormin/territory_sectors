import React from 'react';
import DivMap from "../components/DivMap";
import LoginForm from "../components/LoginForm";
import {useSelector} from "react-redux";
import {getUser} from "../store/selectors/getUser";

const Start = () => {
    const user = useSelector(getUser);
    return (
        <>
            {user.is_login
                ?<DivMap />
                :<LoginForm />
            }
        </>
    );
};

export default Start;
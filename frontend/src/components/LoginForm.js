import React, {useRef, useState} from 'react';
import TextInput from "./input/TextInput";
import NewButton from "./button/NewButton";
import {Form} from "react-bootstrap";
import {useDispatch} from "react-redux";
import {faUser, faLock} from '@fortawesome/free-solid-svg-icons';
import Loading from "./spinner/Loading";
import ErrorAlert from "./Alert/ErrorAlert";
import {useBackendExchange} from "../hooks/useBackendExchange";
import {LoginQUERY} from "../api-helpers/queries/userQueries";
import {parseAuthResult} from "../api-helpers/lib";
import {userSetAction} from "../store/UserReducer";

const LoginForm = () => {
    const dispatch = useDispatch()
    const [showModal,setShowModal] =useState(false)
    const [fetchResult, setFetchResult] = useState({
        fetching:false,
        result:undefined,
        error:undefined,
    });

    const loginInputRef = useRef();
    const passwordInputRef = useRef();
    const callback = useBackendExchange(LoginQUERY);

    const submitAction = (e) => {
        e.preventDefault()
        setFetchResult({...fetchResult, fetching:true})
        const regexp=/(?<=^\[.*\]\s+)\S.*/gm

        callback({
            username: loginInputRef.current.value,
            password: passwordInputRef.current.value
        }).then((result)=>{

            const resultParsed=parseAuthResult(result)
            setFetchResult({
                fetching: false,
                error: regexp.exec(result.error?.message || ''),
                result:resultParsed
            })
            if (result.error){
                setShowModal(true);
            } else {
                dispatch(userSetAction(resultParsed))
            }
        })
    }
    return (
        <Form className={"mt-5 mx-4"} data-testid='loginForm'>
            {
                <ErrorAlert
                    show={showModal}
                    onClose={() => setShowModal(false)}
                >{fetchResult.error}</ErrorAlert>
            }
            <TextInput
                   id="login_field"
                   label="Login"
                   data-testid='login'
                   icon={faUser}
                   className = {fetchResult.error && !fetchResult.fetching?'is-invalid':''}
                   _ref = {loginInputRef}
                   autoComplete='username'
            />
            <TextInput
                id="password_field"
                label="Password"
                data-testid='password'
                icon={faLock}
                className = {fetchResult.error && !fetchResult.fetching?'is-invalid':''}
                _ref = {passwordInputRef}
                autoComplete='password'
                is_password={true}
            />
            <NewButton
                variant="primary"
                classes={"mt-3"}
                data-testid='login_btn'
                type="submit"
                onClick={submitAction}
                disabled={fetchResult.fetching?'disabled':''}
            >
                Login {fetchResult.fetching?<Loading />:<Loading className='visually-hidden' />}
            </NewButton>
        </Form>
    );
};

export default LoginForm;